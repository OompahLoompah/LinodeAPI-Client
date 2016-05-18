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
