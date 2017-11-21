from os import system
from resin import Resin
resin = Resin()

import operator

def get():
    devices = resin.models.device.get_all()
    return devices

def list():
    devices = get()
    devices_uuid = {}
    devices_names = {}
    for items in devices:
        devices_uuid[items["uuid"]] = items
        devices_names[items["name"]] = items["uuid"]
    devices_names = sorted(devices_names.items(), key=operator.itemgetter(0))
    return devices_uuid, devices_names

def printlist(devices_names):
    for items in devices_names:
        print [items][0][0]
    return

def getApplicationDetails(applicationid):
    return resin.models.application.get_by_id(applicationid)["app_name"]


def getBuildDetails(buildid):
    if buildid is None:
        return "None"
    data = resin.models.build.get(buildid["__id"])["d"][0]
    details = str(buildid) + ", " + data["commit_hash"] + ", " + data["push_timestamp"]
    return details

def details(uuid):
    system("clear") # Linux - OSX only :(
    data = resin.models.device.get(uuid)
    print ("Device name: %s" % data["name"])
    print ("ID: %s" % data["id"])
    print ("UUID: %s" % data["uuid"])
    print
    print ("Is online: %s" % data["is_online"])
    print ("Last seen: %s" % data["last_connectivity_event"])
    print ("Location: %s" % data["location"])
    print
    print ("Local IP: %s" % data["ip_address"])
    print ("Public IP: %s" % data["public_address"])
    print
    print ("Application: %s" % getApplicationDetails(data["application"]["__id"]))
    print ("Build set: %s" % getBuildDetails(data["build"]))
    print
    print ("Commit: %s" % data["commit"])
    print ("OS: %s" % data["os_version"])
    print ("Supervisor: %s" % data["supervisor_version"])
    print
    print ("Created on: %s" % data["created_at"])
    print
    print
    print "Press enter to continue"
    return 0
