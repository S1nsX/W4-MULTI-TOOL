import os
import webbrowser
import requests
from rich import print

logo = """
[bold red]██╗    ██╗██╗  ██╗██╗   ██╗ █████╗     ███╗   ███╗██╗   ██╗██╗  ████████╗██╗    ████████╗ ██████╗  ██████╗ ██╗     
██║    ██║██║  ██║██║   ██║██╔══██╗    ████╗ ████║██║   ██║██║  ╚══██╔══╝██║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██║ █╗ ██║███████║██║   ██║███████║    ██╔████╔██║██║   ██║██║     ██║   ██║       ██║   ██║   ██║██║   ██║██║     
██║███╗██║╚════██║██║   ██║██╔══██║    ██║╚██╔╝██║██║   ██║██║     ██║   ██║       ██║   ██║   ██║██║   ██║██║     
╚███╔███╔╝     ██║╚██████╔╝██║  ██║    ██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║       ██║   ╚██████╔╝╚██████╔╝███████╗
 ╚══╝╚══╝      ╚═╝ ╚═════╝ ╚═╝  ╚═╝    ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝  
                                                                 
"""

passwords = {}

def get_weather(api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    location_url = "http://api.ipstack.com/check?access_key=7JBqILZALr9s5ubf5tSnxTAVZPFreMcR"  # Replace with your actual IPStack API key
    location_response = requests.get(location_url)
    location_data = location_response.json()
    latitude = location_data["latitude"]
    longitude = location_data["longitude"]
    complete_url = f"{base_url}appid={api_key}&lat={latitude}&lon={longitude}"
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        return f"Temperature: {main['temp']}K\nPressure: {main['pressure']}hPa\nHumidity: {main['humidity']}%\nWeather: {weather['description']}"
    else:
        return "Weather information not found"

while True:
    os.system("cls")
    print(logo)
    print("[bold blue][1] IP lookup")
    print("[bold blue][2] Webhook Spammer")
    print("[bold blue][3] Secret")
    print("[bold blue][4] Password Saver")
    print("[bold blue][5] Weather Information")
    print("[bold blue][6] Shutdown")
    x = input("Enter your choice: ")

    if x == "1":
        os.system("cls")
        print("[bold blue]IP LOOKUP\n")
        ip = input("Enter IP: ")
        if not ip:
            print("[bold red]Error: No IP provided")
        else:
            os.system("cls")
            # Add your IP lookup logic here

    elif x == "2":
        os.system("cls")
        webhook = input("Enter webhook URL: ")
        message = input("Enter message: ")
        count = int(input("Enter number of messages: "))
        for i in range(count):
            requests.post(webhook, json={"content": message})
            print(f"Sent message #{i+1}/{count}")
        pause = input("Press enter to continue...")

    elif x == "3":
        os.system("cls")
        confirmation = input("Are you sure? (yes/no): ")
        if confirmation.lower() == "yes":
            webbrowser.open("https://pornhub.com")  # Replace with an appropriate URL

    elif x == "4":
        os.system("cls")
        print("[bold blue]Password Saver\n")
        # Add your password saver logic here

    elif x == "5":
        os.system("cls")
        print("[bold blue]Weather Information\n")
        api_key = "98d5964fb273418162ec7034276b96d6"  # Replace with your actual OpenWeatherMap API key
        weather_info = get_weather(api_key)
        print(weather_info)
        pause = input("Press enter to continue...")

    elif x == "6":
        break

    else:
        print("[bold red]Invalid choice, please try again.")