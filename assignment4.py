import requests

def get_weather(city, api_key):
    # Implementation for fetching weather
    pass

def main():
    city = input("Enter city name: ")
    api_key = 'your_api_key_here'
    weather_info = get_weather(city, api_key)
    print(weather_info)

# Ensure that the main function is called at the end of the script
if __name__ == "__main__":
    main()