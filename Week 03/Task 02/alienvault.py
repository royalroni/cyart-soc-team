#!/usr/bin/env python3

import sys
import json
import requests

def main():
    alert = json.loads(sys.stdin.read())

    api_key = "4353bb72dd37dfba6565173e4b36fbaa0d999c2c0e5e4a85b504f2a83e7497aa"

    if 'data' in alert and 'srcip' in alert['data']:
        ip = alert['data']['srcip']
        url = f"https://otx.alienvault.com/api/v1/indicators/IPv4/{ip}/general"
        headers = {"X-OTX-API-KEY": api_key}

        response = requests.get(url, headers=headers)
        print(response.text)

if __name__ == "__main__":
    main()