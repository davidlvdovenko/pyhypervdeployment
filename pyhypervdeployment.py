# Outside Imports
import csv
import os
import psutil

# Import Self
import pyhypervdeployment as phhydeploy

# Call Script
if __name__ == "__main__":
    phhydeploy.deploy()

# Start of Script
def deploy():

    phhydeploy.checkDependencies()
    phhydeploy.getVMs()

def checkDependencies():

    # Check if required services are running
    servicesList = ["vmms","vmcompute"]

    for serviceitem in servicesList:
        service = get_service(serviceitem)
        if service:
            print("Service found: "+serviceitem)
        else:
            print("Service not found: "+serviceitem+"... Exiting Program")
            exit()

        if service and service['status'] == 'running':
            print("Service is running")
        else:
            print("Service is not running: "+serviceitem+"... Please make sure services is running and try again")
            exit()

def getVMs():

    # Import CSV File and Assign variables to VM

    os.system("powershell Import-Module Microsoft.PowerShell.Utility")

    with open('vm.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for rownumber,row in enumerate(csvreader):
            if rownumber == 0:
                # Skip the header row
                continue;
            else:
                # Assigns variables to each parsed row
                VMName = row[0]
                Path = row [1]
                Generation = row[2]
                Memory = row[3]
                Storage = row[4]
                StorageType = row[5]
                Switch = row[6]
                BootDevice = row[7]
                Image = row[8]
                AutoStart = row[9]

                VMPath = Path+"\\"
                VHDPath = Path+"\\"+VMName+".vhdx"

                # Create VHD
                os.system("powershell New-VHD -Path "+VHDPath+" -"+StorageType+" -SizeBytes "+Storage)

                # Create VM Based of Variables
                os.system("powershell New-VM -Name "+VMName+" -Path "+VMPath+" -Generation "+Generation+" -BootDevice "+BootDevice+" -MemoryStartupBytes "+Memory+" -SwitchName "+Switch)

                # Attaches VHD to VM
                os.system("powershell Add-VMHardDiskDrive -VMName "+VMName+" -Path "+VHDPath)

                # If boot from CD, attach the image to VM
                if BootDevice == "CD":
                    os.system("powershell Set-VMDvdDrive -VMName "+VMName+" -Path .\\"+Image)

                # If AutoStart = True, turn on VM
                if AutoStart == "TRUE":
                    os.system("powershell Start-VM -Name "+VMName)


# Credit: https://stackoverflow.com/questions/33843024/check-if-a-windows-service-exists-with-python
def get_service(name):
    service = None
    try:
        service = psutil.win_service_get(name)
        service = service.as_dict()
    except Exception as ex:
        print(str(ex))
    return service