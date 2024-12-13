import os
import requests
import subprocess
import time
import socket
import webbrowser

install = 0

def home():
    print('Welcome to cmdOS 1.2! there are currently 4 apps:')
    print('nomaakip     freakybob   neko    miku')
    app = input()
    if app == 'freakybob':
        freaky = open("freakybob.txt", "r")
        print(freaky.read())
        freaky.close()
        code2()
    elif app == 'miku':
        miku = open("miku.txt", "r")
        print(miku.read())
        miku.close()
        
    elif app == 'neko':
        neko = open("neko.txt", "r")
        print(neko.read())
        neko.close()
        code2()

    elif app == 'nomaakip':
        url = 'https://raw.githubusercontent.com/Nomaakip/cmdOS/refs/heads/main/9d058db6-36a9-4bc0-b3a2-60aed0cb1a85.jpg'
        file_Path = '9d058db6-36a9-4bc0-b3a2-60aed0cb1a85.jpg'
        response = requests.get(url)
        if response.status_code == 200:
            with open(file_Path, 'wb') as file:
                file.write(response.content)
                print('File downloaded successfully')
                
        else:
         print('Download failed!Check your internet connection.')

         url = 'https://raw.githubusercontent.com/Nomaakip/cmdOS/refs/heads/main/github.png'
         file_Path = 'github.png'
         response = requests.get(url)
         if response.status_code == 200:
            with open(file_Path, 'wb') as file:
                file.write(response.content)
                print('File downloaded successfully')
                
         else:
          print('Download failed!Check your internet connection.')
        RdFile = webbrowser.open(r'nomaakip.html') 
        print('going to nomaakip.github.io')
    else:
         code2()
    code2()

def code2():
    app = input()
    if app == 'freakybob':
        freaky = open("freakybob.txt", "r")
        print(freaky.read())
        freaky.close()
        code2()

    elif app == 'miku':
        miku = open("miku.txt", "r")
        print(miku.read())
        miku.close()
    
    elif app == 'neko':
        neko = open("neko.txt", "r")
        print(neko.read())
        neko.close()
        code2()

    elif app == 'nomaakip':
        url = 'https://raw.githubusercontent.com/Nomaakip/cmdOS/refs/heads/main/9d058db6-36a9-4bc0-b3a2-60aed0cb1a85.jpg'
        file_Path = '9d058db6-36a9-4bc0-b3a2-60aed0cb1a85.jpg'
        response = requests.get(url)
        if response.status_code == 200:
            with open(file_Path, 'wb') as file:
                file.write(response.content)
                print('File downloaded successfully')
                
        else:
         print('Download failed!Check your internet connection.')

         url = 'https://raw.githubusercontent.com/Nomaakip/cmdOS/refs/heads/main/github.png'
         file_Path = 'github.png'
         response = requests.get(url)
         if response.status_code == 200:
            with open(file_Path, 'wb') as file:
                file.write(response.content)
                print('File downloaded successfully')
                
         else:
          print('Download failed!Check your internet connection.')
        RdFile = webbrowser.open(r'nomaakip.html') 
        print('going to nomaakip.github.io')
    else:
         code2()
    code2()

def swagos():

    print("Welcome to cmdOS! installing...")
    print("make sure you are connected to the internet before continuing!")
    time.sleep(3)
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
    print("installing neko.txt")
    url = 'https://raw.githubusercontent.com/Nomaakip/cmdOS/refs/heads/main/neko.txt'
    response = requests.get(url)
    file_Path = 'neko.txt'
    response = requests.get(url)
    if response.status_code == 200:
            with open(file_Path, 'wb') as file:
                file.write(response.content)
                print('File downloaded successfully')
                print("20% done")
    else:
         print('Download failed!Check your internet connection.')
    print('Downloading nomaakip.html')
    url = 'https://raw.githubusercontent.com/Nomaakip/cmdOS/refs/heads/main/nomaakip.html'
    response = requests.get(url)
    file_Path = 'nomaakip.html'
    response = requests.get(url)
    if response.status_code == 200:
            with open(file_Path, 'wb') as file:
                file.write(response.content)
                print('File downloaded successfully')
                print("50% done")
    else:
         print('Download failed!Check your internet connection.')
    print("Downloading important files...")
    url = 'https://raw.githubusercontent.com/Nomaakip/cmdOS/refs/heads/main/freakbob.txt'
    response = requests.get(url)
    file_Path = 'freakbob.txt'
    response = requests.get(url)
    if response.status_code == 200:
            with open(file_Path, 'wb') as file:
                file.write(response.content)
                print('File downloaded successfully')
                print("90% done")
    else:
         print('Download failed!Check your internet connection.')
    url = 'https://raw.githubusercontent.com/Nomaakip/cmdOS/refs/heads/main/switch.txt'
    response = requests.get(url)
    file_Path = 'switch.txt'
    response = requests.get(url)
    if response.status_code == 200:
            with open(file_Path, 'wb') as file:
                file.write(response.content)
                print('File downloaded successfully')
                print("95% done")
    else:
         print('Download failed!Check your internet connection.')
    url = 'https://raw.githubusercontent.com/Nomaakip/cmdOS/refs/heads/main/w.txt'
    file_Path = 'w.txt'
    response = requests.get(url)
    if response.status_code == 200:
            with open(file_Path, 'wb') as file:
                file.write(response.content)
                print('File downloaded successfully')
                print("100% done")
    print('..')
    miku = open("miku.txt", "r")
    print(miku.read())
    miku.close()
    time.sleep(2)
    print('--------------------------------------------------------')
    print('we are setting up things for you.')
    print('--------------------------------------------------------')
    time.sleep(2)
    print('please wait.')
    print('--------------------------------------------------------')
    time.sleep(2)
    url = 'https://raw.githubusercontent.com/Nomaakip/cmdOS/refs/heads/main/home.txt'
    file_Path = 'home.txt'
    response = requests.get(url)
    if response.status_code == 200:
            with open(file_Path, 'wb') as file:
                file.write(response.content)
                print('os sucessfully set up.')
    else:
         print('Download failed!Check your internet connection.')
    home()

    
swagos()
