#pip install flask sqlalchemy flask-migrate pymysql
from cgitb import handler

from flask import Flask, render_template, request, redirect, url_for, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_cors import CORS  # Import CORS for handling cross-origin requests
import logging
# pip install flask sqlalchemy flask-migrate pymysql

# app = Flask(__name__)
# CORS(app)  # Enable CORS for the Flask app
# app.config['SQLALCHEMY_DATABASE_URI'] \
#     = 'mysql+pymysql://root:root@localhost:3308/schoolmanagement'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy(app)  # Create a SQLAlchemy instance
# migrate = Migrate(app, db)  # Initialize Flask-Migrate with the app and db

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[
                    logging.FileHandler('app.log'),
                    logging.StreamHandler()
                    ])
logger = logging.getLogger(__name__)




# class Student(db.Model):
#     __tablename__ = 'students'  # Optional: custom table name
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     courses = db.relationship('Course', backref='courses', lazy=True)
#
# class Course(db.Model):
#     __tablename__ = 'courses'  # Optional: custom table name
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     year = db.Column(db.Integer, nullable=False)
#     courses_id = db.Column(db.Integer,
#                             db.ForeignKey('courses.id'), nullable=False)




#flask db init
#flask db migrate -m "Initial migration."
#flask db upgrade


if __name__ == '__main__':
    app.run()


#Testign changes
