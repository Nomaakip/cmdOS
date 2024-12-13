import os
import requests
import subprocess
import time
import socket

install = 0

def swagos():

    print("Welcome to terminal OS! installing...")
    print("make sure you are connected to the internet before continuing!")
    url = 'https://raw.githubusercontent.com/Nomaakip/cmdOS/refs/heads/main/miku.txt'
    response = requests.get(url)
    file_Path = 'miku.txt'
    response = requests.get(url)
    print('downloading miku.txt')
    if response.status_code == 200:
            with open(file_Path, 'wb') as file:
                file.write(response.content)
                print('File downloaded successfully')
                print("10% done")
    else:
         print('Download failed!Check your internet connection.')
    print("installing homescreen.txt")
swagos()
