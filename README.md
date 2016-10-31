# resin-utils
Utilities for working with Resin.io

## resin_devices_update

Update the devices in an application (or a particular device).

The script will prompt for each device in the application which is online if it should be updated or not. It overrides the device lock (/data/resin-updates.lock).

```bash
$ python resin_devices_update.py --help
usage: resin_devices_update.py [-h] [-u USERNAME] [-p PASSWORD]
                               [-ra RESIN_APPLICATION] [-co COMMIT]
                               [-d DEVICE]

optional arguments:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        Resin username (email)
  -p PASSWORD, --password PASSWORD
                        Resin password
  -ra RESIN_APPLICATION, --resin-application RESIN_APPLICATION
                        Resin application to update
  -co COMMIT, --commit COMMIT
                        Optional. The commit that the devices will be updated
                        to. If present, it will not try to update the devices
                        that are already in that commit.
  -d DEVICE, --device DEVICE
                        UUID of the device to update. You can use this option
                        to update only one device instead of --resin-
                        application which updates all the devices from an
                        application.

```
