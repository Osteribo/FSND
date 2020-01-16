import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

'''
This function creates paginated questions.
Separated from the rest of the app to allow for reuse.
'''

def paginate_questions(request, selection):
  page = request.args.get('page', 1, type=int) #set page
  start = (page - 1) * QUESTIONS_PER_PAGE #index pages with # of questions 
  end = start + QUESTIONS_PER_PAGE
  questions = [question.format() for question in selection] 
  current_questions = questions[start:end]
  return current_questions

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

  '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''

  cors = CORS(app, resources={'/': {"origins": "*"}})


  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


  '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  @app.route('/categories',  methods = ['GET'])
  def get_catagories():

    try:
      categories = {}
      for category in Category.query.all():
        categories[category.id] = category.type
      return jsonify({
              'success':True,
              'categories': categories,
            
          })

    except:
      abort(404)

  '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
      '''

  @app.route('/questions', methods = ['GET'])
  def get_questions():
    selection = Question.query.order_by(Question.id).all()
    current_questions = paginate_questions(request, selection)
      
      #if no question are found abort 404
    if len(current_questions) == 0:
      abort(404)
      
      #create a dictionary to hold the categories and their values
    categories = {}
    for category in Category.query.all():
      categories[category.id] = category.type
    return jsonify({
            'success':True,
            'questions': current_questions,
            'total_questions': len(current_questions),
            'categories': categories
        })

  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''

  @app.route('/questions/<int:question_id>', methods = ['DELETE'])
  def delete_question(question_id):
    try:
      question = Question.query.filter(Question.id == question_id).one_or_none()
      if question is None:
        abort(404)
      question.delete()

      selection = Question.query.order_by(Question.id).all()
      current_questions = paginate_questions(request, selection)

      return jsonify({
        'success': True,
        'deleted': question_id,
        'questions': current_questions,
        

      })

    except:
      abort(422)



  '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''
  
  @app.route('/questions', methods= ['POST'])
  def new_question():
    body = request.get_json()

    if not ('question' in body and 'answer' in body and 'difficulty' in body and 'category' in body):
      abort(422)

    new_question = body.get('question', None)
    new_answer = body.get('answer', None )
    new_category = body.get('category', None)
    new_difficulty = body.get('difficulty', None)

    if (new_question == None or new_answer == None or new_category == None or new_difficulty==None):
      abort(422) 

    try:
       
      question = Question(question = new_question, answer = new_answer, category = new_category, difficulty = new_difficulty)
      question.insert()

    
      selection = Question.query.order_by(Question.id).all()
      current_questions = paginate_questions(request, selection)

      return jsonify({
        'success': True,
        'created': question.id,
        'question_created': current_questions,
        'total_questions': len(Question.query.all())
      })


    except:
      abort(422)


  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''
  
  @app.route('/search', methods=['POST'])
  def search_questions():
      
    body = request.get_json() #get infomation from webpage

    search = body.get('searchTerm', None) #assign input from searchTerm from webpage/user entry into variable 

    try: 
      search_return = Question.query.order_by(Question.id).filter(Question.question.ilike(f'%{search}%')).all()
      current_category = [question.category for question in search_return]
      print(search_return[0])
      if search_return is None:
        abort(400)
      if len(search_return) == 0:
        abort(406)

      current_questions = paginate_questions(request, search_return)
      return jsonify({
        'success': True,
        'questions': current_questions,
        'total_questions': len(search_return),
        'currentCategory': current_category 
          })
    except:
      abort(404)
  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''

  @app.route('/categories/<int:category_id>/questions', methods= ['GET'])
  def category_qs(category_id):
    try:
      questions = Question.query.order_by(Question.id).filter_by(category=category_id) 
      current_category = [question.category for question in questions]
      return jsonify({
        'success': True,
        'questions': [question.format() for question in questions.all()],
        'total_questions': len(questions.all()),
        'current_category': current_category
      })


    except:
      abort(404)


  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''

  @app.route('/quizzes', methods= ['POST'])
  def play():
        body = request.get_json()
        previous_questions = body.get('previous_questions', [])
        quiz_category = body.get('quiz_category', None)

        try:

          if quiz_category:
              if quiz_category['id'] == 0:
                  quiz_selections = Question.query.all()
              else:
                  quiz_selections = Question.query.filter_by(category=quiz_category['id']).all()

          filtered_options =  [question.format() for question in quiz_selections if question.id not in previous_questions]
          if len(filtered_options) == 0:
              abort(422)

          randomized_qs = random.choice(filtered_options)
          return jsonify({
              'success': True,
              'question': randomized_qs
          })
        except:
            abort(422)
  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404

  @app.errorhandler(422)
  def fail_processing(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "failed to proccess"
    }), 422

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "bad request"
    }), 400

  @app.errorhandler(500)
  def internal_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "internal server error"
    })
  return app

    
