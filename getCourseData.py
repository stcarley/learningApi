import requests
import json
from getToken import access_token as token

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
    print("Here is the request URL" + url)
    print("Here is the request URL" + returnData.text)
    return json.loads(returnData.text)



courseData = APIcall(token, courseUrl(courseUrn))

print(json.dumps(courseData, indent=4, sort_keys=True))

output = json.dumps(courseData, indent=4, sort_keys=True)

# --- save a sample local file to work with ---
# f = open("jsonCourseOutput.json", "w")
# f.write(output)
# f.close()