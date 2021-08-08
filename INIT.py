import configparser
import os
import time

# initialize the config file (or add one if not present) 

def initialize_cfile():

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

                print("Configuration done!")
                time.sleep(1)
                os.system('clear')
    
    else:

        print("OK")
        time.sleep(1)
        os.system('clear')


def initialize_executable():

    destination_path = '/usr/local/bin/'

    script_loc = str(os.path.realpath('cryper.py'))
    init_loc = str(os.path.realpath('INIT.py'))
    ihcparser_loc = str(os.path.realpath('IHCparser.py'))
    
    if os.path.isdir(destination_path):
        pass
    
    else:
        os.system(destination_path)


    with open(script_loc) as main_file, open(init_loc) as init_mod, open(ihcparser_loc) as parser_mod:

        if os.path.isfile(destination_path) and os.path.isfile(destination_path) and os.path.isfile(destination_path):

            pass

        else:

            print('Attempting to change to executable')
            os.system('sudo chmod 755 ' + script_loc)
            os.system('sudo chmod 755 ' + init_loc)
            os.system('sudo chmod 755 ' + ihcparser_loc)
            os.system('sudo cp -i --preserve ' + script_loc + ' ' + destination_path + 'cryper')
            os.system('sudo cp -i --preserve ' + init_loc + ' ' + destination_path)
            os.system('sudo cp -i --preserve ' + ihcparser_loc + ' ' + destination_path)
            os.system('sudo touch ' + destination_path + '__init__.py')
                
            print('OK')
            time.sleep(1)
            os.system('clear')

            if os.path.isfile(destination_path + 'cryper') and os.path.isfile(destination_path + 'INIT.py') and os.path.isfile(destination_path + 'IHCparser.py'):

                print('OK')
                time.sleep(1)
                os.system('clear')

            else:
                print('Something went wrong.')



    
    
    


