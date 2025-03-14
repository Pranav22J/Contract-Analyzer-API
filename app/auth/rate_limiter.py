from api_key import test_key, API_Keys
from config import Config
from flask_restful import abort

# Defining the daily request limit
DAILY_REQUEST_LIMIT = 20

def increment_request_number(user_api_key, func):
    def wrapper(*args, **kwargs):
        """Increment the requests by 1 for each request sent by an API Key"""
        API_Keys[user_api_key]['requests_today']+=1
    return wrapper


def check_daily_limit(user_api_key, func):
    def wrapper(*args, **kwargs):

        user_requests = API_Keys[user_api_key]['requests_today']
        requests_left = DAILY_REQUEST_LIMIT-user_requests

        if API_Keys[user_api_key]['requests_today'] > DAILY_REQUEST_LIMIT:
            abort(message = 'Daily API request limit reached, please wait 24 hours before sending another request')
        else:
            print(f"API limit valid, you have {requests_left} requests remaining for today")

        func()
    return wrapper