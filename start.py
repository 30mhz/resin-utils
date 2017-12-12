
# Login
import login
from readchar import readkey
from os import system

from resin import Resin
resin = Resin()

def logout():
    from logout import logout
    logout()
    return

def devlist():
    # import devlist
    return

def details():
    # import details
    return

def application_update():
    # import application_update
    return

def application_check():
    # import application_check
    return

def update_device():
    # import update_device
    return

def quit():
    system("clear") # Linux - OSX only :(
    exit()

while True:
    options = {
        "9" : logout,
        "0" : quit,
        "1" : devlist,
        "2" : details,
        "5" : application_check,
        "3" : update_device
        }

    system("clear") # Linux - OSX only :(

    print ("1 Get device list (UUID)")
    print ("2 Check device details (UUID)")
    print ("3 Update one device")
    print ("4 Update an entire application (One by one)")
    print ("5 Check application settings")
    print ("6 Swith rolling updates")
    print ("7 Set base commit application")
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
