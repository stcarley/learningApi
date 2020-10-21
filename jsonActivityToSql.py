import json
import sqlite3
from sqlite3 import Error


with open ("jsonReportsOutput.json", "r") as readFile:
    data = json.load(readFile)



def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)

    return connection

def add_users(connection, profileUrn, name, email, uniqueUserId):
    sql_insert_user_data = """ INSERT OR REPLACE INTO users (
                                    profileUrn,
                                    name,
                                    email,
                                    uniqueUserId)
                                VALUES (
                                    '{profileUrn}',
                                    '{name}',
                                    '{email}',
                                    '{uniqueUserId}'
                                ); """.format(profileUrn=profileUrn, name=name, email=email, uniqueUserId=uniqueUserId)
    try: 
        c = connection.cursor()
        c.execute(sql_insert_user_data)
        connection.commit()
        # print("user {} added".format(profileUrn))
    except Error as e:
        print(e)


def add_courses(connection, courseUrn, courseName):
    sql_insert_course_data = """ INSERT OR REPLACE INTO courses (
                                    courseUrn,
                                    courseName
                                    )
                                VALUES (
                                    '{courseUrn}',
                                    '{courseName}'
                                ); """.format(courseUrn=courseUrn, courseName=courseName)
    try: 
        c = connection.cursor()
        c.execute(sql_insert_course_data)
        connection.commit()
        # print("course {} added".format(courseUrn))
    except Error as e:
        print(e)

def add_userCourses(connection, profileUrn, courseUrn, firstEngaged, lastEngaged, secondsViewed, progressPercentage):
    userCourse = profileUrn + '-' + courseUrn
    # print(userCourse)
    sql_insert_userCourse_data = """ INSERT OR REPLACE INTO userCourses (
                                    userCourse,
                                    courseUrn,
                                    profileUrn,
                                    firstEngaged,
                                    lastEngaged,
                                    secondsViewed,
                                    progressPercentage
                                    )
                                VALUES (
                                    '{userCourse}',
                                    '{courseUrn}',
                                    '{profileUrn}',
                                    '{firstEngaged}',
                                    '{lastEngaged}',
                                    '{secondsViewed}',
                                    '{progressPercentage}'
                                ); """.format(userCourse=userCourse, courseUrn=courseUrn, profileUrn=profileUrn, firstEngaged=firstEngaged, lastEngaged=lastEngaged, secondsViewed=secondsViewed, progressPercentage=progressPercentage)
    # print(sql_insert_userCourse_data)
    try: 
        c = connection.cursor()
        c.execute(sql_insert_userCourse_data)
        connection.commit()
        # print("userCourse {} added".format(userCourse))
    except Error as e:
        print(e)

def get_course_list(connection):
    sql_get_courses = """ SELECT courseUrn FROM courses WHERE duration IS NULL; """
    try: 
        c = connection.cursor()
        c.execute(sql_get_courses)
        courseUrns = c.fetchall()
        return courseUrns
    except Error as e:
        print(e)


def process_json(connection, data):
    for element in data['elements']:
        email = element['learnerDetails']['email']
        uniqueUserId = element['learnerDetails']['uniqueUserId']
        name = element['learnerDetails']['name']
        profileUrn = element['learnerDetails']['entity']['profileUrn']
        progressPercentage = element['activities'][1]['engagementValue']
        secondsViewed = element['activities'][0]['engagementValue']
        firstEngaged = element['activities'][0]['firstEngagedAt']
        lastEngaged = element['activities'][1]['lastEngagedAt']
        courseUrn = element['contentDetails']['contentUrn']
        courseName = element['contentDetails']['name']
        if connection is not None:
            add_users(connection, profileUrn, name, email, uniqueUserId)
            add_courses(connection, courseUrn, courseName)
            add_userCourses(connection, profileUrn, courseUrn, firstEngaged, lastEngaged, secondsViewed, progressPercentage)
        else:
            print("Error! no connection")
        



def main():
    database = 'data.db'
    connection = create_connection(database)
    if connection is not None:
        process_json(connection, data)

    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()

        