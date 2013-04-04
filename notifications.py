#!/usr/bin/env python

class Notifications:
	"""Class for showing standard notifications using the standard color scheme to the command line

	Semantic actions suuported:
		<use>	<function>	<meaning>
		info	inform		showing relevant information to the user
		success	preen		Indicates a successful or positive action
		warning	warn		Indicates caution should be taken with this action
		danger	alarm		Indicates a dangerous or potentially negative action
	Other notifications:
		<function>		<meaning>
		print_standard_error	show an error with a standard message and return code
	"""
	INFO = '\033[94m'
	SUCCESS = '\033[92m'
	WARNING = '\033[93m'
	ERROR = '\033[91m'
	DEFAULT = '\033[0m'


	@staticmethod
	def printc(color_code, message):
		print color_code + message + Notifications.DEFAULT


	@staticmethod
	def warn(message):
		Notifications.printc(Notifications.WARNING, message)


	@staticmethod
	def inform(message):
		Notifications.printc(Notifications.INFO, message)


	@staticmethod
	def alarm(message):
		Notifications.printc(Notifications.ERROR, message)


	@staticmethod
	def preen(message):
		Notifications.printc(Notifications.SUCCESS, message)


	@staticmethod
	def print_standard_error(return_code):
		Notifications.alarm('An error occurred. Return code: ' + str(return_code))

