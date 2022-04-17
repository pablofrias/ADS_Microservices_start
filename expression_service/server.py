#!flask/bin/python
from flask import Flask, jsonify
import re
import requests
import os
import consul

app = Flask(__name__)

def getDictionaryServiceIP():
    c = consul.Consul(host='172.17.0.2', port=8500)
    print(c.health.service('dictionary', passing=True))
    ip = c.health.service('dictionary', passing=True)[1][0]['Node']['Address']
    return ip

@app.route('/expression/api/v1.0/sentiment/<string:exp>', methods=['GET'])
def getSentimentValue(exp):
    if len(exp) == 0: abort(404)
    words = re.split(" ", exp)
    sentiment = 0
    ip_address = getDictionaryServiceIP()
    url = f'http://{ip_address}:5000/dictionary/api/v1.0/words/'
    print("URL de dictionary: " + url)
    
    for word in words:
        response = requests.get(url + word.strip())
        sentiment += response.json()[0]["value"]

    return jsonify([
                    {
                        'expression': exp.strip(),
                        'final_value': sentiment
                    }
                ])

@app.route('/expression/api/v1.0/health', methods=['GET'])
def getHealth():
    return "{\"method\":\"health\"}"

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Expression cannot be empty'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
