from flask import Flask, jsonify, request, make_response
import jwt
from waitress import serve
from functools import wraps
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('API_SECRET_KEY')

# Authentication
# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         token = request.args.get('token') #http://127.0.0.1:5000/route?token=alshfjfjdklsfj89549834ur

#         if not token:
#             return jsonify({'message' : 'Token is missing!'})

#         try:
#             data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
#         except:
#             return jsonify({'message' : 'Token is invalid!'})

#         return f(*args, **kwargs)

#     return decorated


def greet(amount):

    URL = os.environ.get('URL')
    OAUTH_TOKEN = os.environ.get('OAUTH_TOKEN')

    url = URL
    oauth_token = OAUTH_TOKEN

    f = open("content.txt", "r")

    try:

        return jsonify({'message': f.read() + ' ' + str(amount)})
    except Exception as e:
        # print(('Error message: %s' % e.message))
        # print(('Error code: %s' % e.error_code))
        return jsonify({'message': 'Error'})


@app.route("/restAPI/<int:amount>")
# @token_required
def mainFunc(amount):

    b = greet(amount)
    if b:
        return b
    else:
        return jsonify({'message': 'returning none'})


@app.route('/')
def driver():

    return jsonify({'message': 'Working fine'})


if (__name__ == '__main__'):

    # app.run()
    serve(app, host="0.0.0.0", port=8080)  # Production
