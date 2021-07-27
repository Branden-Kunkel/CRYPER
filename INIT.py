#initialize config files and such
import configparser
import os

def initialize():

    print("Initializing...")

    if not os.path.isfile("config.txt"):

            with open("config.txt") as cfile:

                print("Initialization done!")
    
    else:

        print("Initialization done!")
        

