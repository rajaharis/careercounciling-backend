from flask import Blueprint, jsonify ,request
import json


que_Routes=Blueprint("routes ",__name__)

f= open('questions.json')

data = json.load(f)
my_list = []
str1 = "" 
f.close()
for i in data['data']:
    my_list.append(i)
    

@que_Routes.route("/questions")
def get_que():
    return jsonify(my_list)


