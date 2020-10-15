from accessToken import access_token, expires_on
import time
from subprocess import call

# converting current time from seconds since epoch to milliseconds since epoch
current_time = int(time.time() * 1000)

if current_time > int(expires_on):
    print("-----generating new tokens-------")
    call(["python", "oAuth.py"])

token = access_token
#print(token)