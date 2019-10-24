from oAuth import token
import requests

bearerToken = "Bearer "+token
url = "https://api.linkedin.com/v2/learningActivityReports"
querystring = {"q":"criteria","count":"1","startedAt":"1562699900247","timeOffset.unit":"DAY","timeOffset.duration":"7","aggregationCriteria.primary":"ACCOUNT"}
headers = {
    'Authorization': bearerToken,
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Host': "api.linkedin.com",
    'cache-control': "no-cache"
}
response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)