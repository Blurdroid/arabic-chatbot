
from flask import Flask, render_template, request, jsonify
import os,sys,requests, json
from random import randint
import psycopg2

#####################################################END OF LIBRARIES######################################################################################


app = Flask(__name__)

#html code
@app.route('/')
def home():
  return render_template('index.html')


@app.route('/parse',methods=['POST', 'GET'] )
def extract():
    text = str(request.form.get('value1'))
    payload = json.dumps({"sender": "Rasa", "message": text})
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    response = requests.request("POST", url="http://localhost:5005/webhooks/rest/webhook", headers=headers, data=payload)
    response = response.json()
    
    result = []
    for i in range(len(response)):
        try:
            result.append(response[i]['text'])
        except:
            continue
    
    return render_template('index.html', result=result, text=text)


if __name__ == "__main__":
  app.run(debug=True)
