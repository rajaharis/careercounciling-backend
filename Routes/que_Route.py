from crypt import methods
from flask import Blueprint, jsonify ,request
import json

from matplotlib.pyplot import get
from requests import post


que_Routes=Blueprint("routes ",__name__)

f= open('questions.json')

data = json.load(f)
my_list = [] 
f.close()
# for i in data[]:
    

@que_Routes.route("/questions",methods=['GET', 'POST'])
def get_que():
    # index = int(request.form['index'])
    # print(index)

    return jsonify(data)

    

