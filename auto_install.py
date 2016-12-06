import subprocess
from getpass import getuser
import os
from time import sleep
user = getuser()
bin_path = ("/home/"+user+"/bin")

def download():
	os.system("cd /home/$USER/bin; wget https://raw.githubusercontent.com/davix3f/Shellper/master/Shellper.py")

def check_file():
	if os.path.isfile(bin_path+"/Shellper.py") == True:
		print("File dowloaded, proceeding")
	if os.path.isfile(bin_path+"/Shellper.py") == False:
		print("Error: file not present")
		exit()

def bin_true():
    if os.path.isdir(bin_path) == True:
    	print("Already here, good")
    if os.path.isdir(bin_path) == False:
    	mk_bin = ("mkdir /home/"+user+"/bin")
        os.system(mk_bin)


def shortcut_creation():
	bin_creation = ("/home/"+user+"/bin/shelp")
	the_file = open(bin_creation, "w")
	the_file.write("""#!/bin/bash
	python /home/"""+user+"""/bin/Shellper.py
	export PATH=$PATH:~/bin""")
	the_file.close()
	os.system("chmod +x "+bin_creation)
	os.system(". ~/.bashrc")

print("Checking if bin folder is present...")
sleep(1)
bin_true()


print("Downloading the script...")
sleep(1); download()

print("Checking file...")
sleep(1)
check_file()

print("Creating the shortcut file...")
sleep(1)
shortcut_creation()

sleep(2)

print("Now, to activate the program, close the terminal, re-open it, then type: shelp. Hope you'll enjoy it!")
