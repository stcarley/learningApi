from oAuth import token
import requests
import json
import time

#converting current time from seconds since epoch to milliseconds since epoch
currentTime = int(time.time() * 1000)
print(currentTime)
offsetDuration = 14
#startedAt is milliseconds since epoch, adjusted based upon the offset duration
startedAt = currentTime - (86400000 * offsetDuration)

bearerToken = "Bearer "+token
url = "https://api.linkedin.com/v2/learningActivityReports"

#learner activity detail report
querystring = {"q":"criteria",
               "count":"100",
               "startedAt":startedAt,
               "timeOffset.unit":"DAY",
               "timeOffset.duration":offsetDuration,
               "aggregationCriteria.primary":"INDIVIDUAL",
               "aggregationCriteria.secondary":"CONTENT",
               "assetType":"COURSE"}
headers = {
    'Authorization': bearerToken,
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Host': "api.linkedin.com",
    'cache-control': "no-cache"
}
response = requests.request("GET", url, headers=headers, params=querystring)
jsonResponse = json.loads(response.text)
print(json.dumps(jsonResponse, indent=4, sort_keys=True))
#print(response.text)