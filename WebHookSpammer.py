import requests
import time
logo = """
 █     █░▓█████  ▄▄▄▄    ██░ ██  ▒█████   ▒█████   ██ ▄█▀         
▓█░ █ ░█░▓█   ▀ ▓█████▄ ▓██░ ██▒▒██▒  ██▒▒██▒  ██▒ ██▄█▒          
▒█░ █ ░█ ▒███   ▒██▒ ▄██▒██▀▀██░▒██░  ██▒▒██░  ██▒▓███▄░          
░█░ █ ░█ ▒▓█  ▄ ▒██░█▀  ░▓█ ░██ ▒██   ██░▒██   ██░▓██ █▄          
░░██▒██▓ ░▒████▒░▓█  ▀█▓░▓█▒░██▓░ ████▓▒░░ ████▓▒░▒██▒ █▄         
░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒         
  ▒ ░ ░   ░ ░  ░▒░▒   ░  ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░         
  ░   ░     ░    ░    ░  ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░          
    ░       ░  ░ ░       ░  ░  ░    ░ ░      ░ ░  ░  ░            
                      ░                                           
  ██████  ██▓███   ▄▄▄       ███▄ ▄███▓ ███▄ ▄███▓▓█████  ██▀███  
▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░▓██    ▓██░▒███   ▓██ ░▄█ ▒
  ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██ ▒██    ▒██ ▒▓█  ▄ ▒██▀▀█▄  
▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒▒██▒   ░██▒░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░░ ▒░   ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░░  ░      ░ ░ ░  ░  ░▒ ░ ▒░
░  ░  ░  ░░         ░   ▒   ░      ░   ░      ░      ░     ░░   ░ 
      ░                 ░  ░       ░          ░      ░  ░   ░
"""


print(logo)
message = input("What message do you want to send? ")
discord_webhook = input("Please enter your discord webhook: ")

number = input("How many times do you want to send the message? ")


try:
    number = int(number)
except ValueError:
    print("Please enter a valid number")
    exit()


for i in range(number):
    response = requests.post(discord_webhook, json={"content": message})
    if response.status_code == 204:
        print(f"Message {i+1} sent successfully")
    if response.status_code == 429:
        print(f"Webhook is being rate limited waiting 5 seconds and trying again")
        exit = input("Do you want to exit? (y/n) ")
        if exit == "y":
            break
        if exit == "n":
            print("Continuing")


    if i + 1 == number:
        print("All messages sent successfully")
        time.sleep(5)
        exit()


        time.sleep(5)
        

        