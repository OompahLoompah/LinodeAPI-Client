from client import linodeClient
import os

linode = linodeClient(os.getcwd() + '/../.config')

userInput = raw_input("What do you want to do?\n")

if userInput == 'create':
    linode.createLinode('3', '1')

if userInput == 'destroy':
    userInput = raw_input("What do you want to destroy?\n")
    linode.destroyLinode(userInput)

if userInput == 'cfd':
    linodeID = raw_input("LinodeID: ")
    distro = raw_input("Distro ID: ")
    label = raw_input("Label: ")
    size = raw_input("Size (MB): ")
    password = raw_input("Password: ")
    print(linode.createFromDistro(linodeID, distro, label, size, password))
    linode.createDisk(linodeID, 'swap', '512', 'swap')
    linode.createConfig(linodeID, label, [label,'swap'])

if userInput == 'config':
    linodeID = raw_input("LinodeID: ")
    label = raw_input("Label: ")

    disks = []
    disk = raw_input("Enter disk ID")
    while disk != '':
        disks.append(disk)
        disk = raw_input("Enter disk ID: ")
    print(linode.createConfig(linodeID, label, disks))

if userInput == 'boot':
    vps = raw_input("Which Linode? ")
    print(linode.boot(vps))
