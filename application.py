import general


def get():
    applications = resin.models.application.get_all()
    return applications

def list():
    applications = get()
    applications_uuid = {}
    applications_names = {}
    for items in applications:
        applications_uuid[items["id"]] = items
        applications_names[items["app_name"]] = items["id"]
    applications_names = sorted(applications_names.items(), key=operator.itemgetter(0))
    return applications_uuid, applications_names

def check(ID):
    data = resin.models.application.get_by_id(ID)
    print ("Aplication name:\t%s" % data["app_name"] )
    print ("Aplication ID:\t\t%s" % data["id"] )
    print ("URL:\t\t\thttps://dashboard.resin.io/apps/%s/devices" % data["id"])# https://dashboard.resin.io/apps/747385/devices
    print # newline
    print ("Rolling updates enabled: %s" % data["should_track_latest_release"])
    print
    print ("Default software:\t %s" % data["commit"])
    from build import getBuildDetails
    builddetials = getBuildDetails(ID,data["commit"])
    print ("Push data:\t\t %s" % builddetials["push_timestamp"])
    print ("Build id:\t\t %s" % builddetials["id"])
    print
    print "Press a key to continue."
    #{u'depends_on__application': None, u'should_track_latest_release': True, u'app_name': u'NewMotherTemp', u'__metadata': {u'type': u'', u'uri': u'/resin/application(770949)'}, u'is_accessible_by_support_until__date': None, u'actor': 2083072, u'git_repository': u'resin15/newmothertemp', u'version': 1, u'user': {u'__deferred': {u'uri': u'/resin/user(8052)'}, u'__id': 8052}, u'device_type': u'beaglebone-black', u'commit': u'4c75e9991754cf4a440e0c6c9d3be45aa5401102', u'id': 770949}
    # ID: 890981
    # UUID: 2801325107d749c9f029fd3aa09f8063
    #
    # Is online: True
    # Last seen: 2017-12-11T10:45:49.050Z
    # Location: Amsterdam, North Holland, Netherlands
    #
    # Local IP: 192.168.8.82
    # Public IP: 185.3.177.98
    return data
