import json
from json.decoder import JSONDecodeError 
import requests
import getopt, sys
import IHCparser
import INIT

INIT.initialize()

# default variables returned from config file via 'IHCparser'
api_key, frun_mode, fcrypto, fcurrency = IHCparser.conf_parse()
#print(api_key)

# function to figure out the options to use
    # 1) function needs to conform to user bieng able to use defaults
def arg_engine(run_mode, crypto, currency):

    argvalue = sys.argv[1:]

    run_type = run_mode
    crypto_asset = crypto
    currency_match = currency

    opts, args = getopt.getopt(argvalue, 'haxc:m:')

    try:

        for opt, arg in opts:

            if opt in ['-x']:

                run_type = opt

                for opt, arg in opts:

                    if opt in ['-c']:
                        crypto_asset = arg

                    elif opt in ['-m']:
                        currency_match = arg

                    else:
                        crypto_asset = crypto
                        currency_match = currency

            elif opt in ['-a']:
                run_type = opt

            elif opt in ['-h']:
                print("help message here")
            

    except getopt.GetoptError('Invalid option speciefied') as err:
        print("Invalid option specified.")

    # pipes the following variables to 'main'
    print(run_type, crypto_asset, currency_match)
    return run_type, crypto_asset, currency_match


# main function, binds all    
def main():

    run_mode, crypto, currency = arg_engine(frun_mode, fcrypto, fcurrency)

    headers = {'X-CoinAPI-Key' : api_key, 'Accept' : 'application/json', 'Accept-Encoding' : 'deflate, gzip'}
    asset_url = 'https://rest-sandbox.coinapi.io/v1/assets'
    exchange_url =  'https://rest-sandbox.coinapi.io/v1/exchangerate/' + crypto + '/' + currency
    
    try:

        if run_mode in ['x', '-x']:
            
            print(run_mode)

            response = requests.get(exchange_url, headers=headers)

            data = json.loads(response.text)

            print(response)

            print(json.dumps(data, ensure_ascii=True, sort_keys=True, indent=6))
            
        elif run_mode in ['-a', 'a']:

            print(run_mode)

            response = requests.get(asset_url, headers=headers)

            data = json.loads(response.text)
            
            print(response)

            print(json.dumps(data, ensure_ascii=True, sort_keys=True, indent=6))

    except JSONDecodeError:
        print("Empty JSON response recieved!")

main()
