#!/usr/bin/env python2


"""
Part of update set for Resin used by 30MHz

Start menu presenting all available options with a one key press prompt.

A: Fokko
E: fokko@30MHz.com
D: 20 Dec 2017
"""


# Login
from login import login
login()

from readchar import readkey
from os import system

# Loading Resin Python SDK
from resin import Resin
resin = Resin()


# Define and import all functions
def logout():
    from logout import logout
    logout()
    return

def devlist():
    from devices import devicelist
    devicelist()
    return

def details():
    from devices import printdetails
    printdetails()
    return

def application_check():
    from application import printapplicationdetails
    printapplicationdetails()
    return

def update_device():
    from devices import setbuildinteractive
    setbuildinteractive()
    return

def switch_rolling():
    from application import setrollingupdates
    setrollingupdates()
    return

def set_basecommit():
    from application import setbasecommit
    setbasecommit()
    return

def do_updateallinteractive():
    from devices import updateallinteractive
    updateallinteractive()
    return

def quit():
    system("clear") # Linux - OSX only :(
    exit()

# Set all available options
while True:
    options = {
        "9" : logout,
        "0" : quit,
        "1" : devlist,
        "2" : details,
        "5" : application_check,
        "3" : update_device,
        "6" : switch_rolling,
        "7" : set_basecommit,
        "4" : do_updateallinteractive
        }

    # clear screen
    system("clear") # Linux - OSX only :(

    # print instructions
    print ("1 Get device list (UUID)")
    print ("2 Check device details (UUID)")
    print ("3 Update one device")
    print ("4 Update an entire application (One by one)")
    print ("5 Check application settings")
    print ("6 Switch rolling updates")
    print ("7 Set base commit application")
    print ("9 Logout")
    print ("0 Quit")
    print
    print ("Run:  ")

    # Wait for keypress
    while True:
        try:
            options[readkey()]()
        except KeyError:
            print "Invalid option"
        else:
            break
