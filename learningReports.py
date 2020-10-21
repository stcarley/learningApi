from getToken import token
import requests
import json
import time
from jsonActivityToSql import create_connection, process_json



def reports_url(numberOfResults, startedAt, offsetUnit, offsetDuration, primaryAggregation, secondaryAggregation, contentSource, assetType):


    #learner activity detail report, sorted by completions
    querystring = {"q":"criteria",
                "count":numberOfResults,
                "startedAt":startedAt,
                "timeOffset.unit":offsetUnit,
                "timeOffset.duration":offsetDuration,
                "aggregationCriteria.primary":primaryAggregation,
                "aggregationCriteria.secondary":secondaryAggregation,
                "locale.language":"en",
                #scopeFilterType:scopeFilter,
                "contentSource":contentSource,
                "assetType":assetType
                }

    # if using CONTENT aggregation criteria you must include assetType COURSE

    return querystring



def report_import(url, headers, querystring = ''):

    response = requests.request("GET", url, headers=headers, params=querystring)
    print(url)
    data = json.loads(response.text)
    print(json.dumps(data, indent=4, sort_keys=True))
    database = 'data.db'
    connection = create_connection(database)
    if connection is not None:
        process_json(connection, data)
    else:
        print("Error! cannot create the database connection.")
    if not 'href' in data['paging']['links'][0] or len(data['paging']['links']) == 0:
        print("End of results for request")
    elif data['paging']['links'][0]['rel'] == 'next':
        url = 'https://api.linkedin.com/' + data['paging']['links'][0]['href']
        print("next batch", url)
        report_import(url, headers)


# report_import(url, headers, reports_url(numberOfResults, startedAt, offsetUnit, offsetDuration, primaryAggregation, secondaryAggregation, contentSource, assetType))

# report_import(url, headers, querystring)


# --- save a sample local file to work with ---
# f = open("jsonReportsOutput.json", "w")
# f.write(data)
# f.close()