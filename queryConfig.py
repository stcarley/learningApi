from getToken import token
import requests
import json

# See documentation for addtional details about query parameters
# https://docs.microsoft.com/en-us/linkedin/learning/reference/learningactivityreports

primaryAggregation = "INDIVIDUAL"
secondaryAggregation = "CONTENT"


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
assetType = "COURSE"


bearerToken = "Bearer "+token

headers = {
    'Authorization': bearerToken,
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Host': "api.linkedin.com",
    'cache-control': "no-cache"
}

url = "https://api.linkedin.com/v2/learningActivityReports"