import os
import requests
import subprocess
import time
import socket
import webbrowser

install = 0
nomaakip = 1

def home():
    print('Welcome to cmdOS 1.4-nightly! there are currently 4 apps:')
    print(' freakybob   neko    miku    app_store')
    app = input()

    if app == 'app_store':
        print('--------------------------------------------------------')
        print('Welcome to the app store:there is currently 1 app that you can download!')
        print('--------------------------------------------------------')
        print('nomaakip')
        print('--------------------------------------------------------')
        downl = input()
        if downl == 'nomaakip':
            print('download nomaakip.app? (36kb)')
            print('Downloading nomaakip.html')
            nomaakip =+ 1
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
                 print('--------------------------------------------------------')
                 print('nomaakip.app downloaded successfully')
            else:
             print('Download failed!Check your internet connection.')


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
    if install == 0:
        print('--------------------------------------------------------')
        print('apps from app store:')
        print('nomaakip(make sure you downloaded it from the app store)')
        app = input()
        if app == 'nomaakip':
          RdFile = webbrowser.open(r'nomaakip.html') 
          print('going to nomaakip.github.io')
    else:
         code2()
    home()

def code2():
    app = input()

    if app == 'app_store':
        print('--------------------------------------------------------')
        print('Welcome to the app store:there is currently 1 app that you can download!')
        print('--------------------------------------------------------')
        print('nomaakip')
        print('--------------------------------------------------------')
        downl = input()
        if downl == 'nomaakip':
            print('download nomaakip.app? (36kb)')
            print('Downloading nomaakip.html')
            nomaakip =+ 1
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
                 print('--------------------------------------------------------')
                 print('nomaakip.app downloaded successfully')
                 print('--------------------------------------------------------')
                 nomaakip = True
            else:
             print('Download failed!Check your internet connection.')

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

    if install == 0:
        print('--------------------------------------------------------')
        print('apps from app store:')
        print('--------------------------------------------------------')
        print('nomaakip')
        app = input()
        if app == 'nomaakip':
          RdFile = webbrowser.open(r'nomaakip.html') 
          print('going to nomaakip.github.io')

    else:
         code2()
    code2()

def swagos():

    print("Welcome to  cmdOS! installing...")
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
                print("30% done")
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
