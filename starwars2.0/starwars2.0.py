#!/usr/bin/python3

import requests

AOIF_CHAR = "https://swapi.dev/api/people/"
def main():
    choice= input("Choose a number from 1-88 young one!\n>" )

    resp = requests.get(AOIF_CHAR + choice).json()
    
    print("CHARACTER:", end= " ")
    print(f"{resp['name']}\n" if resp['name'] else f"{resp['aliases'][0]}\n")

if __name__ == "__main__":
    main()

# let's try looking for Vadar.
#GetStarWarsCharacters()
#'name': 'darth vader',

 # 'skin_color': 'white',
  #'species': ['http://swapi.dev/api/species/1/'],
  #'starships': ['http://swapi.dev/api/starships/13/'],
  #'url': 'http://swapi.dev/people/4/',
  #'vehicles': []},
 # {'birth_year': '19BBY',
  #'eye_color': 'brown',
  #'films': ['http://swapi.dev/api/films/6/'
   # example of reading the star-wars api
#characters = GetStarWarsCharacters() # This function gets the people as json
