from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pymysql
from yaml import load, Loader
import os
import sqlalchemy
from client import database as dbClient


app = Flask(__name__)



# app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index.html")

@app.route('/post', methods=['GET', 'POST']) 
def getPost():

    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']
        dbClient.__addComments__(post_title, post_content, post_author)
        return redirect('/post')
    else:
        all_post = dbClient.getComments()
        return render_template('post.html', posts = all_post)

@app.route('/courses', methods=['GET', 'POST'])
def getCourse():

    if request.method == 'POST':
        year_term = request.form['yearTerm']
        subject = request.form['subject']
        CRN = request.form['crn']
        course_code = request.form['courseCode']
        course_title = request.form['CourseTitle']
        instructor = request.form['Instructor']
        avg_gpa = request.form['AverageGPA']


        dbClient.addCoourse(year_term, subject, CRN, course_code, course_title, instructor, avg_gpa)
        return redirect('/courses')
    else:
        all_course = dbClient.getCourse()
        return render_template('courses.html', courses = all_course)



@app.route('/courses/edit/<code>', methods=['GET', 'POST']) 
def updateCourse(code):
    if request.method == 'POST':
        year_term = request.form['yearTerm']
        subject = request.form['subject']
        CRN = request.form['crn']
        # course_code = request.form['courseCode']
        course_title = request.form['CourseTitle']
        instructor = request.form['Instructor']
        avg_gpa = request.form['AverageGPA']
        dbClient.updateCourse(year_term, subject, CRN, course_title, instructor, avg_gpa, code)
        return redirect('/courses')
    else:
        return render_template('updateCourse.html', code = code)



@app.route('/post/delete/<int:c_id>', methods=['GET', 'POST'])
def deleteComment(c_id) :

    try:
        dbClient.deleteComment(c_id)
        result = {'success': True, 'response': 'Removed comment'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
        return "Something went wrong"

    return redirect('/post')

@app.route('/searchTop15', methods=['GET', 'POST'])
def getHighestGPA():
    top_classes = dbClient.getHighestGPA()
    return render_template('search.html', topClasses = top_classes)

@app.route('/search', methods=['GET', 'POST'])
def user_search():
    if request.method == 'POST':
        input = request.form['crn']
        res = dbClient.userSearch(input) 
        return render_template('result.html', r = res)
        # return "test1"
    else :
        return render_template('user_search.html')

@app.route('/courses/delete/<code>', methods=['GET', 'POST'])
def deleteCourse(code) :
    try:
        dbClient.deleteCourse(code)
        result = {'success': True, 'response': 'Removed Course'}
        return redirect('/courses')
    except:
        result = {'success': False, 'response': 'Something went wrong'}
        return "Something went wrong"

    return redirect('/courses')


if __name__ == "__main__":
    app.run(debug=True)

