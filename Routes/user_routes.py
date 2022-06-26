from flask import Blueprint ,request
from firebase_admin import credentials,auth
import json
import pyrebase



userRoutes=Blueprint("route ",__name__)
pb = pyrebase.initialize_app(json.load(open('fbconfig.json')))


def check_token(f):
    # @wraps(f)
    def wrap(*args,**kwargs):
        if not request.headers.get('authorization'):
            return {'message': 'No token provided'},400
        try:
            user = auth.verify_id_token(request.headers['authorization'])
            request.user = user
        except:
            return {'message':'Invalid token provided.'},400
        return f(*args, **kwargs)
    return wrap

@userRoutes.route('/api/signup')
def signup():
#     email = request.form.get('email')
#     password = request.form.get('password')
    email='danish@gmail.com'
    password='123123'

    if email is None or password is None:
        return {'message': 'Error missing email or password'},400
    try:
        user = auth.create_user(
               email=email,
               password=password
        )
       
        return {'message': f'Successfully created user '},200

    except:
        return {'message': 'Error creating user'},400
#Api route to get a new token for a valid user
@userRoutes.route('/api/signin')
def token():
    email='danish@gmail.com'
    password='123123'
    try:
        user = pb.auth().sign_in_with_email_and_password(email, password)
        jwt = user['idToken']
        return {'token': jwt}, 200
    except:
        return {'message': 'There was an error logging in'},400


@userRoutes.route('/api/userinfo')
@check_token
def userinfo():
    return {'data': "hahahah"}, 200
      