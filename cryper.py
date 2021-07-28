import json
from json.decoder import JSONDecodeError 
import requests
import getopt
import sys
import os
import IHCparser
import INIT

# Main CRYPER program file

INIT.initialize()

api_key, frun_mode, fcrypto, fcurrency = IHCparser.conf_parse()

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
                try:

                    with open('HELP.txt') as help_file:
                        read_file = help_file.read()
                        print(read_file)

                except FileNotFoundError:
                    print("Help file not found?!")

    except getopt.GetoptError('Invalid option speciefied') as err:
        print("Invalid option specified.")

    print(run_type, crypto_asset, currency_match)
    return run_type, crypto_asset, currency_match

    
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
