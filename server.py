# import imp
from flask import Flask, jsonify,request
import firebase_admin
from firebase_admin import credentials,auth
from firebase_admin import db
import pyrebase
import json
from Routes.user_routes import userRoutes
from Routes.que_Route import que_Routes
from Untitled14 import UniRoute
# import route
import array


app = Flask(__name__)
app.register_blueprint(userRoutes,url_prefix=("/user"))
app.register_blueprint(que_Routes)
app.register_blueprint(UniRoute)
cred = credentials.Certificate('career-counciling-firebase-adminsdk-vckja-502a244017.json')
firebase_admin.initialize_app(cred, {'databaseURL':"https://career-counciling-default-rtdb.firebaseio.com/"})
pb = pyrebase.initialize_app(json.load(open('fbconfig.json')))

ref = db.reference('name')
# print(ref.get())
users = [{'uid': 1, 'name': 'Noah Schairer'}]





      
if __name__ == "__main__":
  app.run(host="0.0.0.0" ,debug=True)














