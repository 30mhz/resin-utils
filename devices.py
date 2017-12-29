"""
Part of update set for Resin used by 30MHz

All functions related to managing devices settings. Serving the functions:
- Get device list (UUID): devicelist()
- Check device details (UUID): printdetails()
- Update one device: setbuildinteractive()
- Update an entire application (One by one): updateallinteractive()

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

# Helper function to return complete device list from available for this user
def get():
    devices = resin.models.device.get_all()
    return devices

def get_by_application_id(ID):
    try:
        devices = resin.models.device.get_all_by_application_id(ID)
    except:
        print ("Application not found.")
        devices = None
    return devices

# Helper function to get devices list and sort it on alphabetical order.
def devlist():
    devices = get()
    devices_uuid = {}
    devices_names = {}
    for items in devices:
        devices_uuid[items["uuid"]] = items
        devices_names[items["name"]] = items["uuid"]
    devices_names = sorted(devices_names.items(), key=operator.itemgetter(0))
    return devices_names

# Helper function to actually print the device list
def printlist(devices_names):
    for items in devices_names:
        print [items][0][0]
    return

# Helper function to actually update a device
def update(UUID, BuildID):
    status = resin.models.device.set_to_build('UUID', 'BuildID')
    return status

# Helper function to retreive applications name in device details list.
def getApplicationDetails(applicationid):
    return resin.models.application.get_by_id(applicationid)["app_name"]

# Helper function to show build details in device details list.
def getBuildDetails(buildid):
    if buildid is None:
        return "None"
    data = resin.models.build.get(buildid["__id"])
    details = "\n\n\tBuild ID: \t%s \n\tBuild hash: \t%s \n\tDate: \t\t%s" % (buildid["__id"], data["d"][0]["commit_hash"], data["d"][0]["push_timestamp"])
    return details

# Helper function that prints the actual device details
def details(uuid):
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
    print ("Application: %s" % getApplicationDetails(data["belongs_to__application"]["__id"]))
    print ("Build set: %s" % getBuildDetails(data["should_be_running__build"]))
    print
    print ("Commit: %s" % data["is_on__commit"])
    print ("OS: %s" % data["os_version"])
    print ("Supervisor: %s" % data["supervisor_version"])
    print
    print ("Created on: %s" % data["created_at"])
    return data["belongs_to__application"]["__id"]

# Function 'Get device list (UUID)' that prints all devices in alphabetical order.
def devicelist():
    system("clear") # Linux - OSX only :(
    for items in devlist():
        print ("%s\t%s" % (items[1],items[0]))
    raw_input ("Press enter to continue")

# Function 'Check device details (UUID)' that prints device details.
def printdetails():
    system("clear") # Linux - OSX only :(
    print ("Check device UUID on dashboard or go one step back and select \"Get device list\"")
    UUID = raw_input("Input your device UUID: ")
    system("clear") # Linux - OSX only :(
    try:
        details(UUID)
        print
        print
        print "Press a key to continue"
        readkey()
    except:
        print("UUID not corect or device not found. Press a key to continue.")
        readkey()

# Helper fucntion to get the application id from a UUID
def getapplicationid(UUID):
    return resin.models.device.get(UUID)["application"]["__id"]

# Helper function that shows the print while setting a specific build
def setbuildUI(UUID, BuildHash):
    print
    print "Setting build:"
    print "Device UUID %s" % UUID
    appID = getapplicationid(UUID)
    print "In application %s" % appID
    print "To build hash %s" % BuildHash
    try:
        from build import getBuildID
        BuildID = getBuildID(appID, BuildHash)
        print "That is buildnumber %s" % BuildID
        setbuild(UUID, BuildID)
        print "Setting value: Done"
        print
        details(UUID)
    except:
        print "Setting value: failed"
    print
    print
    print "Press a key to continue"
    return

# Helper function that actually sets the specific build
def setbuild(UUID, BuildID):
    print resin.models.device.set_to_build(UUID, BuildID)
    return

# function 'Update one device:' to update one device at a time
def setbuildinteractive():
    system("clear") # Linux - OSX only :(
    UUID = raw_input("Enter device UUID to update: ")
    system("clear") # Linux - OSX only :(
    try:
        applicationid = details(UUID)
    except:
        print "Device not found. Press a key to continue."
        readkey()
        return
    print
    from build import listAvailableBuilds
    listAvailableBuilds(applicationid)
    print
    COMMIT = raw_input("Enter hash to set: ")
    setbuildUI(UUID, COMMIT)
    readkey()

# Helper function to fix current software function in build parameter
def setCurrentFixed(UUID):
    device = resin.models.device.get(UUID)
    from build import getBuildID
    buildID = getBuildID(device['belongs_to__application']['__id'],device['commit'])
    setbuild(UUID, buildID)
    return device['commit']
    # u'application': {u'__deferred': {u'uri': u'/resin/application(328080)'}, u'__id': 328080}

# function 'Update an entire application (One by one):' interactively asking to update each device in a application
def updateallinteractive():
    from yesorno import query_yes_no
    from application import selectapplication, check
    ID = selectapplication()
    system("clear")
    print
    if check(ID) == None:
        return
    print
    from build import listAvailableBuilds,getBuildID,getAllBuildHash
    listAvailableBuilds(ID)
    print
    BuildHash = raw_input("Enter build Hash: ")
    try:
        BuildID = getBuildID(ID, BuildHash)
    except:
        print "Build not found."
        return
    devices = get_by_application_id(ID)
    system("clear")
    print ("Application: %s" % ID)
    print ("Build: %s" % BuildID)
    print ("Hash: %s" % BuildHash)
    # print devices
    print "Devices found: {0}".format(len(devices))
    print
    allcommits = getAllBuildHash(ID)
    def printdevices():
        print "Commit\t\t\t\t\t\tOnline\tCommit"
        for device in devices:
            # print device
            try:
                commit = allcommits[device['should_be_running__build']['__id']]['commit_hash']
            except:
                commit = "None\t\t\t\t\t"
            print "{2}\t{1}\t{0}".format(device['name'], device['is_online'], commit)
    printdevices()
    print
    for device in devices:
        # print device
        if device['is_online'] == True and device['should_be_running__build'] != None:
            # print BuildHash
            if BuildHash != None and device['should_be_running__build']['__id'] == BuildID:
                print "[{1}]\nSkipping device, it is already at commit {0}".format(BuildHash, device['name'])
            else:
                 # ask user if she wants to update it
                if query_yes_no("\n[{0}]\nDo you want to update the device?".format(device['name']),"no"):
                    setbuild(device['uuid'], BuildID)
                    # Old call but still handy :)
                    resin.models.supervisor.update(device['uuid'], device['belongs_to__application']['__id'], force=True)
                    print
        elif device['is_online'] == True and device['should_be_running__build'] == None:
            print ("\n[{0}] is online but no build is set. ".format(device['name']))
            if query_yes_no("Set current software version as fixed build?","no"):
                try:
                    commit = setCurrentFixed(device['uuid'])
                    print "Device now set to commit {0}".format(commit)
                except:
                    print "Error fixing current commit! Maybe device switched applications."
        else:
            print ("\n[{0}] is offline. ".format(device['name']))
            if device['should_be_running__build'] == None:
                if query_yes_no("And there is not build set. Set current software version as fixed build?","no"):
                    try:
                        commit = setCurrentFixed(device['uuid'])
                        print "Device now set to commit {0}".format(commit)
                    except:
                        print "Error fixing current commit! Maybe device switched applications."
            else:
                print "Skipping device"
    print "\n\nDone!"

    print "\n\nPress a key to continue."
    readkey()
