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

def application_update():
    print ("Application update:")

def application_check():
    system("clear") # Linux - OSX only :(
    print ("Select Application to check settings:")
    print #newline
    print ("ID\tNAME")
    import application
    applications, shortlist = application.list()
    for items in shortlist:
        print ("%s\t%s" % (items[1], items[0]))
    print #newline
    ID = input("Please enter application ID: ")
    system("clear") # Linux - OSX only :(
    application.check(ID)
    readkey()


def quit():
    exit()

while True:
    options = {
        "9" : logout,
        "0" : quit,
        "1" : details,
        "4" : application_check
        }

    system("clear") # Linux - OSX only :(

    print ("1 Check device details (UUID)")
    print ("2 Update one device")
    print ("3 Update an entire application (One by one)")
    print ("4 Check application settings")
    print ("5 Swith rolling updates")
    print ("6 Set base commit application")
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
