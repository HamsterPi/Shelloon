shelloon V1.0 by connell kelly
this is a simple shell built upon python 3.5.2

legend:
:~$ - indicates usage.
<> - undetermined command, directory or input.
e.g. - example of command or concept in use.
> - overwrite file.
>> - add to file.
/ - or.
<none> - empty value or string.

execution:
	- execute shell.
	  :~$ python3 myshell.py
	- execute batch file using shell.
	  :~$ python3 myshell.py <filename>


user commands:
	- change current directory location to directory requested.
	  :~$ cd <directory>
	  e.g. cd documents
	- clear command prompt of all text present.
	  :~$ clr
	- list contents of current directory in use.
	  :~$ dir
	- list contents of specified directory.
	  :~$ dir <directory>
	  e.g. dir documents
	- list all environment strings present within the physical setting of the program.
	  :~$ environ
	- output a string input onto display.
	  :~$ echo <input>
	  e.g. echo lorem ipsum
	- open user manual within shell.
	  :~$ help
	- pause shell until "enter" is pressed.
	  :~$ pause
	- quit shell.
	  :~$ quit

external functions:
	- overwrite part of a file with output of command.
	  override(inp, file)
	  e.g. override(keyval, elist[1:])
	- append result of a command to chosen file.
	  attach(inp, file)
	  e.g. attach(keyval, elist[1:])
	- finds data in directory and returns as a string.
	  dir_str(direc=None)
	  e.g. dir_str(datalist[0])

subproccesses:
	subproccesses allow for improved usage of program resources. they allow the user to specify child and background processes at will which can run concurrently with other processes.
	
	- if the shell attempts to execute a function that is not built-in, it will still be executed, but as a child process.
	  :~$ <non-built-in command> 
	  e.g. :~$ python3	
	- if the shell attmepts to execute a function, but with the process being forked and returning to prompt after execution.
	  :~$ <command> &
	  e.g. :~$ python3 &
	
i/o redirection:
	with this functionality, the user can effectively obtain or write something on the prompt using a command and place the result in a specific external file e.g. txt file.
	- redirect contents of directory to a file.
	  :~$ dir <none>/<directory> >/>> <filename>
	  e.g. dir documents > lorem.txt
	- redirect list of environment strings to a file.
	  :~$ environ >/>> <filename>
	  e.g. environ >> ipsum.txt
	- redirect string input to a file.
	  :~$ echo <input> >/>> <filename>
	  e.g. echo mouse > cheese.txt

references:
pymotw was used to gain further understanding of cmd fundamentals
link to site: https://pymotw.com/2/cmd/?fbclid=IwAR3OxcEZBOzC2pZO_PwHHt_tpDA4OgMZTRXx3FT25KZVwwCiiry_R9CXNh8
