# Hyper-V VM Automatic Deploy Script
A simple python script to deploy a lot of VMs to Hyper-V using a CSV spreadsheet...

To learn more visit: https://davidlvdovenko.com/hyper-v-vm-automatic-deployment-script/

## Introduction
Prerequisites: Hyper-V Role installed on either Windows 10 Pro or Windows Server. Must also have Powershell Version 3 or higher. If you would like to use the decompiled version of the script, it requires Python3 and psutils to be installed. Want to use an ISO image for the VMs, you will need to have that downloaded for this…

So, let’s say that you have a Hyper-V environment setup and you need to deploy, for example, 50 virtual machines. Ughh – now you have to sit through that GUI 50 times and manually name and set up each virtual machine. It hurts just thinking about it. Well, fear not, I have a solution for you. My python script takes a .CSV spreadsheet and passes it through to create VMs based on the .CSV file on the server. 


## Install
This is very straightforward. You only need a Hyper-V server running either on Windows 10 or Windows Server. The services related to Hyper-V must also be active otherwise the script will error out. You must also have administrative privileges to the Hyper-V Machine. The only way to run this script is using the terminal with elevated privileges on that machine. You can either use “Command Prompt” or “Powershell”. To begin please download the files that you can find in my Github Repo:

https://github.com/davidlvdovenko/pyhypervdeployment

You may now begin to extract the contents of the repository. In the repository, you will find a couple of files. Here are the most important ones:

pyhypervdeploymeny.py | Source code – use this if you want to change or modify any parts of the script.
vm.csv | This is an example of the CSV file. I will explain more about how to use the file below.
\build\pyhypervdeployment.exe | This is the compiled version of the script. Use this if you don’t need any modifications.

You may choose to either use the .py file or the .exe. This is simply a matter of preference and whether or not you want to install the dependencies.

## Configuration
Go ahead and place your files in the directory you wish to run the script from… Make sure that if you are booting off an ISO image(s), you have that in the same directory as the script. Make sure your vm.csv file is also in the same directory (NOTE: the file must be named ‘vm.csv’, otherwise this will not work). Now you are ready to set up the vm.csv file. Below is an example of one.

 Name  	Path	Generation	Memory	Storage	Storage Type	Switch	Boot	Image	AutoStart
VM1	C:\VMs	1	4GB	25GB	Fixed	NewSwitch	CD	image.iso	TRUE
VM2	C:\VMs	1	3GB	20GB	Dynamic	NewSwitch	CD	image.iso	FALSE
NOTE: THE HEADER/TITLES IN THE ‘VM.CSV’ FILE MUST STAY THERE. THE SCRIPT AUTOMATICALLY STRIPS THE HEADER…

Every row in the .CSV file corresponds to a VM. You can theoretically have as many rows as you want in this file. Every column has to be filled in in order to work unless otherwise stated… In the example file above we see that there are 2 VMS to be made by the script. All settings are pretty self-explanatory here. Only the ‘STORAGE TYPE’ , ‘BOOT’ , ‘IMAGE’  and ‘AUTOSTART’ options need to be explained.

STORAGE TYPE: ‘Static’, ‘Dynamic’, ‘Differencing’ (This depends on what kind of disk you want. You can learn more about the different kinds of Virtual Hard Disks here: https://www.faqforge.com/windows/fixed-dynamically-expanding-differencing-disk-hyper-v/)
BOOT: ‘IDE’, ‘CD’ (Depends on whether you want to boot from the Virtual HD or an ISO Image)
IMAGE: Set this to whatever you named your ISO file in the script directory. Make sure to include the ‘.ISO’ in the CSV file.
AUTOSTART: Set this to TRUE if you would like the VM to boot as soon as it is created. Set to false otherwise.
04
Section IV
Run the Script
You are now ready to run the script. Open your terminal with elevated permissions in the directory where the script is located along with all the other files. If you are running the executable, simply run the following command:

.\pyhypervdeployment.exe

The script will take over and this point and begin the process of creating your VMs. You can have your Hyper-V Manager open and see as all the new VMs pop up. And that it – It’s simple as that! If you would like a closer look at the source code – head over to my Github Repo – all of it is commented, so it should be easy to read…
