import requests

def fetch_weather_data(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching weather data: {response.status_code}")
        return None

def display_current_weather(weather_data):
    if weather_data is None:
        return
    
    main_data = weather_data['main']
    weather = weather_data['weather'][0]

    print(f"Weather in {weather_data['name']}:")
    print(f"Description: {weather['description'].capitalize()}")
    print(f"Temperature: {main_data['temp']} °C")
    print(f"Humidity: {main_data['humidity']}%")
    print(f"Pressure: {main_data['pressure']} hPa")
    print(f"Wind Speed: {weather_data['wind']['speed']} m/s")

def main():
    api_key = 'ced98f46bf29ba3078ae443bdbc97148'  
    
    while True:
        location = input("Enter city name or ZIP code (or 'quit' to exit): ")
        if location.lower() == 'quit':
            break
        
        weather_data = fetch_weather_data(api_key, location)
        if weather_data:
            display_current_weather(weather_data)

if __name__ == "__main__":
    main()
