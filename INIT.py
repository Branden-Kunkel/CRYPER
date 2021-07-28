import configparser
import os

# initialize the config file (or add one if not present) 

def initialize():

    print("Initializing...")


    if not os.path.isfile("config.txt"):

            with open("config.txt", mode='a') as cfile:

                cfile.write("## Config file - CRYPER\n\n")
                cfile.write('# Any and all crypto currencies or government currencies shall be referred to as assets from this point on.\n\n\n')
                cfile.write('## USER DEFAULT SECTION ##\n\n')
                cfile.write('# Enter the API key provided by https://www.coinapi.io/\napi_key = \n\n')
                cfile.write('# Run mode flags are either \'a\' for all assets or \'x\' to view exchange rates for any two given currencies.\nrun_mode = \n\n')
                cfile.write('# Set this flag as your preferred asset that you wish to see the exchange rate of, IN ALL CAPS! ex. BTC, DOGE, USD, etc. Only has effect when the run mode is set to \'x\'. Equal to \'-c\' option. \ncrypto_currency = \n\n')
                cfile.write('# Set this flag as your preferred asset to match against, IN ALL CAPS. ex. DOGE, BTC, USD, etc. Equal to \'-m\' option. \nmatch_currency = \n\n')

                print("Initialization done!")
    
    else:

        print("Initialization done!")
        

