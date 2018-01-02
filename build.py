"""
Part of update set for Resin used by 30MHz

All functions related to view build settings.
Builds are set with their build hashes, but are application specific
thus get a buildnumber accordingly.

A: Fokko
E: fokko@30MHz.com
D: 20 Dec 2017
"""

from os import system # for screen clear

# Loading Resin Python SDK
from resin import Resin
resin = Resin()

# Helper function to retreive all builds in a specific application
def getallbuilds(APP_ID):
    return resin.models.build.get_all_by_application(APP_ID)

# Helper function that retreives details of a specific build using its commit hash
def getBuildDetails(APP_ID, COMMIT):
    all_builds = getallbuilds(APP_ID)
    builds_on_Hash = {}
    for items in all_builds:
       builds_on_Hash[items["commit_hash"]] = items
    return builds_on_Hash[COMMIT]

# Helper function that returns the build ID from a specific build in its app
def getBuildID(APP_ID, COMMIT):
    return getBuildDetails(APP_ID, COMMIT)["id"]

# Helper function that return a list of available builds and stores it on ID
def getAllBuildHash(ID):
    all_builds = getallbuilds(ID)
    builds_on_ID = {}
    for items in all_builds:
        builds_on_ID[items["id"]] = items
    return builds_on_ID

# Helper function tgat actually prints all available builds.
def listAvailableBuilds(applicationid):
    print "Available build options:"
    print "[Hash]\t\t\t\t\t\t[Timestamp]\t\t\t[ID]"
    availablebuild = getallbuilds(applicationid)
    for items in availablebuild:
        if items["status"]=="success":
            print ("%s\t%s\t%s" % (items["commit_hash"], items["push_timestamp"], items["id"]))
    return
