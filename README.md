# resin-utils
Utilities for working with rolling updates in combination with Resin.io. Utilizing settings build version and applications that not following the latest commit to Resin.

This script can be run in two way's: With Docker or plain local. 

## Running with docker

To run with docker (make sure docker is started) simply enter:
```
./run.sh
```


## Running Locally

To run it with Python use Python 2.
```
python2 start.py
```

### Requirements
Make shure you meet de following requirements:

Pyhton 2 is installed
Install resin cli with `pip` or `pip2 install git+https://github.com/resin-io/resin-sdk-python.git`
`pip` or `pip2 install readchar`

# Usage

## Login

If not already logged in the Resin python SDK, the script prompts for you authentication token. 

```
You need to login, please enter your authentication token.
https://dashboard.resin.io/preferences/details
Token: 

```

## Menu

```
1 Get device list (UUID)
2 Check device details (UUID)
3 Update one device
4 Update an entire application (One by one)
5 Check application settings
6 Swith rolling updates
7 Set base commit application
9 Logout
0 Quit

Run:  
```

Press the corresponding number the function you want to run. 

### Get device list (UUID)
This function will return all Resin devices with the corresponding UUID sorted on device name:

```
df1a0ff51d4ac0d34f1bf94cb48d83de	lingering-sunset
5b6751ef1bf94cb48d83defa8dbf0ef1	misty-breeze
1f55e6261fc3ce3df1a0ff51d4ac0d34 	quiet-mountain
Press enter to continue
```
This can be used to pick an UUID for checking details on.

Press enter to return to the main menu.

### Check device details (UUID)
With an UUID (retrieved with above function) all details of this perticulair device can be shown.

```
Device name: lingering-sunset
ID: 720567
UUID: df1a0ff51d4ac0d34f1bf94cb48d83de

Is online: False
Last seen: 2017-12-06T13:17:21.198Z
Location: Amsterdam, North Holland, Netherlands

Local IP: None
Public IP: 185.1.150.98

Application: Zensie
Build set: None

Commit: b91b6e267eada7de9c2f67b27e6db6bc4420 
OS: Resin OS 2.0.0+rev2 (prod)
Supervisor: 4.1.1

Created on: 2017-12-06T13:14:48.967Z
```
Important to get to know which build is set. 

### Update one device
With this function it is possible to set a device to a specific commit, either new or old commits. 

```
Enter device UUID to update: 
```

Enter the UUID of the device

```
Device name: New Mother testboard
ID: 720567
UUID: df1a0ff51d4ac0d34f1bf94cb48d83de

Is online: True
Last seen: 2017-12-12T15:17:57.878Z
Location: Amsterdam, North Holland, Netherlands

Local IP: 192.168.8.82
Public IP: 185.1.150.98

Application: NewMother
Build set: 

	Build ID: 	734928 
	Build hash: 	b91b6e267eada7de9c2f67b27e6db6bc44202fds 
	Date: 		2017-11-28T19:21:12.860Z

Commit: b91b6e267eada7de9c2f67b27e6db6bc44202fds
OS: Resin OS 2.7.5+rev2
Supervisor: 6.3.6

Created on: 2017-12-07T11:53:38.348Z

Available build options:
[Hash]						[Timestamp]			[ID]
b91b6e267eada7de9c2f67b27e6db6bc44202fds	2017-12-06T11:48:02.375Z	734928
df1a0ff51d4ac0d34f1bf94cb48d83de67b27f32	2017-12-06T11:33:58.442Z	728363
5b6751ef1bf94cb48d83defa8dbf0ef1ada7de97	2017-11-28T19:21:12.860Z	716739
1f55e6261fc3ce3df1a0ff51d4ac0d349c2f67bd	2017-11-28T14:24:08.209Z	707345

Enter hash to set: 
```
Pick a build hash of the succesfull builds, form either the Dashboard or this list.

```
Setting build:
Device UUID df1a0ff51d4ac0d34f1bf94cb48d83de
In application 306681
To build hash 1f55e6261fc3ce3df1a0ff51d4ac0d349c2f67bd
That is buildnumber 707345
OK
Setting value: Done

Device name: New Mother testboard
ID: 720567
UUID: df1a0ff51d4ac0d34f1bf94cb48d83de

Is online: True
Last seen: 2017-12-12T15:17:57.878Z
Location: Amsterdam, North Holland, Netherlands

Local IP: 192.168.8.82
Public IP: 185.1.150.98

Application: NewMother
Build set: 

	Build ID: 	707345 
	Build hash: 	1f55e6261fc3ce3df1a0ff51d4ac0d349c2f67bd 
	Date: 		2017-11-28T14:24:08.209Z

Commit: b91b6e267eada7de9c2f67b27e6db6bc44202fds
OS: Resin OS 2.7.5+rev2
Supervisor: 6.3.6

Created on: 2017-12-07T11:53:38.348Z



Press a key to continue

```



### Update an entire application (One by one)
### Check application settings
### Swith rolling updates
### Set base commit application
### Logout
### Quit


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
