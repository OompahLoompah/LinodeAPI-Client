from client import linodeClient
import os

linode = linodeClient(os.getcwd() + '/../.config')

userInput = raw_input("What do you want to do?\n")

if userInput == 'create':
    linode.createLinode('3', '1')

if userInput == 'destroy':
    userInput = raw_input("What do you want to destroy?\n")
    linode.destroyLinode(userInput)
