#!/usr/bin/env python3
import os
import requests
import sys
file_source = sys.argv[1]
file_destination = sys.argv[2]
api_url = "https://cleanuri.com/api/v1/shorten"
def main():
    with open(file_source, 'r') as source_url_list:
        with open(file_destination, 'a') as destination_url_list:
            for url in source_url_list:
                try:
                    response = requests.post(api_url, data="url=" + url, headers = {"Content-Type": "application/x-www-form-urlencoded"})
                except Exception as error:
                    print("Error in response from api %s \n", error)
                    pass
                destination_url_list.write(response.json()["result_url"]+ "\n")
if __name__ == "__main__":
    main()
