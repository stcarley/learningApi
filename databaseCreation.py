import sqlite3
from sqlite3 import Error

# connection = sqlite3.connect('data.db')
# c = connection.cursor()

def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)

    return connection



def create_table(connection, create_table_sql):

    try:
        c = connection.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = 'data.db'

    # Table 1 --- users ---
    # PK: profileUrn
    # email, uniqueUserId, name

    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        profileUrn text PRIMARY KEY,
                                        name text,
                                        email text,
                                        uniqueUserId text
                                    ); """


    # Table 2 --- courses ---
    # PK: courseUrn
    # courseName

    sql_create_courses_table = """ CREATE TABLE IF NOT EXISTS courses (
                                        courseUrn text PRIMARY KEY,
                                        courseName text NOT NULL,
                                        duration int,
                                        published int,
                                        updated int,
                                        locale text
                                    ); """



    # Table 3 --- userCourses ---
    # PK: userCourse (concat courseUrn + profileUrn)
    # FK: courseUrn, profileUrn
    # first engaged at, last engaged at, seconds viewed, progress percentage

    sql_create_userCourses_table = """CREATE TABLE IF NOT EXISTS userCourses (
                                    userCourse text PRIMARY KEY,
                                    courseUrn text NOT NULL,
                                    profileUrn text NOT NULL,
                                    firstEngaged int,
                                    lastEngaged int,
                                    secondsViewed int,
                                    progressPercentage int,
                                    FOREIGN KEY (courseUrn) REFERENCES courses (courseUrn),
                                    FOREIGN KEY (profileUrn) REFERENCES users (profileUrn)
                                );"""

    connection = create_connection(database)


    if connection is not None:
        # create users table
        create_table(connection, sql_create_users_table)

        # create courses table
        create_table(connection, sql_create_courses_table)

        # create userCourses table
        create_table(connection, sql_create_userCourses_table)

    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()


