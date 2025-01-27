from flask import Flask
from .routes import main
from .services.db import init_mongo

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    # app.config['OPEN_AI_KEY']  = OPEN_AI_KEY
    init_mongo(app)
    
    app.register_blueprint(main)

    return app