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
    print("[bold blue][1] IP lookup")
    print("[bold blue][2] Webhook Spammer")
    print("[bold blue][3] Shutdown")
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
    else:
        print("[bold red]Invalid choice, please try again.")
