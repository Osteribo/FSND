from flask import Flask, request, jsonify, abort

from functools import wraps

app = Flask(__name__)

greetings = {
            'en': 'hello', 
            'es': 'Hola', 
            'ar': 'مرحبا',
            'ru': 'Привет',
            'fi': 'Hei',
            'he': 'שלום',
            'ja': 'こんにちは'
            }

@app.route('/greeting', methods=['GET'])
def greeting_all():
    return jsonify({'greetings': greetings})

@app.route('/greeting/<lang>', methods=['GET'])
def greeting_one(lang):
    print(lang)
    if(lang not in greetings):
        abort(404)
    return jsonify({'greeting': greetings[lang
    ]})

@app.route('/greeting', methods=['POST'])
def greeting_add():
    info = request.get_json()
    if('lang' not in info or 'greeting' not in info):
        abort(422)
    greetings[info['lang']] = info['greeting']
    return jsonify({'greetings':greetings})

'''
Identity and authentication walkthrough 

'''

def get_token_auth_header():
    if 'Authorization' not in request.headers:
        abort(401)


    auth_header = request.headers['Authorization']
    headers_parts = auth_header.split(' ')

    if len(headers_parts) != 2: # malformed header
        abort(401)

    if headers_parts[0].lower() != 'bearer': #ensure it is a bearer token
        abort(401)

        #return second part of header
    return headers_parts[1] 



    #decorator
def requires_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        jwt = get_token_auth_header()
        return f(jwt, *args, **kwargs)
    return wrapper

@app.route('/headers')
@requires_auth
def headers(jwt):

    

    print(jwt)
    return 'not implemented'

@app.route('/image')
@requires_auth
def images(jwt):
    print(jwt)
    return 'not implemented'