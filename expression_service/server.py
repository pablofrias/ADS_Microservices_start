#!flask/bin/python
from flask import Flask, jsonify
import re
import requests
import os

app = Flask(__name__)

@app.route('/expression/api/v1.0/sentiment/<string:exp>', methods=['GET'])
def getSentimentValue(exp):
    if len(exp) == 0: abort(404)
    words = re.split(" ", exp)
    sentiment = 0
    url = 'http://localhost:5000/dictionary/api/v1.0/words/'
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

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Expression cannot be empty'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
