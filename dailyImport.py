from getToken import token
import requests
import json
import time
from learningReports import reports_url, report_import
from queryConfig import primaryAggregation, secondaryAggregation, contentSource, assetType, headers, url
from datetime import datetime



numberOfResults = 20
offsetUnit = "DAY"
offsetDuration = 1     # maximum offset is 14 days, larger calls will return 500 error

# converting current time from seconds since epoch to milliseconds since epoch
currentTime = int(time.time() * 1000)
# startedAt is milliseconds since epoch, adjusted based upon the offset duration
startedAt = currentTime - (86400000 * offsetDuration)       # 86400000 is number of milliseconds in a day



report_import(url, headers, reports_url(numberOfResults, startedAt, offsetUnit, offsetDuration, primaryAggregation, secondaryAggregation, contentSource, assetType))
print(time.asctime(time.localtime(startedAt/1000)), " complete")