#!/usr/bin/env python

import argparse
import signal
import sys
import os.path

from notifications import *

def ctrl_c(signal, frame):
	sys.exit(1)

def handle_key_interrupt():
	signal.signal(signal.SIGINT, ctrl_c)
handle_key_interrupt()

def printDebug(args, message):
	if args.debug:
		print(' '.join(['DEBUG:', str(message)]))

def prompt(message='Do you want to continue?'):
	"""Show a yes-no prompt to the user.

	If choice is neither 'yes', 'y' nor <Enter>, script will exit
	Parameter
		message str	an optional parameter for specifying the question
	"""
	if prompt:
		yes = set(['yes', 'y', ''])
		Notifications.warn(message)
		choice = raw_input('[Y/n]: ').lower()
		if choice not in yes:
			Notifications.inform('Exiting now.')
			sys.exit(0)

