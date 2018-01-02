<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [resin-utils](#resin-utils)
  - [Running with docker](#running-with-docker)
  - [Running Locally](#running-locally)
    - [Requirements](#requirements)
- [Usage](#usage)
  - [Login](#login)
  - [Update procedure](#update-procedure)
    - [Step 1: Stop auto updating](#step-1-stop-auto-updating)
    - [Step 2: Fix build version](#step-2-fix-build-version)
    - [Step 3: Set a base commit](#step-3-set-a-base-commit)
    - [Step 4: Start updating](#step-4-start-updating)
  - [Menu](#menu)
    - [Get device list (UUID)](#get-device-list-uuid)
    - [Check device details (UUID)](#check-device-details-uuid)
    - [Update one device](#update-one-device)
    - [Update an entire application (One by one)](#update-an-entire-application-one-by-one)
    - [Check application settings](#check-application-settings)
    - [Switch rolling updates](#switch-rolling-updates)
    - [Set base commit application](#set-base-commit-application)
    - [Logout](#logout)
    - [Quit](#quit)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

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
Make sure you meet de following requirements:

Pyhton 2 is installed

#### Resin CLI
Install resin cli with 

```
pip install git+https://github.com/resin-io/resin-sdk-python.git@v1.6.3
``` 

or 

```
pip2 install git+https://github.com/resin-io/resin-sdk-python.git@v1.6.3
```

#### readchar

```pip install readchar``` or ```pip2 install readchar```

# Usage

## Login

If not already logged in the Resin python SDK, the script prompts for you authentication token.

```
You need to login, please enter your authentication token.
https://dashboard.resin.io/preferences/details
Token:

```


## Update procedure
Follow this procedure to make sure each device updates to the version you want.

### Step 1: Stop auto updating
Resin will alway's try to update all devices to the latest softwarepush. If not disabled the default application will always equel the latest push.

To stop this toggle the `rolling updates` to `false` with `Switch rolling updates` and current states of rolling update can be checked with `Check application settings`

### Step 2: Fix build version
Make sure that all devices have a (or current) build fixed in there registers. Default is `None`.
This can be done by running `Update an entire application (One by one)` with a version until all have a value set.

### Step 3: Set a base commit
Setting a base commit on the application can change the version new devices start with, since there build register will contain `None`.

### Step 4: Start updating
Update all devices accordingly, using update either one device or an entire application

## Menu

```
1 Get device list (UUID)
2 Check device details (UUID)
3 Update one device
4 Update an entire application (One by one)
5 Check application settings
6 Switch rolling updates
7 Set base commit application
9 Logout
0 Quit

Run:  
```

Press the corresponding number of the function you want to run.

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
With an UUID (retrieved with above function) all details of this particulair device can be shown.

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
Pick a build hash of the successfull builds, from either the Dashboard or this list.

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

Same as the above, but then for a whole application. The script will prompt for each device in the application which is online if it should be updated or not. It overrides the device lock (/data/resin-updates.lock).

```
Select Application to check settings:

ID	NAME
306681	NewMother

Please enter application ID:
```


```
Application name:	NewMother
Application ID:		306681
URL:			https://dashboard.resin.io/apps/306681/devices

Rolling updates enabled: True

Default software:	 b91b6e267eada7de9c2f67b27e6db6bc44202fds
Push data:		 2017-12-06T11:48:02.375Z
Build id:		 734928

Available build options:
[Hash]						[Timestamp]			[ID]
b91b6e267eada7de9c2f67b27e6db6bc44202fds	2017-12-06T11:48:02.375Z	734928
df1a0ff51d4ac0d34f1bf94cb48d83de67b27f32	2017-12-06T11:33:58.442Z	728363
5b6751ef1bf94cb48d83defa8dbf0ef1ada7de97	2017-11-28T19:21:12.860Z	716739
1f55e6261fc3ce3df1a0ff51d4ac0d349c2f67bd	2017-11-28T14:24:08.209Z	707345

Enter hash to set:
```

```
Application: 306681
Build: 734928
Hash: b91b6e267eada7de9c2f67b27e6db6bc44202fds
Devices found: 4
```

For each device that is online, it can be decided to update or not.

```
[New mother demo]
Do you want to update the device? [Y/n]
```

If the device is online but no build is set you can only set it to current version. Run the program again to update it. 
```
[bluecasing Resin 2] is online but no build is set. 
Set current software version as fixed build? [Y/n] 

OK
Device now set to commit b91b6e267eada7de9c2f67b27e6db6bc44202fds

```

If a device is offline it will be skipped:
```
[quiet-mountain] is offline.
Skipping device
```

If the particulair build is already set, it will be skipped too:
```
[misty-breeze]
Skipping device, it is already at commit b91b6e267eada7de9c2f67b27e6db6bc44202fds
```

When a device is offline and no build is set. It is still important to set a build. Therefore current software can be set as build:

```
[lingering-sunset] is offline.
And there is not build set. Set current software version as fixed build? [Y/n]
```

### Check application settings
```
Select Application to check settings:

ID	NAME
306681	NewMother

Please enter application ID:
```
```
Application name:	NewMother
Application ID:		306681
URL:			https://dashboard.resin.io/apps/306681/devices

Rolling updates enabled: True

Default software:	 b91b6e267eada7de9c2f67b27e6db6bc44202fds
Push data:		 2017-12-06T11:48:02.375Z
Build id:		 734928
Press a key to continue.
```

### Switch rolling updates

```
Select Application to check settings:

ID	NAME
306681	NewMother

Please enter application ID:
```
```
Application name:	NewMother
Application ID:		306681
URL:			https://dashboard.resin.io/apps/306681/devices

Rolling updates enabled: True

Default software:	 b91b6e267eada7de9c2f67b27e6db6bc44202fds
Push data:		 2017-12-06T11:48:02.375Z
Build id:		 734928

Do you want to disable rolling updates? [Y/n]
```
```
Disabling
OK
Press a key to continue.
```

### Set base commit application
```
Select Application to check settings:

ID	NAME
306681	NewMother

Please enter application ID:
```


```
Application name:	NewMother
Application ID:		306681
URL:			https://dashboard.resin.io/apps/306681/devices

Rolling updates enabled: True

Default software:	 b91b6e267eada7de9c2f67b27e6db6bc44202fds
Push data:		 2017-12-06T11:48:02.375Z
Build id:		 734928

Available build options:
[Hash]						[Timestamp]			[ID]
b91b6e267eada7de9c2f67b27e6db6bc44202fds	2017-12-06T11:48:02.375Z	734928
df1a0ff51d4ac0d34f1bf94cb48d83de67b27f32	2017-12-06T11:33:58.442Z	728363
5b6751ef1bf94cb48d83defa8dbf0ef1ada7de97	2017-11-28T19:21:12.860Z	716739
1f55e6261fc3ce3df1a0ff51d4ac0d349c2f67bd	2017-11-28T14:24:08.209Z	707345

Enter build Hash:
```
```
OK

Application name:	NewMother
Application ID:		306681
URL:			https://dashboard.resin.io/apps/306681/devices

Rolling updates enabled: True

Default software:	 b91b6e267eada7de9c2f67b27e6db6bc44202fds
Push data:		 2017-12-06T11:48:02.375Z
Build id:		 734928

Default commit changed!
Press a key to continue.
```

### Logout
You don't have to logout this script. But for changing account, a logout is needed.

### Quit
Cleanly quit the program
