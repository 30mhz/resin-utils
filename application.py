"""
Part of update set for Resin used by 30MHz

All functions related to managing application settings. Serving the functions:
- Check application settings: printapplicationdetails()
- Switch rolling updates: setrollingupdates()
- Set base commit application: setbasecommit()

A: Fokko
E: fokko@30MHz.com
D: 20 Dec 2017
"""

from os import system # for clear
from readchar import readkey # to get a keypress
import operator # for sorting

# Loading Resin Python SDK
from resin import Resin
resin = Resin()

# helper function that actually retrieves the application list
def get():
    return resin.models.application.get_all()

# Helper function that retreives all applications and sorts them alphabetically
def list():
    applications = get()
    applications_uuid = {}
    applications_names = {}
    for items in applications:
        applications_uuid[items["id"]] = items
        applications_names[items["app_name"]] = items["id"]
    applications_names = sorted(applications_names.items(), key=operator.itemgetter(0))
    return applications_uuid, applications_names

# Helper function that actually prints the application data
def check(ID):
    try:
        data = resin.models.application.get_by_id(ID)
    except:
        print "Application not found"
        readkey()
        return None
    print ("Application name:\t%s" % data["app_name"] )
    print ("Application ID:\t\t%s" % data["id"] )
    print ("URL:\t\t\thttps://dashboard.resin.io/apps/%s/devices" % data["id"])# https://dashboard.resin.io/apps/747385/devices
    print # newline
    print ("Rolling updates enabled: %s" % data["should_track_latest_release"])
    print
    print ("Default software:\t %s" % data["commit"])
    from build import getBuildDetails
    builddetials = getBuildDetails(ID,data["commit"])
    print ("Push data:\t\t %s" % builddetials["push_timestamp"])
    print ("Build id:\t\t %s" % builddetials["id"])
    return data

# Helper function that displays all applications, in order to help the user to select one.
def selectapplication():
    system("clear") # Linux - OSX only :(
    print ("Select Application to check settings:")
    print #newline
    print ("ID\tNAME")
    applications, shortlist = list()
    for items in shortlist:
        print ("%s\t%s" % (items[1], items[0]))
    print #newline
    ID = input("Please enter application ID: ")
    return ID

# function 'Check application settings' that prints applicaiton details
def printapplicationdetails():
    ID = selectapplication()
    try:
        system("clear") # Linux - OSX only :(
        check(ID)
    except:
        print "Retrieve error."
        print
    print "Press a key to continue."
    readkey()
    return ID

# function 'Switch rolling updates' to toggle the automatic update setting
def setrollingupdates():
    ID = selectapplication()
    check(ID)
    from yesorno import query_yes_no
    print
    if query_yes_no("Do you want to disable rolling updates?", "yes"):
        print "Disabling"
        resin.models.application.disable_rolling_updates(ID)
    else:
        print
        if query_yes_no("Do you want to re-enable rolling updates?", "no"):
            print "Enabling"
            resin.models.application.enable_rolling_updates(ID)
        else:
            print "Nothing done."
    print "OK"
    print "Press a key to continue."
    readkey()

# Helper function to set the default application software
# This function isn't implemented in the Resin Python SDK
# the web api was used to fullfill this function.
def setcommittroughapi(ID, Commit):
    import requests
    endpoint = "https://api.resin.io/v2/application(%s)" % ID
    data = {"commit":"%s" % Commit}
    headers = {"Authorization":"Bearer %s" % resin.auth.get_token()}

    return requests.patch(endpoint,data=data,headers=headers).text

# function 'Set base commit application' to set the default commit of an application
def setbasecommit():
    ID = selectapplication()
    print
    check(ID)
    print
    import build
    build.listAvailableBuilds(ID)
    print
    BuildHash = raw_input("Enter build Hash: ")
    # Is not implmented in SDK, so API is used.
    print setcommittroughapi(ID, BuildHash)
    print
    check(ID)
    print
    print "Default commit changed!"
    print "Press a key to continue."
    readkey()
