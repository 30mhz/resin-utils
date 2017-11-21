# Login
import login
from time import sleep
from readchar import readkey
from os import system

from resin import Resin

resin = Resin()

def logout():
    resin.auth.log_out()
    print("Logged out")
    exit()

def details():
    from devices import details
    system("clear") # Linux - OSX only :(
    UUID = raw_input("Input your device UUID: ")
    try:
        details(UUID)
        readkey()
    except:
        print("UUID not corect or device not found. Press a key to continue.")
        readkey()

def quit():
    exit()

while True:
    options = {
        "9" : logout,
        "1" : details,
        "0" : quit,
        }

    system("clear") # Linux - OSX only :(

    print ("1 Check device details (UUID)")
    print ("9 Logout")
    print ("0 Quit")
    print
    print ("Run:  ")

    while True:
        try:
            options[readkey()]()
        except KeyError:
            print "Invalid option"
        else:
            break

        # # while True:
        # try:
        #
        # except:
        #     print "Invalid option"
        # sleep(1)
