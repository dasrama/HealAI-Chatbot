import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv(".env")

    def get(self, ENV_VAR):
        return os.getenv(ENV_VAR)
    
config = Config()

    
        

