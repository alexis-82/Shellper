import os
import getpass
import time
import subprocess
import random
import sys
version = str("1.0 - build: 01 dec 2016")
os.system("clear")
#WIFI
def SECURE(command):
   lock_status = True
   sec_confirm_code = random.randint(1500, 7000)
   sec_confirm_input = raw_input("Type the following code: " + str(sec_confirm_code) + " :")
   if str(sec_confirm_input) == str(sec_confirm_code):
   	 lock_status = False
   if lock_status == False:
   	 exec str(command)
   else:
   	 print("The lock status is: ACTIVE")

def NETWORK_WiFi():
	os.system("iwlist wlp2s0 scan")
	chosen_network = raw_input("What network do you want to connect? ")
	network_password = raw_input("Password: ")
	os.system("iwconfig wlp2s0 "+ chosen_network +" "+"s:"+ network_password)
	print("Connecting to " + chosen_network)
	os.system("dhclient wlp2s0")

def NETWORK():
 raw_input("Activate network(1), disable it(2) or next step(3)?: ")
 if str(raw_input) == '1':
  os.system("ifconfig wlan0 up")
  os.system("ifconfig wlp2s0 up")
  print("Network is now working")
  NETWORK_wifi()
 if str(raw_input) == '2':
  os.system("ifconfig wlan0 down")
  os.system("ifconfig wlp2s0 down")
  print("Network is now off")
 if str(raw_input) == '3':
  print("Okay")
  NETWORK_wifi()
 else:
  print("Error: invalid input") #BUG

#MOUNT
def MOUNT():
	os.system("sudo echo Root confirmed")
	os.system("lsblk -o KNAME,TYPE,SIZE,MODEL")
	mount_name = raw_input("Type name of the device you want to mount (es. sdb1): ")
	mount_folder = raw_input("""Now type the folder where you want to mount the device, with the full path. (es. /home/me/foldername)
	   Also, if folder does not exist, it will be created in your home folder: """)
	if os.path.isdir(mount_folder) == True:
		def MOUNT_active():
			mounter = str("sudo mount /dev/"+ mount_name + " " + mount_folder)
			mount_proc = subprocess.Popen(mounter, shell=True)
			time.sleep(1)
			mount_proc.terminate()
		MOUNT_active()
	if os.path.isdir(mount_folder) == False:
	   os.system ("mkdir /home/$USER"+mount_name)
	   def MOUNT_active_2():
		    mounter_2 = str("sudo mount /dev"+ mount_name + " " + "/home/$USER" + mount_name)
		    mount_proc_2 = subprocess.Popen(mounter_2, shell=True)
		    time.sleep(1)
		    mount_proc_2.terminate()
	   MOUNT_active_2()

#INSTALL\UNINSTALL
def UNIN():
    input_choice_unin = raw_input("Do you want to install (1) o or unistall (2)?")
    if input_choice_unin == "1":
      input_choice_unin_prog_in = raw_input("Type names of the packages you wnat to install: ")
      os.system("sudo apt-get install"+ " "+ input_choice_unin_prog_in)
    elif input_choice_unin == "2":
     print("List of the installed packets")
     time.sleep(2)
     os.system("dpkg -l")
     time.sleep(2)
     input_choice_unin_prog_un = raw_input("Type the packets you want to unistall: ")
     os.system("sudo apt-get remove"+ " "+ input_choice_unin_prog_un)

#killmepls
def SELFDESTR():
    print("""Apparently, you're hunted by policemen, or you hate your datas. Anyway, here's what you can do:
    1) Format the /home folder
    2) Format the /root folder
    3) Format both of them
    4) Format all connected drives in ext3 format
    5) Make all your datas disappear in a BlackHole """)
    self_destr_choice = raw_input("1, 2, 3, 4, 5, or EXIT?")
    if self_destr_choice == "1":
    	SECURE(os.system("sudo rm -rf /home/$USER"))
    if self_destr_choice == "2":
    	SECURE(os.system("sudo rm -rf /"))
    if self_destr_choice == "3":
    	SECURE(os.system("sudo rm -rf /; sudo rm -rf /home/$USER"))
    if self_destr_choice == "4":
    	SECURE(os.system("sudo mkfs.ext3 /dev/sda"))
    if self_destr_choice == "5":
    	print("Sending your files in another dimension with CHASE...")
    	SECURE(os.system("mv folder /dev/null"))

#CREDIT
def CREDITS():
	credits = "Developped by davix3f\n    davide_fiorito@libero.it\n"
	for char in credits:
		time.sleep(0.2)
		sys.stdout.write(char)
		sys.stdout.flush()

#MENU
print version
print("====================\nWelcome to Shellper!\n====================")
print("""        1. Connect to WiFi
	2. Mount a USB or anything else
	3. Install/Uninstall an application
	4. Get the credits
	5. Report a bug (will be implemented in 2.0)
	6. Changelog
	7: Exit :c """)
#menu_choice = raw_input("\nTell me, Sir: ")

menu_choice = raw_input("\nTell me, Sir: ")
if menu_choice == "1":
	NETWORK()
elif menu_choice == "2":
	MOUNT()
elif menu_choice == "3":
	UNIN()
elif menu_choice == "4":
	CREDITS()
elif menu_choice == "5":
	print("Coming soon")
elif menu_choice == "6":
	CHANGELOG()
elif menu_choice == "7":
	os.system("clear")
	exit()
