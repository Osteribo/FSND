# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

REVIEW_COMMENT
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
GET '/categories'
GET ...
POST ...
DELETE ...

GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}

```
GET /questions
- fetches a dictionary of question from the database by id with category, answer and rating 
- has no request arguments
- Returns: an object with all the questions and their associated information

Request:

{
    
}

Response:


{ "categories": { "1": "Science", "2": "Art", "3": "Geography", "4": "History", "5": "Entertainment", "6": "Sports" }, "questions": [ { "answer": "Tom Cruise", "category": 5, "difficulty": 4, "id": 4, "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?" }, { "answer": "Maya Angelou", "category": 4, "difficulty": 2, "id": 5, "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?" }, { "answer": "Edward Scissorhands", "category": 5, "difficulty": 3, "id": 6, "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?" }, { "answer": "Muhammad Ali", "category": 4, "difficulty": 1, "id": 9, "question": "What boxer's original name is Cassius Clay?" }, { "answer": "Brazil", "category": 6, "difficulty": 3, "id": 10, "question": "Which is the only team to play in every soccer World Cup tournament?" }, { "answer": "Uruguay", "category": 6, "difficulty": 4, "id": 11, "question": "Which country won the first ever soccer World Cup in 1930?" }, { "answer": "George Washington Carver", "category": 4, "difficulty": 2, "id": 12, "question": "Who invented Peanut Butter?" }, { "answer": "Lake Victoria", "category": 3, "difficulty": 2, "id": 13, "question": "What is the largest lake in Africa?" }, { "answer": "The Palace of Versailles", "category": 3, "difficulty": 3, "id": 14, "question": "In which royal palace would you find the Hall of Mirrors?" }, { "answer": "Escher", "category": 2, "difficulty": 1, "id": 16, "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?" } ], "success": true, "total_questions": 48 }

DELETE /questions/<int:questions_id>
- fetches a question from the database with
- Request: needs the id of the question that will be pulled from the database
- Returns: this returns an object with information from the question 
Request:

http://127.0.0.1:5000/questions/5

Return:

{
    {
  "deleted": 5, 
  "questions": [
    {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }, 
    {
      "answer": "Escher", 
      "category": 2, 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }, 
    {
      "answer": "Mona Lisa", 
      "category": 2, 
      "difficulty": 3, 
      "id": 17, 
      "question": "La Giaconda is better known as what?"
    }, 
    {
      "answer": "One", 
      "category": 2, 
      "difficulty": 4, 
      "id": 18, 
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }
  ], 
  "success": true
}

}

POST /questions 
- Inserts a new question into the database
- Request: a string for question and answer. integer for difficulty. category with string
    {
        question=new_question,
        answer=new_answer,
        category=new_category,
        difficulty=new_difficulty
    }
- Returns: pagination of the questions. 
    {
        'success': True,
        'created': 1,
        'question_created': current_questions,
        'total_questions': len(Question.query.all()
    }

POST /search 
- Searches questions in database for the input string
- Request: input as string into the search bar

{
	"searchTerm": 1
}
- Returns: the questions with the search string
{
  "currentCategory": [
    5,
    6
  ],
  "questions": [
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }
  ],
  "success": true,
  "total_questions": 2
}


GET /categories/<int:category_id>/questions
- gets all the questions in a specific category
- Requests: input or click on category id

http://127.0.0.1:5000/categories/2/questions


- Returns: The questions associated with the category and paginates them
{
  "current_category": [
    2,
    2,
    2,
    2
  ],
  "questions": [
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "One",
      "category": 2,
      "difficulty": 4,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    },
    {
      "answer": "Jackson Pollock",
      "category": 2,
      "difficulty": 2,
      "id": 19,
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }
  ],
  "success": true,
  "total_questions": 4
}

POST /quizzes
- starts the quiz game by showing trivia questions
- Requests: takes in the previous questions and preferred quiz category

{
    "previous_questions": [5, 9],
    "quiz_category": {"type": "History", "id": "4"}
}
- Returns: Randomize questions to answer

{
  "question": {
    "answer": "George Washington Carver",
    "category": 4,
    "difficulty": 2,
    "id": 12,
    "question": "Who invented Peanut Butter?"
  },
  "success": true
}
## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```