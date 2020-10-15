from getToken import token
import requests
import json
import time
from jsonActivityToSql import create_connection, process_json



# converting current time from seconds since epoch to milliseconds since epoch
currentTime = int(time.time() * 1000)


# QUERY PARAMETERS #
numberOfResults = 3
offsetUnit = "DAY"
offsetDuration = 1     # maximum offset is 14 days, larger calls will return 500 error

# startedAt is milliseconds since epoch, adjusted based upon the offset duration
startedAt = currentTime - (86400000 * offsetDuration)       # 86400000 is number of milliseconds in a day

# filtering by group
#scopeFilterType = "enterpriseScopeFilters[0].groupUrn"
#scopeFilter = "urn:li:enterpriseGroup:(urn:li:enterpriseAccount:2108938,3157260)"

# filtering by profile ****NOT CURRENTLY SUPPORTED****
# scopeFilterType = "enterpriseScopeFilters[0].profileUrn"
# scopeFilter = "urn:li:enterpriseProfile:(urn:li:enterpriseAccount:2108938,60432694)"

# filtering by course ****NOT CURRENTLY SUPPORTED****
# scopeFilterType = "enterpriseScopeFilters[0].contentUrn"
# scopeFilter = "urn:li:lyndaCourse:563464"


contentSource = "EXTERNAL"



url = "https://api.linkedin.com/v2/learningActivityReports"

#learner activity detail report, sorted by completions
querystring = {"q":"criteria",
               "count":numberOfResults,
               "startedAt":startedAt,
               "timeOffset.unit":offsetUnit,
               "timeOffset.duration":offsetDuration,
               "aggregationCriteria.primary":"INDIVIDUAL",
               "aggregationCriteria.secondary":"CONTENT",
               #"sortBy.engagementMetricType":"COMPLETIONS",
               "locale.language":"en",
               #scopeFilterType:scopeFilter,
               "contentSource":contentSource,
               "assetType":"COURSE"
               }

# if using CONTENT aggregation criteria you must include assetType COURSE

bearerToken = "Bearer "+token

headers = {
    'Authorization': bearerToken,
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Host': "api.linkedin.com",
    'cache-control': "no-cache"
}


def reportImport(url, headers, querystring = ''):

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    #jsonResponse = json.loads(response.text)
    #data = json.dumps(jsonResponse, indent=4, sort_keys=True)
    database = 'data.db'
    connection = create_connection(database)
    if connection is not None:
        process_json(connection, data)
    else:
        print("Error! cannot create the database connection.")
    if data['paging']['links'][0]['rel'] == 'next':
        url = 'https://api.linkedin.com/' + data['paging']['links'][0]['href']
        print(url)
        reportImport(url, headers)
    
reportImport(url, headers, querystring)


# --- save a sample local file to work with ---
# f = open("jsonReportsOutput.json", "w")
# f.write(data)
# f.close()