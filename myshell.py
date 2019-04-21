#Shelloon - Connell Kelly
#Language: Python 3.7
#I hope the cowboy theme don't sour your milk.
#My thanks for a good semester.

#Relevant modules.
from cmd import Cmd
import getpass
import os
import pathlib
import platform
import readline
import socket
import sys

#Shell class and functions.
class Shelloon(Cmd):
	def do_cd(self, args):
		"""Changes current default directory to directory requested. If it doesn't exist, report current directory.\n"""
		try:
			if len(args)==0:
				#print(os.getcdw())
				pass
			else:
				os.chdir(args)
				self.prompt = "shell=" + os.getcwd() + ':$ '
		except FileNotFoundError:
			print("That there directory don't exist, partner.")

	def do_clr(self, args):
		"""Will clear the command prompt of all text.\n"""
		os.system('clear')

	def do_dir(self, args):
		"""Lists current directories in use.\n"""
		count = 0
		if args == "":
			for i in os.listdir():
				count += 1
				print(i)
			if count == 0:
				print("This here directory is bone-dry.")
		else:
			for i in os.listdir(args):
				count += 1
				print(i)
			if count == 0:
				print("This here directory is bone-dry.")

	def do_environ(self, args):
		"""Lists all environment strings.\n"""
		elist = []
		for k in os.environ:
			if os.environ[k] == "":
				elist.append(k + "=NULL")
			else:
				elist.append(k + "=" + os.environ[k])
		print("\n".join(elist) + "\n")

	def do_echo(self, args):
		"""Outputs args onto display with new line.\n"""
		print(str(args + "\n"))

	def do_pause(self, arg):
		"""Pauses shell until 'Enter' is pressed.\n"""
		pause = input()

	def do_quit(self, args):
		"""Quits the program."""
		print("So long, regular cowboy.")
		raise SystemExit

def batch_file():
	"""Identifies and reads commands from a text file."""
	try:
		with open(sys.argv[1], 'r') as args:
			shell = Shelloon()
			commandlines = args.readlines() 
			commandlines.append('quit')
			shell.cmdqueue = commandlines
			shell.cmdloop()
	except IndexError:
			pass

if __name__ == "__main__":
	batch_file()

	if platform.system() == "Windows":
		prompt = Shelloon()
		prompt.prompt = os.getcwd() + '>'
		prompt.cmdloop("Starting prompt...\nHowdy, welcome to the Shelloon!\n(Type 'help' for a list of commands.)")

	elif platform.system() == "Linux":
		user = getpass.getuser()
		host = socket.gethostname() #need to get colours

		prompt = Shelloon()
		prompt.prompt = user + "@" + host + "\nshell=" + os.getcwd() + ":~$ "
		prompt.cmdloop("Starting prompt...\nHowdy, welcome to the Shelloon!\n(Type 'help' for a list of commands.)\n")
	else:
		pass
