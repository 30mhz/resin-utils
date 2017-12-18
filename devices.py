from os import system
from readchar import readkey
import operator
from resin import Resin
resin = Resin()


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

def devlist():
    devices = get()
    devices_uuid = {}
    devices_names = {}
    for items in devices:
        devices_uuid[items["uuid"]] = items
        devices_names[items["name"]] = items["uuid"]
    devices_names = sorted(devices_names.items(), key=operator.itemgetter(0))
    return devices_names

def printlist(devices_names):
    for items in devices_names:
        print [items][0][0]
    return

def update(UUID, BuildID):
    status = resin.models.device.set_to_build('UUID', 'BuildID')
    return status

def getApplicationDetails(applicationid):
    return resin.models.application.get_by_id(applicationid)["app_name"]


def getBuildDetails(buildid):
    if buildid is None:
        return "None"
    data = resin.models.build.get(buildid["__id"])
    details = "\n\n\tBuild ID: \t%s \n\tBuild hash: \t%s \n\tDate: \t\t%s" % (buildid["__id"], data["d"][0]["commit_hash"], data["d"][0]["push_timestamp"])
    return details



def getapplicationid(UUID):
    return resin.models.device.get(UUID)["application"]["__id"]

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
    print ("Application: %s" % getApplicationDetails(data["application"]["__id"]))
    print ("Build set: %s" % getBuildDetails(data["build"]))
    print
    print ("Commit: %s" % data["commit"])
    print ("OS: %s" % data["os_version"])
    print ("Supervisor: %s" % data["supervisor_version"])
    print
    print ("Created on: %s" % data["created_at"])
    return data["application"]["__id"]

def devicelist():
    system("clear") # Linux - OSX only :(
    for items in devlist():
        print ("%s\t%s" % (items[1],items[0]))
    # print ("Devices:")
    # readkey()
    # system("clear") # Linux - OSX only :(
    raw_input ("Press enter to continue")

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

def setbuild(UUID, BuildID):
    print resin.models.device.set_to_build(UUID, BuildID)
    return

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
    # print getallbuilds(appli4cationid)
    print
    COMMIT = raw_input("Enter hash to set: ")
    setbuildUI(UUID, COMMIT)

    readkey()
    # resin.models.device.set_to_build('8deb12a58e3b6d3920db1c2b6303d1ff32f23d5ab99781ce1dde6876e8d143', '123098')

def setCurrentFixed(UUID):
    device = resin.models.device.get(UUID)
    from build import getBuildID
    buildID = getBuildID(device['application']['__id'],device['commit'])
    setbuild(UUID, buildID)
    return device['commit']
    # u'application': {u'__deferred': {u'uri': u'/resin/application(328080)'}, u'__id': 328080}

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
                commit = allcommits[device['build']['__id']]['commit_hash']
            except:
                commit = "None\t\t\t\t\t"
            print "{2}\t{1}\t{0}".format(device['name'], device['is_online'], commit)
    printdevices()

    print
    for device in devices:
        # print device
        if device['is_online'] == True:
            BuildHash
            if BuildHash != None and device['build']['__id'] == BuildID:
                print "[{1}]\nSkipping device, it is already at commit {0}".format(BuildHash, device['name'])
            else:
                 # ask user if she wants to update it
                if query_yes_no("\n[{0}]\nDo you want to update the device?".format(device['name'])):
                    setbuild(device['uuid'], BuildID)
                    # Old call but still handy :)
                    resin.models.supervisor.update(device['uuid'], device['application']['__id'], force=True)
                    print
        else:
            print ("\n[{0}] is offline. ".format(device['name']))
            if device['build'] == None:
                if query_yes_no("And there is not build set. Set current software version as fixed build?"):
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
