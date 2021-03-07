import requests

r = requests.get("http://api.lib.sfu.ca/")
print(r.content)