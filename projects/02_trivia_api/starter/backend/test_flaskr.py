import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_category_true(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])
    
    def test_get_category_fail(self):
        res = self.client().get('/categories/1000', )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')
    
    def test_questions_true(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['questions'])

    def test_questions_fail(self):
        res = self.client().get('/questions?page=1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_question_delete_true(self):
        dummy_question = Question(question= 'dummy question', answer = 'dum dumn', difficulty = 4, category = 1)

        dummy_question.insert()
        question_id = dummy_question.id        
        
        res = self.client().delete(f'/questions/{question_id}')
        data = json.loads(res.data)
        
        no_dummy_question = Question.query.filter(Question.id == dummy_question.id).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], question_id)
        self.assertFalse(no_dummy_question)

    def test_question_delete_false(self):
        dummy_question = Question(question= 'dummy question', answer = 'dum dumn', difficulty = 4, category = 1)

        dummy_question.insert()
        question_id = dummy_question.id        
        
        res = self.client().delete(f'/questions/{1}')
        data = json.loads(res.data)
        
        no_dummy_question = Question.query.filter(Question.id == dummy_question.id).one_or_none()
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False )
        self.assertEqual(data['message'], 'failed to proccess')

    def test_add_question(self):
        dummy_question = {
            'question': 'dummy question', 
            'answer': 'dum dumn', 
            'difficulty': 4, 
            'category': 1
            }

        before_post_questions = len(Question.query.all())
        res = self.client().post('/questions', json=dummy_question)
        data = json.loads(res.data)
        after_post_questions = len(Question.query.all())

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(before_post_questions < after_post_questions)

    def test_add_question_fail(self):
            #tries to add a question missing information
        dummy_question = {
            
            }

        res = self.client().post('/questions', json=dummy_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False )
        self.assertEqual(data['message'], 'failed to proccess')
        

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()