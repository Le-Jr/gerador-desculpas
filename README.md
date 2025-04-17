# 📝 Gerador de Desculpas

Um aplicativo web feito com Flask que gera desculpas criativas de forma automática. Ideal para quem precisa sair de uma situação embaraçosa com estilo — ou só quer dar boas risadas.

## 🚀 Funcionalidades

- Geração automática de desculpas aleatórias  
- Interface simples e direta  
- Sistema de rotas: `/` (formulário) e `/generate` (resultado)  
- Pronto para expansão com sistema de usuários e precificação  

## ✨ Exemplos de Desculpas

- "Desculpa, meu gato deletou o arquivo final do projeto."  
- "Eu estava a caminho, mas fui abduzido por alienígenas que amam churrasco."  

## 🛠️ Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/gerador-desculpas.git
cd gerador-desculpas
```

## Crie um ambiente virtual e instale as dependências:
```bash
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Inicie o Servidor:
```bash
flask run
```

## 📦 Estrutura do Projeto
```
gerador-desculpas/
├── app/
    ├── services/
        ├── db.py
    ├── templates/
        ├── index.html
        └── excuse.html
    ├── __init__.py
    ├── routes.py
├── config.py
├── run.py
├── .gitignore
├── Procfile
├── requirements.txt
└── README.md
```

## 🔮 MVP e Roadmap
### ✅ Versão Atual
Formulário básico e geração de desculpas

## 🛣️ Planejamento Futuro
- Cadastro de usuários

- Histórico de desculpas geradas

- Sistema de créditos e plano premium

- Customização do estilo da desculpa (formal, absurda, criativa...)

## 🤝 Agradecimentos

Projeto desenvolvido como parte do estudo de Flask e MVPs com foco em produto digital.
Em serviço do humor — e de todas as situações em que só uma boa desculpa poderia salvar o dia.
