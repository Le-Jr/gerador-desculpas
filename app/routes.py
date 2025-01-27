from flask import Blueprint, render_template, redirect, current_app

main = Blueprint('main', __name__)

open_ai_key = current_app.config['OPEN_AI_KEY']


@main.route("/", methods= ["GET", "POST"])
def homepage():
    return render_template('index.html')

