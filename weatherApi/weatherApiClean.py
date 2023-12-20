#This script calls the openweathermap.org current weather forecast API to get current weather data for Toronto

import requests
import datetime

#Building weatherUrl for get request
#city/id = 'Gananoque'/'5959326'
#city/id = 'Toronto'/'6167863'
id = '6167863'
apiKey = 'yourKey'
units = 'metric'
weatherUrl = 'http://api.openweathermap.org/data/2.5/weather?id='+id+'&APPID='+apiKey+'&units='+units+''

#Performing get request and saving in resp object
resp = requests.get(weatherUrl)
#Useful calls for accessing the 'resp' object below:
#resp.headers
#resp.text
#resp.status_code

#Loading resp as json object
respJson = resp.json()
#Userful calls for accessing the 'respJson' object below:
#respJson.keys()
#respJson['main']
#respJson['main']['temp']
#respJson['weather'][0]['description']

#Initializing a dictionary to store key:value pairs from respJson
weatherData = {}

#Populating dictionary with key:value pairs
weatherData['location'] = respJson['name']
weatherData['temp'] = str(respJson['main']['temp'])+' °C'
weatherData['humidity'] = str(respJson['main']['humidity'])+' %'
weatherData['windSpeed'] = str(respJson['wind']['speed'])+' meter/sec'
weatherData['pressure'] = str(respJson['main']['pressure'])+ ' hPa'
weatherData['condition'] = respJson['weather'][0]['description']
weatherData['sunrise'] = datetime.datetime.fromtimestamp(int(respJson['sys']['sunrise'])).strftime('%H:%M')
weatherData['sunset'] = datetime.datetime.fromtimestamp(int(respJson['sys']['sunset'])).strftime('%H:%M')
weatherData['daylightHours'] = round((respJson['sys']['sunset'] - respJson['sys']['sunrise'])/3600,2)

#Create a payload to post to slack, iterate over weatherData dictionary and append to the list textPayload
textPayload = ''
for k,v in weatherData.items():
    textPayload = textPayload + k + ': ' + str(v) + '\n'
    
#Build post request for slack
channel = "yourChannel"
userName = "yourName"
iconEmoji = "yourEmoji"
slackUrl = 'yourSlackURL'
#Populate payload with above variables
payload={"channel": channel, "username": userName, "text": textPayload,"icon_emoji": iconEmoji}
slackPost = requests.post(slackUrl, json = payload)



