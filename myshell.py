#Shelloon by Connell Kelly
#Language: Python 3.7.0

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

def override(body, args):
	"""Overwrites file with info or creates file containing input.\n"""
	with open(args[0], "w+") as args:
		for i in body:
			#Writes data to file.
			args.write(i)
			#Adds newline character to end of file.
			args.write("\n")

def attach(body, args):
	"""Appends input to file or creates file containing input.\n"""
	with open(args[0], "a+") as args:
		for i in body:
			args.write(i)
			args.write("\n")

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
					overwrite(subprocess.Popen(proclist[:i]), proclist[i+1:])
				elif proclist[i] == ">>":
					#Append output.
					append(subprocess.Popen(proclist[:i], proclist[i+1]))
				else:
					#Otherwise, look to ampersand.
					subprocess.Popen(proclist[:-1])
		else:
			#If ampersand is not present.
			subprocess.run(proclist)

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
