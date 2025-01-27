from dotenv import load_dotenv
import os

class Config:
    MONGO_URI = "mongodb://localhost:27017/silly"
 
    load_dotenv()

    OPEN_AI_KEY = os.getenv('OPEN_AI_KEY')