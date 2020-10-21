from getToken import token
import requests
import json
import time
from learningReports import reports_url, report_import
from queryConfig import primaryAggregation, secondaryAggregation, contentSource, assetType, headers, url
from datetime import datetime



# ---- Define time range  day.month.year hours:minutes:seconds---- #
startDate = '04.12.2019 00:00:01'
endDate = '05.12.2019 00:00:01'

def date_to_millis(date):
    dateObj = datetime.strptime(date,
                            '%d.%m.%Y %H:%M:%S')
    millis = int(dateObj.timestamp() * 1000)
    return millis

startMillis = date_to_millis(startDate)
endMillis = date_to_millis(endDate)



# converting current time from seconds since epoch to milliseconds since epoch
# currentTime = int(time.time() * 1000)
# startedAt is milliseconds since epoch, adjusted based upon the offset duration
# startedAt = currentTime - (86400000 * offsetDuration)       # 86400000 is number of milliseconds in a day

numberOfResults = 20
offsetUnit = "DAY"
offsetDuration = 1     # maximum offset is 14 days, larger calls will return 500 error

startedAt = startMillis

while startedAt < endMillis:
    report_import(url, headers, reports_url(numberOfResults, startedAt, offsetUnit, offsetDuration, primaryAggregation, secondaryAggregation, contentSource, assetType))
    startedAt = startedAt + 86400000 # 86400000 is number of milliseconds in a day
    print(time.asctime(time.localtime(startedAt/1000)), " complete")