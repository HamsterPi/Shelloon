#Shelloon by Connell Kelly (Student Number: 17480902)
#Language: Python 3.5.2
#I hope the cowboy theme doesn't sour your milk.
#My thanks for a good semester.

#Relevant modules.
from cmd import Cmd
import getpass
import os
import pathlib
import platform
import readline
import socket
import subprocess
import sys

#External functions for use in main class.
def attach(inp, file):
	"""Appends input to file or creates file containing input.\n"""
	with open(file[0], "a+") as j:
		for i in inp:
			#Writes data to file.
			j.write(i)
			#Adds newline character to end of file.
			j.write("\n")

def override(inp, file):
	"""Overwrites file with input or creates file containing input.\n"""
	with open(file[0], "w+") as j:
		for i in inp:
			j.write(i)
			j.write("\n")

#Shell class and functions.
class Shelloon(Cmd):
	def default(self, args):
		"""Changes to subprocess if using undefined function.\n"""
		proclist = args.split()
		if proclist[-1] == "&":
			#Prepares each as a background process.
			for i in range(0, len(proclist[:-1])):
				if proclist[i] == ">":
					#Overwrite output.
					override(subprocess.Popen(proclist[:i]), proclist[i+1:])
				elif proclist[i] == ">>":
					#Append output.
					attach(subprocess.Popen(proclist[:i], proclist[i+1]))
				else:
					#Otherwise, look to ampersand.
					subprocess.Popen(proclist[:-1])
		else:
			#If ampersand is not present.
			subprocess.run(proclist)

	def do_cd(self, args):
		"""Changes current default directory to directory requested. If it doesn't exist, report current directory.\n"""
		try:
			#If input is empty, move on.
			if len(args) == 0:
				pass
			#Otherwise, OS changes directory.
			else:
				os.chdir(args)
				#Prompt reflects this change.
				self.prompt = "shell=" + os.getcwd() + ':$ '
		#If the directoru cannot be found.
		except FileNotFoundError:
			print("That there directory don't exist, partner.")

	def do_clr(self, args):
		"""Will clear the command prompt of all text.\n"""
		os.system('clear')

	def do_dir(self, args):
		"""Lists current directories in use.\n"""
		flag = False
		#If user doesn't specify a directory, use current one.
		if args == "":
			#Observe each item in directory and print it.
			for i in os.listdir():
				#This directory is not empty.
				flag = True
				print(i)
			#Determines if directory is empty.
			if flag == False:
				print("This here directory is bone-dry.")
		#Otherwise, move on to specified directory.
		else:
			#Observe each item in the specified directory and print it.
			for i in os.listdir(args):
				flag = True
				print(i)
			if flag == 0:
				print("This here directory is bone-dry.")

	def do_environ(self, args):
		"""Lists all environment strings.\n"""
		#List of environment strings.
		elist = []
		#For each item in the OS environment.
		for i in os.environ:
			#If it is empty, add "NULL" to it's respective postion in the list.
			if os.environ[i] == "":
				elist.append(i + "=NULL")
			#Otherwise, append the environment key and value to the list.
			else:
				elist.append(i + "=" + os.environ[i])
		#Join and print the final list elements and add newline for each.
		print("\n".join(elist) + "\n")

	def do_echo(self, args):
		"""Outputs args onto display with newline.\n"""
		print(str(args + "\n"))

	def do_pause(self, arg):
		"""Pauses shell until 'Enter' is pressed.\n"""
		pause = input()

	def do_quit(self, args):
		"""Quits the program."""
		print("Happy trails!\nQuitting prompt...")
		raise SystemExit

def batch_file():
	"""Identifies and reads commands from a text file."""
	try:
		#Read batch file as args.
		with open(sys.argv[1], 'r') as args:
			shell = Shelloon()
			#Collect commands.
			commandlines = args.readlines()
			#Allows prompt to end after txt commands.
			commandlines.append('quit')
			#Queue all batch file commands.
			shell.cmdqueue = commandlines
			#Loop through each command and end.
			shell.cmdloop()
	except IndexError:
			#If there's no file, move on to prompt.
			pass

if __name__ == "__main__":
	#Call function and check if batch file is present.
	batch_file()
	#Determine whether or not prompt is on Windows or Linux.
	if platform.system() == "Windows":
		prompt = Shelloon()
		prompt.prompt = os.getcwd() + '>'
		prompt.cmdloop("Starting prompt...\nHowdy, welcome to the Shelloon!\n(Type 'help' for a list of commands.)")
	elif platform.system() == "Linux":
		user = getpass.getuser()
		host = socket.gethostname()
		prompt = Shelloon()
		prompt.prompt = user + "@" + host + "\nshell=" + os.getcwd() + ":~$ "
		prompt.cmdloop("Starting prompt...\nHowdy, welcome to the Shelloon!\n(Type 'help' for a list of commands.)\n")
	#Otherwise, it cannot be supported.
	else:
		pass