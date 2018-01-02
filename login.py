#!/usr/bin/env python

"""
Part of update set for Resin used by 30MHz

Resin Python SDK login script.

A: Fokko
E: fokko@30MHz.com
D: 20 Dec 2017
"""


from os import system

# Loading Resin Python SDK
from resin import Resin
resin = Resin()

def login():
	system("clear") # Linux - OSX only :(
	# Check if not already logged in
	if not resin.auth.is_logged_in():

		print ("You need to login, please enter your authentication token.")
		print ("https://dashboard.resin.io/preferences/details")
		auth_token = raw_input("Token: ")

		try:
			resin.auth.login_with_token(auth_token)
		except:
			print ("Login error")
			exit()

	print ("Logged in as %s" % resin.auth.who_am_i())
