from flask import Blueprint, render_template, redirect, current_app, request, url_for
from openai import OpenAI
from config import Config

main = Blueprint('main', __name__)

open_ai_key = Config.OPEN_AI_KEY

client = OpenAI(
    organization='org-rKAJGiGYPIYjgz6o441DkC7V',
    project='proj_Q6YIIPWgtYS8O3W9x5Xvxblz',
    api_key=open_ai_key,
)


@main.route("/", methods= ["GET", "POST"])
def homepage():
    # open_ai_key = current_app.config['OPEN_AI_KEY'] 
    if request.method == "POST":
        redirect(url_for('generate'))

    return render_template('index.html')
    


@main.route("/generate", methods = ["GET","POST"])
def generate():
    
    if request.method == "POST":
        context = request.form.get("context")
        reason = request.form.get("reason")
        details = request.form.get("details")

        prompt = f"""Você é um especialista em criar desculpas engraçadas e criativas. Aqui estão os detalhes:
                    - Contexto: {context}
                    - Razão: {reason}
                    - Detalhes adicionais: {details}

                    Por favor, gere uma desculpa absurda, mas divertida, que combine essas informações. Use um tom leve e engraçado. Seja criativo e exagere o suficiente para surpreender! Tente se ater a 100 no máximo 200 carcteres, só escreva a desculpa"""

        completion = client.chat.completions.create(
            model='gpt-4o',
            messages=[
                {"role": "user", "content": prompt},
            ],
            max_completion_tokens=200,
            stop=['/n', 'FIM'],
            temperature=0.5,

        )
        print(completion.choices[0].message.content)
        response=completion.choices[0].message.content

        return render_template('excuse.html', response=response)