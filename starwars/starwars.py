#!/usr/bin/env python3
""" Star Wars"""
import urllib.request
import requests
import json
    # defining the url
starwars = "https://swapi.dev/"
   
def main():
    starwars =json.loads(starwars.decode('utf-8'))
    starwars = urllib.request.urlopen(starwars)
    starwarslore = starwarslore.read()
#print(starwarslore)
if __name__ == "__main__":
    main()
