#!flask/bin/python
from flask import Flask, jsonify, abort
from dictionary_reader import search
import sys
import logging
import platform

app = Flask(__name__)

@app.route('/dictionary/api/v1.0/words/<string:word>', methods=['GET'])
def getSentimentValue(word):
    logger = logging.getLogger('Dictionary Service')
    if len(word.strip()) == 0: abort(404)
    word_value = search(word)
    if word_value[0]["value"] == 'unknown':
        #send_to_unknown(word)
        word_value[0]["value"] = 0
    logger.info("DICTIONARY: word: " + word + " - hostname: " + platform.node())
    return jsonify(word_value)

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Word cannot be empty'}), 404

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    app.run(host= '0.0.0.0', debug=True)