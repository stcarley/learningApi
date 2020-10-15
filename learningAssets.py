from getToken import access_token
import requests

bearerToken = "Bearer "+access_token
url = "https://api.linkedin.com/v2/learningAssets"
querystring = {"q":"criteria","assetFilteringCriteria.assetTypes[0]":"COURSE","assetFilteringCriteria.licensedOnly":"true","count":"100"}
headers = {
    'Authorization': bearerToken,
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Host': "api.linkedin.com",
    'cache-control': "no-cache"
}
response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)