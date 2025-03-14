import os
from dotenv import load_dotenv

load_dotenv

class Config:
    """This class is to store the OpenAI API key and development testing key in a secure manner"""
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    TEST_KEY = os.getenv('TEST_KEY')