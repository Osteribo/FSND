from sqlalchemy import Integer, Column, String, create_engine, Date
from flask_sqlalchemy import SQLAlchemy
import json
import os

database_path= os.environ['DATABASE_URL']

# database_name = "fsdn"
# database_path = "postgres://{}:{}@{}/{}".format('alo', '1234', 'localhost:5432', database_name)

db = SQLAlchemy()


'''
setup_db(app)
    binds a flask application and SQLAlchemy service
'''

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"]= database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

'''
Donor

'''

class Donor(db.Model):
    __tablename__= "Donor"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date_of_birth = Column(Date)
    blood_type = Column(String)
    products = Column(String)
    num_products = Column(Integer)

'''
Product
#later implementation

class Product(db.Model):
    __tablename__="Product"

    id = Column(Integer, primary_key=True)
    cell_type = Column(String)
    date_of_processing = Column(Date)
    donor = 


'''

