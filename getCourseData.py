import requests
import json
import sqlite3
from sqlite3 import Error
from getToken import access_token as token
from jsonActivityToSql import getCourseList, create_connection

#----------------------------
# API Call
# Input - accesstoken and url
# Output - Return data in JSON
#----------------------------

courseUrn = 'urn:li:lyndaCourse:724791'

def courseUrl(courseUrn):
    courseUrl = 'https://api.linkedin.com/v2/learningAssets/{URN}'.format(URN = courseUrn)
    print(courseUrl)
    return courseUrl


def APIcall(token, url):

    # Make POST Headers
    headers = {
        "Authorization":"Bearer "+token
    }

    returnData = requests.get(url, headers=headers)
    # print("Here is the request URL" + url)
    # print("Here is the request URL" + returnData.text)
    return json.loads(returnData.text)

def add_course_details(connection, courseUrn, courseName, duration, published, updated, locale):
    sql_insert_course_details = """ INSERT OR REPLACE INTO courses (
                                    courseUrn,
                                    courseName,
                                    duration,
                                    published,
                                    updated,
                                    locale
                                    )
                                VALUES (
                                    '{courseUrn}',
                                    '{courseName}',
                                    '{duration}',
                                    '{published}',
                                    '{updated}',
                                    '{locale}'
                                ) ; """.format(courseUrn=courseUrn, courseName=courseName, duration=duration, published=published, updated=updated, locale=locale)
    print(sql_insert_course_details)
    try: 
        c = connection.cursor()
        c.execute(sql_insert_course_details)
        connection.commit()
    except Error as e:
        print(e)

def process_course_details(connection, data):
    courseUrn = data['urn'],
    courseName = data['title']['value'],
    duration = data['details']['timeToComplete']['duration'],
    published = data['details']['publishedAt'],
    updated = data['details']['lastUpdatedAt'],
    locale = data['details']['shortDescription']['locale']['language']
    if connection is not None:
        add_course_details(connection, courseUrn[0], courseName[0], duration[0], published[0], updated[0], locale)
    else:
        print("Error! no connection")    

def update_course_details():
    database = 'data.db'
    connection = create_connection(database)
    if connection is not None:
        courseUrns = getCourseList(connection)
        for row in courseUrns:
            data = APIcall(token, courseUrl(row[0]))
            process_course_details(connection, data)
    else:
        print("Error! cannot create the database connection.")

update_course_details()

# courseData = APIcall(token, courseUrl(courseUrn))

# print(json.dumps(courseData, indent=4, sort_keys=True))

# output = json.dumps(courseData, indent=4, sort_keys=True)

# --- save a sample local file to work with ---
# f = open("jsonCourseOutput.json", "w")
# f.write(output)
# f.close()