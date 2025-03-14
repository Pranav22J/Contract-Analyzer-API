from flask_restful import abort, reqparse, Resource
from auth.api_key import test_key, generate_and_add_key, validate_key, API_Keys, validate_user_id
from auth.rate_limiter import increment_request_number, check_daily_limit

generate_api_key_post_args = reqparse.RequestParser()
generate_api_key_post_args.add_argument("email", type = 'str', help = 'Enter your email address', required=True)

class contract_analyzer(Resource):
    """Analyzing PDF Resource"""
    @test_key
    @increment_request_number
    @check_daily_limit
    def put(self, text):
        # input put request logic
        return{}
    
class generate_api_key(Resource):
    """Resource for generating an API key """
    def post(self, email):
        args = generate_api_key_post_args.parse_args()
        user_id = args['email']

        if not validate_user_id(user_id):
            key = generate_and_add_key(user_id)
        else:
            abort(409, message = 'This email already exists, please use the API key given earlier')

        return {"API Key": key, "message": "Succesfully added user to database, please store your API key securely"}
    



