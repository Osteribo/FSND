import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink, db
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
'''
# db_drop_and_create_all()

## ROUTES
'''
@TODO implement endpoint
    GET /drinks
        it should be a public endpoint
        it should contain only the drink.short() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks')
def show_drinks():
    try:
        # drinks = {}
        # for drink in Drink.query.all():
        #     drinks[drinks.id] = drinks.short()
        drinks = Drink.query.all()
        return jsonify({
            'success': True,
            'drinks': [drink.short() for drink in drinks]
        })
    except:
        abort(400)

'''
@TODO implement endpoint
    GET /drinks-detail
        it should require the 'get:drinks-detail' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''

@app.route('/drinks-detail')
@requires_auth('get:drinks-detail')
def concoctions(token):
    try:
        drinks = Drink.query.all()
        return jsonify({
            'success': True,
            'drinks': [drink.long() for drink in drinks]
        })
    except:
        abort(404)


'''
@TODO implement endpoint
    POST /drinks
        it should create a new row in the drinks table
        it should require the 'post:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink
        or appropriate status code indicating reason for failure
'''

@app.route('/drinks', methods = ['POST'])
@requires_auth('post:drinks')
def new_drank(token):
    # drank_title = json.get_request('title')
    # drank_recipe = json.get_request('recipe')

    # new_drank = Drink(drank_title, drank_recipe)
    # new_drink = Drink(title = body['title'], recipe = """{}""".format(body['recipe']))
    # Drink.insert(new_drink)
    body = request.get_json()
    print(body)
    
    ## if no form data 
    if body == None:
        abort(404)
    new_recipe = body.get('recipe')
    print(new_recipe)
    new_title = body.get('title')
    print(new_title)
    try:
        new_drink = Drink(title=new_title, recipe=json.dumps(new_recipe))
        print(new_drink)
        new_drink.insert()
        new_drink = Drink.query.filter_by(id= new_drink.id).first()
        print(new_drink)
        return jsonify({
            'success': True,
            'drinks': new_drink.long()
        })
    except:
        abort(404)

'''
@TODO implement endpoint
    PATCH /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
        or appropriate status code indicating reason for failure
'''

@app.route('/drinks/<int:drink_id>', methods = ['PATCH'])
@requires_auth('patch:drinks')
def edit_drank(payload, drink_id):

        # grab information from front end in a simplified format
    body = request.get_json()

    title_edit = body.get('title')
    recipe_edit = body.get('recipe')
    drank_to_update = Drink.query.filter(Drink.id == drink_id).one_or_none()
    drank_to_update.title = title_edit
    drank_to_update.recipe = recipe_edit
    Drink.update()

    return jsonify({
        'success': True,
        'drinks': drink_to_update
    })
    


'''
@TODO implement endpoint
    DELETE /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
'''

@app.route('/drinks/<int:drink_id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_da_drink(payload, drink_id):
    try:
            
        drank_to_delete = Drink.query.filter(Drink.id == drink_id).one_or_none()
        drank_to_delete.delete()
        return jsonify({
            'success': True,
            'delete': drink_id
         })

    except:
        abort(404)

## Error Handling
'''
Example error handling for unprocessable entity
'''
@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
                    "success": False, 
                    "error": 422,
                    "message": "unprocessable"
                    }), 422

'''
@TODO implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with approprate messages):
             jsonify({
                    "success": False, 
                    "error": 404,
                    "message": "resource not found"
                    }), 404

'''


'''
@TODO implement error handler for 404
    error handler should conform to general task above 
'''
@app.errorhandler(404)
def page_not_found(error):
    return jsonify({
                    "success": False, 
                    "error": 404,
                    "message": "Page not found"
                    }), 404



'''
@TODO implement error handler for AuthError
    error handler should conform to general task above 
'''
@app.errorhandler(AuthError)
def unprocessable(error):
    return jsonify({
                    "success": False, 
                    "error": AuthError,
                    "message": "Error with authorization"
                    }), AuthError

@app.errorhandler(401)
def page_not_found(error):
    return jsonify({
                    "success": False, 
                    "error": 401,
                    "message": "Unauthorized"
                    }), 401

@app.errorhandler(400)
def bad_request(error):
    return jsonify({
      "success": False,
      "error": 400,
      "message": "bad request"
      }), 400


