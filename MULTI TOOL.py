import requests
import os
import json
from rich import print, pretty
from rich.table import Table
from rich.panel import Panel
from rich.box import HEAVY
from rich.console import Console
from rich import print, panel

logo = """
[bold red]██╗    ██╗██╗  ██╗██╗   ██╗ █████╗     ███╗   ███╗██╗   ██╗██╗  ████████╗██╗    ████████╗ ██████╗  ██████╗ ██╗
██║    ██║██║  ██║██║   ██║██╔══██╗    ████╗ ████║██║   ██║██║  ╚══██╔══╝██║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║
██║ █╗ ██║███████║██║   ██║███████║    ██╔████╔██║██║   ██║██║     ██║   ██║       ██║   ██║   ██║██║   ██║██║
██║███╗██║╚════██║██║   ██║██╔══██║    ██║╚██╔╝██║██║   ██║██║     ██║   ██║       ██║   ██║   ██║██║   ██║██║
╚███╔███╔╝     ██║╚██████╔╝██║  ██║    ██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║       ██║   ╚██████╔╝╚██████╔╝███████╗
 ╚══╝╚══╝      ╚═╝ ╚═════╝ ╚═╝  ╚═╝    ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
 
"""

while True:
    os.system("2X MULTI TOOL")
    os.system("cls")
    print(logo)
    print("[bold blue][01] IP lookup")
    print("[bold blue][02] Webhook Spammer")
    print("[bold blue][03] Shutdown")
    print("[bold purple][04] Discord Nitro Generator")
    x = input("Enter your choice: ")

    if x == "1":
        os.system("cls")
        print("IP LOOKUP\n")
        ip = input("Enter IP: ")
        if not ip:
            print("[bold red]Error: No IP provided")
        else:
            os.system("cls")
            r = requests.get(f"http://ip-api.com/json/{ip}")
            data = r.json()
            print(f"[bold cyan]IP: {data['query']}")
            print(f"[bold cyan]Country: {data['country']}")
            print(f"[bold cyan]Region: {data['regionName']}")
            print(f"[bold cyan]City: {data['city']}")
            print(f"[bold cyan]Time Zone: {data['timezone']}")
            print(f"[bold cyan]Zip Code: {data['zip']}")
            print("")
        pause = input("Press enter to continue...")

    if x == "2":
        os.system("cls")
        print("WEBHOOK SPAMMER\n")
        webhook = input("Enter webhook URL: ")
        message = input("Enter message: ")
        count = int(input("Enter number of messages: "))
        os.system("cls")
        for i in range(count):
            requests.post(webhook, json={"content": message})
            print(f"Sent message #{i+1}/{count}")
        pause = input("Press enter to continue...")

    if x == "3":
        break

   if x == '4':
        os.system("cls")
    print("[bold purple]Discord Nitro Generator\n")
    print("Generating and checking Discord Nitro links. Press Enter to stop.")
    
    def check_nitro_code(code):
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)
        return response.status_code == 200

    stop_flag = threading.Event()

    def check_for_enter():
        while not stop_flag.is_set():
            if msvcrt.kbhit() and msvcrt.getch() == b'\r':
                stop_flag.set()

    enter_thread = threading.Thread(target=check_for_enter)
    enter_thread.start()

    while not stop_flag.is_set():
        code = ''.join([chr(randint(48, 122)) for _ in range(16)])
        nitro_link = f"https://discord.gift/{code}"
        
        if check_nitro_code(code):
            print(f"\n[bold green]Valid Nitro Link Found: {nitro_link}")
            break
    
    stop_flag.set()
    enter_thread.join()

    if not check_nitro_code(code):
        print("\n[bold red]No valid Nitro link found. Process stopped.")
    
    input("\nPress enter to continue...")

    else:
        print("[bold red]Invalid choice, please try again.")
