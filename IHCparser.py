import re
import os

# Parser for config file

def conf_parse():

    pattern_apikey = re.compile("(?<=api_key\s=\s).*")

    pattern_runmode = re.compile("(?<=run_mode\s=\s).*")

    pattern_crypto = re.compile("(?<=crypto_currency\s=\s).*")

    pattern_currency = re.compile("(?<=match_currency\s=\s).*")

    pattern_comments = re.compile("\#*")


    with open("config.txt", mode='r') as parse_it:

        for line in parse_it:

            result_apikey = re.search(pattern_apikey, line)
            result_runmode = re.search(pattern_runmode, line)
            result_crypto = re.search(pattern_crypto, line)
            result_currency = re.search(pattern_currency, line)
            result_comments = re.search(pattern_comments, line)

            if result_apikey:
                ret_apikey = result_apikey.group(0)
            elif result_runmode:
                ret_runmode = result_runmode.group(0)
            elif result_crypto:
                ret_crypto = result_crypto.group(0)
            elif result_currency:
                ret_currency = result_currency.group(0)
            elif result_comments:
                ret_comments = result_comments.group(0)
            else:
                None


    return ret_apikey, ret_runmode, ret_crypto, ret_currency
