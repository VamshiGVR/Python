#using python to talk to external application[git]
import requests

response  = requests.get("https://abc.com") #get takes URL into it
print(response.text)

