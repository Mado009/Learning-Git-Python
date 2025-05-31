#pip install flask sqlalchemy flask-migrate pymysql
from cgitb import handler

from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS  # Import CORS for handling cross-origin requests
import logging
# pip install flask sqlalchemy flask-migrate pymysql

app = Flask(__name__)
CORS(app)  # Enable CORS for the Flask app
app.config['SQLALCHEMY_DATABASE_URI'] \
    = 'mysql+pymysql://root:root@localhost:3308/schoolmanagement'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)  # Create a SQLAlchemy instance
migrate = Migrate(app, db)  # Initialize Flask-Migrate with the app and db

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[
                    logging.FileHandler('app.log'),
                    logging.StreamHandler()
                    ])
logger = logging.getLogger(__name__)




class Student(db.Model):
    __tablename__ = 'students'  # Optional: custom table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    courses = db.relationship('Course', backref='courses', lazy=True)

class Course(db.Model):
    __tablename__ = 'courses'  # Optional: custom table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    courses_id = db.Column(db.Integer,
                            db.ForeignKey('courses.id'), nullable=False)




#flask db init
#flask db migrate -m "Initial migration."
#flask db upgrade



@app.route('/api/students', methods=['GET'])
def get_students():
    try:
        students = Student.query.all()
        return jsonify([{'id': student.id, 'name': student.name} for student in students])
    except Exception as e:
        logger.error(f"Error fetching students: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/students', methods=['POST'])
def add_student():
    try:
        data = request.json
        new_student = Student(name=data['name'])
        db.session.add(new_student)
        db.session.commit()
        return jsonify({'id': new_student.id, 'name': new_student.name}), 201
    except Exception as e:
        logger.error(f"Error adding student: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    try:
        data = request.json
        student = Student.query.get_or_404(student_id)
        student.name = data['name']
        db.session.commit()
        return jsonify({'id': student.id, 'name': student.name})
    except Exception as e:
        logger.error(f"Error updating student: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    try:
        student = Student.query.get_or_404(student_id)
        db.session.delete(student)
        db.session.commit()
        return jsonify({'message': 'Student deleted successfully'})
    except Exception as e:
        logger.error(f"Error deleting student: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/courses', methods=['GET'])
def get_courses():
    try:
        courses = Course.query.all()
        return jsonify([{'id': course.id, 'name': course.name, 'year': course.year} for course in courses])
    except Exception as e:
        logger.error(f"Error fetching courses: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/courses', methods=['POST'])
def add_course():
    try:
        data = request.json
        new_course = Course(name=data['name'], year=data['year'])
        db.session.add(new_course)
        db.session.commit()
        return jsonify({'id': new_course.id, 'name': new_course.name, 'year': new_course.year}), 201
    except Exception as e:
        logger.error(f"Error adding course: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    try:
        data = request.json
        course = Course.query.get_or_404(course_id)
        course.name = data['name']
        course.year = data['year']
        db.session.commit()
        return jsonify({'id': course.id, 'name': course.name, 'year': course.year})
    except Exception as e:
        logger.error(f"Error updating course: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    try:
        course = Course.query.get_or_404(course_id)
        db.session.delete(course)
        db.session.commit()
        return jsonify({'message': 'Course deleted successfully'})
    except Exception as e:
        logger.error(f"Error deleting course: {e}")
        return jsonify({'error': str(e)}), 500









if __name__ == '__main__':
    app.run()


#Testign changes
