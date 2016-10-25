import argparse
import sys
from resin import exceptions

from resin import Resin

def show_error_and_exit(message, show_usage=False):
    sys.stdout.write(message + "\n")
    if show_usage:
        parser.print_help()
    exit()

## {{{ http://code.activestate.com/recipes/577058/ (r2)
def query_yes_no(question, default="no"):
        """Ask a yes/no question via raw_input() and return their answer.

        "question" is a string that is presented to the user.
        "default" is the presumed answer if the user just hits <Enter>.
                It must be "yes" (the default), "no" or None (meaning
                an answer is required of the user).

        The "answer" return value is one of "yes" or "no".
        """
        valid = {"yes":"yes",   "y":"yes",      "ye":"yes",
                         "no":"no",             "n":"no"}
        if default == None:
                prompt = " [y/n] "
        elif default == "yes":
                prompt = " [Y/n] "
        elif default == "no":
                prompt = " [y/N] "
        else:
                raise ValueError("invalid default answer: '%s'" % default)

        while 1:
                sys.stdout.write(question + prompt)
                choice = raw_input().lower()
                if default is not None and choice == '':
                        return default
                elif choice in valid.keys():
                        return valid[choice]
                else:
                        sys.stdout.write("Please respond with 'yes' or 'no' "\
                                                         "(or 'y' or 'n').\n")
## end of http://code.activestate.com/recipes/577058/ }}}

resin = Resin()

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--username', help='Resin username (email)')
parser.add_argument('-p', '--password', help='Resin password')
parser.add_argument('-ra', '--resin-application', help='Resin application to update')
parser.add_argument('-co', '--commit', help='Optional. The commit that the devices will be updated to. If present, it will not try to update the devices that are already in that commit.')
parser.add_argument('-d', '--device', help='UUID of the device to update. You can use this option to update only one device instead of --resin-application which updates all the devices from an application.')

args = vars(parser.parse_args())

if not 'username' in args or args['username'] == None:
	show_error_and_exit("Missing Resin username parameter", True)
if not 'password' in args or args['password'] == None:
	show_error_and_exit("Missing Resin password parameter", True)
# Either the application or a device must be supplied, to know to which device(s) to apply the update: 
if not 'resin_application' in args or args['resin_application'] == None:
    if not 'device' in args or args['device'] == None:
        show_error_and_exit("Missing Resin application or device parameter, enter one of the two.", True)
# But both device AND application should not be supplied:
if 'device' in args and args['device'] != None and 'resin_application' in args and args['resin_application'] != None:
    show_error_and_exit("Please select either an application or a device, not both.", True)

update_commit = None
if 'commit' in args and args['commit'] != None:
    update_commit = args['commit']


credentials = { 'username': args['username'], 'password':args['password']}

# TODO show informative error when authentication fails
try:
    resin.auth.login(**credentials)
except exceptions.RequestError:
	show_error_and_exit("Authentication with Resin failed")

print "Application: {0}".format(args['resin_application'])

if args['resin_application']:
    # get the devices only for the application we are interested in (e.g. ZENSIEmotherBBB)
    devices = resin.models.device.get_all_by_application(args['resin_application'])
else:
    # get the device by uuid:
    devices = [ resin.models.device.get(args['device']) ]

print "Found {0} devices".format(len(devices))

# For each device,
for device in devices:
    online = False
    if device['is_online'] == True:
        online = True
    print "[{0}]. Online: {1}, commit: {2}".format(device['name'], online, device['commit'])

    # print device

    if online:
        if update_commit != None and device['commit'] == update_commit:
            print "Skipping device, it is already at commit {0}".format(update_commit)
        else:
             # ask user if she wants to update it
            if query_yes_no("Do you want to update the device [{0}]".format(device['name'])) == "yes":
                resin.models.supervisor.update(device['uuid'], device['application']['__id'], force=True)

    else:
        print "Skipping device, it's offline."

# Iterate over the list of devices
