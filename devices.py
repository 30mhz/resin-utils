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
    resin.models.device.set_to_build(UUID, BuildID)
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
    # print getallbuilds(applicationid)
    print
    COMMIT = raw_input("Enter hash to set: ")
    setbuildUI(UUID, COMMIT)

    readkey()
    # resin.models.device.set_to_build('8deb12a58e3b6d3920db1c2b6303d1ff32f23d5ab99781ce1dde6876e8d143', '123098')

def updateallinteractive():
    from yesorno import query_yes_no
    from application import selectapplication, check
    ID = selectapplication()
    system("clear")
    print
    check(ID)
    print
    from build import listAvailableBuilds,getBuildID
    listAvailableBuilds(ID)
    print
    BuildHash = raw_input("Enter build Hash: ")
    BuildID = getBuildID(ID, BuildHash)
    devices = get_by_application_id(ID)
    print devices
    print "Found {0} devices:".format(len(devices))
    print
    print "Commit\t\t\t\t\t\tOnline\tCommit"
    for device in devices:
        online = False
        if device['is_online'] == True:
            online = True
        print "{2}\t{1}\t{0}".format(device['name'], online, device['commit'])

    print
    for device in devices:
        if online:
            BuildHash
            if BuildHash != None and device['build']['__id'] == BuildID:
                print "[{1}]\nSkipping device, it is already at commit {0}".format(BuildHash, device['name'])
            else:
                if 
                 # ask user if she wants to update it
                if query_yes_no("\n[{0}]\nDo you want to update the device?".format(device['name'])):
                    # resin.models.supervisor.update(device['uuid'], device['application']['__id'], force=True)
                    print
        else:
            print ("[{0}]\nSkipping device, it's offline. ".format(device['name']))
    readkey()
