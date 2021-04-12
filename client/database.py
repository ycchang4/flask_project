import mysql.connector
from mysql.connector.constants import ClientFlag
from flask import Flask, render_template, request, redirect


config = {
    'user': 'root',
    'password': '0000',
    'host': '35.224.184.136',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': './ssl/server-ca.pem',
    'ssl_cert': './ssl/client-cert.pem',
    'ssl_key': './ssl/client-key.pem',
    'database': 'gpa'
}
def addCoourse(YearTerm: str, Subject: str, CRN:int, CourseCode: str, CourseTitle:str,Instructor:str, AverageGPA:float) :
    cnxn = mysql.connector.connect(**config)
    cursor = cnxn.cursor() 

    add_course = ("INSERT INTO avgGPA "
                  "(YearTerm, Subject, CRN, CourseCode, CourseTitle, Instructor, AverageGPA) "
                  "VALUES(%s, %s, %s, %s, %s, %s, %s)")
    data = (YearTerm, Subject, CRN, CourseCode, CourseTitle, Instructor, AverageGPA)
    cursor.execute(add_course, data)

    cnxn.commit()

    cursor.close()
    cnxn.close()


def getCourse():
    cnxn = mysql.connector.connect(**config)
    cursor = cnxn.cursor()
    query = ("SELECT CourseCode, AverageGPA, Instructor FROM avgGPA ORDER BY AverageGPA DESC LIMIT 10")
    cursor.execute(query)

    course = []
    for result in cursor:
        item = {
            "CourseCode" : result[0],
            "AverageGPA": result[1],
            "Instructor": result[2]
        }
        course.append(item)

    return course

def updateCourse(YearTerm: str, Subject: str, CRN: int, CourseTitle:str,Instructor:str, AverageGPA:float, code:str):
    cnxn = mysql.connector.connect(**config)
    cursor = cnxn.cursor()

    query = 'UPDATE avgGPA SET YearTerm = %s, Subject=%s, CRN=%s, CourseTitle=%s, Instructor=%s, AverageGPA=%s WHERE CourseCode = %s;'
    data = (YearTerm, Subject, CRN, CourseTitle, Instructor, AverageGPA, code)

    cursor.execute(query, data)

    cnxn.commit()

    cursor.close()
    cnxn.close()

def __addComments__(c_title: str, c_content: str, c_author: str) :
    cnxn = mysql.connector.connect(**config)
    cursor = cnxn.cursor() 

    add_comment = ("INSERT INTO comments "
                  "(title, author, content) "
                  "VALUES(%s, %s, %s)")
    data = (c_title, c_author, c_content)
    cursor.execute(add_comment, data)
    id = cursor.lastrowid

    cnxn.commit()

    cursor.close()
    cnxn.close()


def getComments():
    cnxn = mysql.connector.connect(**config)
    cursor = cnxn.cursor()
    query = ("SELECT * FROM comments")
    cursor.execute(query)

    user_comments = []
    for result in cursor:
        item = {
            "id" : result[0],
            "author": result[1],
            "title": result[2],
            "content": result[3]
        }
        user_comments.append(item)

    return user_comments

    cursor.close()
    cnxn.close()

def deleteComment(c_id: int) :
    cnxn = mysql.connector.connect(**config)
    cursor = cnxn.cursor()

    query = 'Delete From comments where id={};'.format(c_id)
    cursor.execute(query)
    cnxn.commit()
    cursor.close()
    cnxn.close()

def getHighestGPA() : 
    cnxn = mysql.connector.connect(**config)
    cursor = cnxn.cursor()
    query = ("SELECT Instructor, CourseCode, avgGPA FROM avgGPA NATURAL JOIN (SELECT avg(AverageGPA) AS avgGPA, CourseCode FROM avgGPA GROUP BY CourseCode) AS info ORDER BY info.avgGPA DESC LIMIT 15;")
    cursor.execute(query)

    courses = []
    for result in cursor:
        item = {
            "Instructor" : result[0],
            "CourseCode": result[1],
            "avgGPA": result[2],
        }
        courses.append(item)

    return courses

    cursor.close()
    cnxn.close()

def userSearch(crn: int) :
    cnxn = mysql.connector.connect(**config)
    cursor = cnxn.cursor()
    query = 'SELECT Instructor, CourseCode, AverageGPA FROM avgGPA WHERE CRN = {} ORDER BY AverageGPA DESC'.format(crn)


    cursor.execute(query)
   

    courses = []
    for result in cursor:
        item = {
            "Instructor" : result[0],
            "CourseCode": result[1],
            "avg_gpa": result[2]
        }
        courses.append(item)

    return courses

    cursor.close()
    cnxn.close()

def deleteCourse(code: str) :
    cnxn = mysql.connector.connect(**config)
    cursor = cnxn.cursor()

    query = 'Delete From avgGPA where CourseCode="{}";'.format(code)
    cursor.execute(query)
    cnxn.commit()
    cursor.close()
    cnxn.close()
    
class databaseClient:
    def __init__(self):
        self.cnxn = mysql.connector.connect(**config)
        self.cursor = cnxn.cursor()
        print('connection succeed')

    def queryData(self):
        query = ("SELECT * FROM avgGPA LIMIT 10")
        self.cursor.execute(query)
        res = []
        for (item) in cursor:
            res.append(item)
            print(item)
        return res

    def closeClient(self):
        self.cursor.close()
        self.cnxn.close()