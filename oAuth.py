import requests
from credentials import client_id, client_secret
import json
import time



url = "https://www.linkedin.com/oauth/v2/accessToken"
querystring = {"grant_type":"client_credentials","client_id":client_id,"client_secret":client_secret}
payload = "<share>\n    <comment>Comment</comment>\n    <content>\n        <title>title"
headers = {'Content-Type': "text/plain", 'Cache-Control': "no-cache", 'Host': "www.linkedin.com", 'Accept-Encoding': "gzip, deflate", 'Connection': "keep-alive", 'cache-control': "no-cache"}
response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
response = json.loads(response.text)
token = response['access_token']

current_time = int(time.time() * 1000)
expiration = current_time + response['expires_in']

exp  = str(expiration)
# exp = "{:.0f}".format(expiration)
print ("exp:", exp)
print(response)

new_token = "access_token = %a \nexpires_on = '%s'" % (token, exp)
print("new expiration:", new_token)



f = open("accessToken.py", "w")
f.write(new_token)
f.close()