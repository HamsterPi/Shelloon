#Shelloon by Connell Kelly (Student Number: 17480902)
#Language: Python 3.5.2
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

def dir_str(direc=None):
	"""Finds data in directory and returns as a string.\n"""
	#For specified directory.
	if direc != None:
		#Returns string of specified directory data.
		return "\n".join([i for i in os.listdir(direc)])
	#For unspecified directory.
	else:
		#Returns string of current directory data.
		return '\n'.join([i for i in os.listdir(os.getcwd())])

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
		os.system("clear")

	def do_dir(self, args):
		"""Lists current directories in use.\n"""
		#Converts command-line arguments to a list.
		args = args.split()
		try:
			#For standard input.
			if args[0] == "<":
				#Open inputted file as a directory.
				with open(args[1], "r") as i:
					#Creates list of all lines in specified file.
					datalist = [args.strip() for args in i.readlines()]
				#For overwrite redirection.
				if args[2] == ">":
					#Overwrite data in specified file.
					override(dir_str(datalist[0]), args[3:])
				#For add redirection.
				elif args[2] == ">>":
					#Add data to specified file.
					attach(dir_str(datalist[0]), args[3:])
				else:
					#For non-redirection, print data from directory.
					print(dir_str(datalist[0]))
			elif args[1] == ">":
				#Overwrites to specified file.
				override(dir_str(args[0]), args[2:])
			elif args[1] == ">>":
				#Adds to specified file.
				attach(dir_str(args[0]), args[2:])
			elif args[0] == ">":
				#Overwriting without specified directory.
				override([dir_str()], args[1:])
			elif args[0] == ">>":
				#Adding without specified directory.
				attach([dir_str()], args[1:])
			else:
				#Prints data from specified directory.
				print(dir_str(args[0]))
		except IndexError:
			#Prints data from current directory.
			print(dir_str())

	def do_environ(self, args):
		"""Lists all environment strings.\n"""
		#Converts args to a list.
		elist = args.split()
		try:
			#For I/O redirection overwrite.
			if elist[0] == ">":
				#List for environment keys and values.
				keyval = []
				for i in os.environ:
					#If it is empty, add "NULL" to it's respective postion in the list.
					if os.environ[i] == "":
						keyval.append(i + "=NULL")
					#Otherwise, append the environment key and value to the list.
					else:
						keyval.append(i + "=" + os.environ[i])
				#Overwrite environment strings to a specific file.
				override(keyval, elist[1:])
			#For I/O redirection adding.
			elif elist[0] == ">>":
				keyval = []
				for i in os.environ:
					if os.environ[i] == "":
						keyval.append(i + "=NULL")
					else:
						keyval.append(i + "=" + os.environ[i])
				#Add environment strings to a specific file.
				attach(keyval, elist[1:])
		#If there is no I/O redirection, just print environ list.
		except IndexError:
			keyval = []
			for i in os.environ:
				if os.environ[i] == "":
					keyval.append(i + "=NULL")
				else:
					keyval.append(i + "=" + os.environ[i])
			#Print joined list of of environment keys and values.
			print("\n".join(keyval))

	def do_echo(self, args):
		"""Outputs args onto display with newline.\n"""
		#Puts arguments into a list.
		alist = args.split()
		#Counter for determining input positioning.
		counter = 0
		#List containing echo inputs.
		inplist = []
		#For each item from the start to the end of the argument list.
		for i in range(0, len(alist)):
			#For I/O redirection overwrite.
			if alist[i] == ">":
				#Joins arguments to a string.
				ewords = " ".join(inplist)
				#Overrites string to specified file.
				override([ewords], alist[i+1:])
				break
			#For I/O redirection adding.
			elif alist[i] == ">>":
				#Joins arguments to a string.
				ewords = " ".join(inplist)
				#Adds string to specified file.
				attach([ewords], alist[i+1:])
				break
			else:
				#Adds non-redirection arguements to a list.
				inplist.append(alist[i])
				#Add to counter to specify positioning.
				counter += 1
		#Once loop has been broken, determine if function has reached list limit.
		if counter == len(alist):
			#Print the argument lists as strings.
			print(" ".join(inplist))

	def do_help(self, args):
		"""Displays user manual.\n"""
		#Set the manual file to the "man" variable.
		with open("readme.md", "r") as man:
			#Print each line in the user manual.
			for line in man.readlines():
				print(line)
		
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
			commandlines.append("quit")
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
