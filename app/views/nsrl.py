'''
API to take in requestes for lookups of hashes in the NSRL database
'''
import re
import app.models.nsrl as nsrl_model
from flask import Blueprint, jsonify, request

nsrl = Blueprint('nsrl', __name__)
regex = re.compile('[0-9a-fA-F]+$')

@nsrl.route('/query', methods=['POST'])
def post_query():
    hash = request.form['hash']

    if regex.match(hash):
        if len(hash) is 40:
            return nsrl_model.hash_lookup(hash, 'SHA-1')
        elif len(hash) is 32:
            return nsrl_model.hash_lookup(hash, 'MD5')
        else:
            return jsonify({'response_code': 2, 'message': 'Invalide hash providede', 'info': hash})
    else:
        return jsonify({'response_code': 2, 'message': 'Invalide hash providede', 'info': hash})
