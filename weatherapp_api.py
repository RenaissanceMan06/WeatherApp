import json
import pyowm
import requests


print('\n')
print('=='*40)
print('International Weather App'.center(80, '_'))
print('=='*40)
print('To find weather information, type your city below.')
print('*Please note, temperature readings are in Fahrenheit.')
print('=='*40)
print('\n')

def main():
# using requests library to capture our weather data from openweathermap
    api_key = 'api_key' # my api key
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    location = input('Enter city name: ') # prompt user for city name
    url = base_url + 'appid=' + api_key + '&q=' + location
    response = requests.get(url)
    response.raise_for_status()
    json_storage = response.json() # storing response in json format
    if json_storage['cod'] != 404: # testing our connection
        print('Connection Status: Good!')
    else:
        print('There\'s an error with your connection')
    print('=='*25)


# using PyOWN library to print weather forecast
    degree_sign = u'\N{DEGREE SIGN}' # using degree sign for fahrenheit reading
    own = pyowm.OWM(api_key) # using my key for pyOWM library
    yourlocation = own.weather_at_place(location.title())
    weather = yourlocation.get_weather()
    temperature = weather.get_temperature('fahrenheit')['temp'] # function method to display current temp
    temperature_max = weather.get_temperature('fahrenheit')['temp_max'] # function method to display max temp
    temperature_min = weather.get_temperature('fahrenheit')['temp_min'] # function method to display lowest temp

    print(f'Current temperature in {location.title()}: {temperature}{degree_sign}')
    print(f'High temperature: {temperature_max}{degree_sign}')
    print(f'Low temperature: {temperature_min}{degree_sign}')
    humidity = weather.get_humidity()
    print(f'Humidity: {humidity} %')
    detail_status = weather.get_detailed_status() # outlook forecast function method
    print(f'Outlook: {detail_status}')
    rain = weather.get_rain()
    if rain == {}:
        print('No Precipitation: ')
    else:
        print('Precipitation: ', rain['1h'], '%')
    wind = weather.get_wind()['speed']
    print(f'Wind speed: {wind} mph')
    snow = weather.get_snow()
    if snow == {}:
        print('No Snow: ')
    else:
        print('Snow: ', snow['1h'], '%')

    print('=='*25)


# using main function to loop script
main()
while True:
    print('Would you like weather information for another city? ')
    get_weather = input('Please enter yes or no: ')
    if get_weather == 'yes':
        print(main())
    else:
        print('Enjoy your day!')
        break



