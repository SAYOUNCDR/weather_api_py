import requests

API_KEY = "9412facaf953881806d802c79df734aa"

#then url to which we hit and get data
BASE_URL="https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: \n")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

# getting the request request 
response = requests.get(request_url)


if response.status_code == 200:
    # getting the  data in jason format
    data = response.json()

    # extracting city name from the json
    city_name = data ['name']
    
    # extraacting weather description from the json
    weather = data ['weather'] [0] ['description']

    # extracting temprature and converting it into celcius aand rouding off to 2 decimal places
    temp = round(data ['main'] ['temp'] - 273.15, 2)

    # extracting country of the state 
    country = data ['sys'] ['country']

    print(f"Given city is in {country}")
    print(f"The weather in {city_name} is {weather} and temprature is approx {temp} degree celcius")
    
else:
    print("An error occured")