# learningApi
LinkedIn Learning learningAssets and learningActivityReports APIs

Python code samples for Python 3.x, using Requests package and sqlite. 

Token creation requires credentials.py, which would be formatted as follows:
client_id = 'xxx'
client_secret = 'yyy'

For instructions on generating API keys see the following article:
https://www.linkedin.com/help/learning/answer/90058

To utilize the learningAssets endpoint you will need the API keys to have "content" permissions.
To utilize the learningActivityReports endpoint you will the API keys to have "reports" permissions. 

oAuth.py makes the authentication call and caches the authentication token and expiration in accessToken.py

getToken.py returns a valid token, or re-calls oAuth.py if token is expired


Using this repo to pull usage reporting information:
queryConfig.py specifies the type of data being retrieved (https://docs.microsoft.com/en-us/linkedin/learning/reference/learningactivityreports)

databaseCreation.py creates a local SQL (sqlite) database with the tables where this data will be stored in the following format:
users (user information)
courses (details about the courses)
userCourses (information about user's progress through the courses)

historicalImport.py iterates through API calls to return all data from the beginning date to the end date, storing it in the tables mentioned above.

dailyImport.py calls the previous 24 hours worth of usage data

getCourseData.py backfills additional details about the courses listed in the 'courses' table.  


Full API documentation can be found here:
https://docs.microsoft.com/en-us/linkedin/learning/overview/
