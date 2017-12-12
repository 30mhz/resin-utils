#!/usr/bin/env python

from resin import Resin
from os import system

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
