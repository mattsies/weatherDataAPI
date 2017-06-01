# Current Weather Forecast

This script is a great introduction to using python to call APIs and push data to slack.

This script is organized into two parts:
1. *openweathermap.org API request* pulls current weather data for a city, parses into a json file and stores specific fields into a dictionary called weatherData.
2. *slack API post* weatherData dictionary is stored as a text string and pushed to slack using incoming API webhook.

## Getting Started

1. Get API key from https://openweathermap.org/appid
2. Install python https://www.python.org/downloads/
3. Install a gui for running python, rodeo recommended: https://www.yhat.com/products/rodeo
4. Create a slack app and get the proper slack url to post your payload: https://api.slack.com/slack-apps

## Built With

* Python 3.4

## Authors

Matthew 'Ghost Tiger' Thompson 

## License

This project is for EVERYONE

## Acknowledgments

me, myself and I.
