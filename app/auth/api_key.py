import secrets
from flask import request
from flask_restful import abort
from rate_limiter import increment_request_number

API_Keys = {}

def generate_and_add_key(user_id): 
    """Generate an API key for a new user and add it to the list of other API Keys"""
    key = secrets.token_hex(16)
    API_Keys[key] = {'user_id': user_id, "requests_today":0}
    return key

def validate_key(key):
    """Validates API Key sent by user against the list of API Keys generated"""
    if key not in API_Keys:
        return False
    else:
        return True
    
def validate_user_id(user_id):
    result = True
    for key, val in API_Keys.items():
        if val['user_id'] == user_id:
            result = True
        else:
            result= False
    return result
        
        
def test_key(func):
    """Test the api key sent in by a user"""
    def wrapper(*args, **kwargs):
        user_api_key = request.headers.get('X-API-KEY') # Getting the API key from the headers section of the user request. 

        if not user_api_key:
            abort(401, message = "Missing API key, please send an API key with your request")

        if not validate_key(user_api_key):
            abort(401, message = 'Invalid API key, please send a valid API key with your request')

    return wrapper
    


