from os import system
import operator
from resin import Resin
resin = Resin()

def getallbuilds(APP_ID):
    return resin.models.build.get_all_by_application(APP_ID)

def getBuildDetails(APP_ID, COMMIT):
    all_builds = getallbuilds(APP_ID)
    builds_on_Hash = {}
    for items in all_builds:
       builds_on_Hash[items["commit_hash"]] = items
    return builds_on_Hash[COMMIT]

def getBuildID(APP_ID, COMMIT):
    return getBuildDetails(APP_ID, COMMIT)["id"]

def getAllBuildHash(ID):
    all_builds = getallbuilds(ID)
    builds_on_ID = {}
    for items in all_builds:
        builds_on_ID[items["id"]] = items
    return builds_on_ID

def listAvailableBuilds(applicationid):
    print "Available build options:"
    print "[Hash]\t\t\t\t\t\t[Timestamp]\t\t\t[ID]"
    availablebuild = getallbuilds(applicationid)
    for items in availablebuild:
        if items["status"]=="success":
            print ("%s\t%s\t%s" % (items["commit_hash"], items["push_timestamp"], items["id"]))
    return
