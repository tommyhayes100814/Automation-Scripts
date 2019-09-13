import requests
import os
from twilio.rest import Client

# input city here
city = '-Enter desired city here-'
weatherkey = '-Enter weather key here-'
twilo_id = '-Enter twilo id here-'
twilo_token = '-Enter twilo token here-'
twilo_number = '+' + '-Enter twilo number here'
personal_number = '+' + '-Enter personal number here'

# degree sign unicode symbbol
degree_sign= u'\N{DEGREE SIGN}'

# weather api info
weather_key = weatherkey
city_name = city

# sms api information
sms_sid = twilo_id
sms_token = twilo_token

client = Client(sms_sid, sms_token)

title = 'Weather Notifcaton'

url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&APPID={weather_key}'

response = requests.get(url)

weather_data = response.json()

current_temp = weather_data['main']['temp']

def convert_to_farenh(temp):

    farenh = int((temp - 273.15) * 9/5 + 32)

    return farenh

def alert(title):
    text = convert_to_farenh(current_temp)

    farenh = 'The current temperature is: ' + str(text) + degree_sign

    message = client.messages \
                            .create(
                                 body=farenh,
                                 from_=twilo_number,
                                 to=personal_number
                             )

    print(message)

    print(farenh)
    os.system("""osascript -e 'display notification "{}" with title "{}"'""".format(farenh, title))



if __name__ == '__main__':
    alert(title)
