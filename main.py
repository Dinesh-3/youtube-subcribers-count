import urllib.request
import json

channel_name = input("Enter Youtube channel name: ")
key = "Enter your api key"

url = "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+name+"&key="+key

data = urllib.request.urlopen(url).read()
subcount = json.loads(data)["items"][0]["statistics"]["subscriberCount"]

print(f"{channel_name} subcribers count is : {sub_count}")
