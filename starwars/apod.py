#!/usr/bin/python3
import urllib.request
import json

## uncomment this import if you run in a GUI
## and want to open the URL in a browser
## import webbrowser

Starwars = "https://swapi.dev/"

def main():
    ## Define creds
    with open("/home/student/starwars.creds") as mycreds:
        nasacreds = mycreds.read()

    ## remove any "extra" new line feeds on our key
    nasacreds = "api_key=" + starwarscred.strip("\n")

    ## Call the webservice with our key
    apodurlobj = urllib.request.urlopen(starwars + starwarscreds)

    ## read the file-like object
    apodread = apodurlobj.read()

    ## decode JSON to Python data structure
    apod = json.loads(apodread.decode("utf-8"))

    ## display our Pythonic data
    print("\n\nConverted Python data")
    print(apod)

    print()

    print(apod["title"] + "\n")

    print(apod["date"] + "\n")

    print(apod["explanation"] + "\n")

    print(apod["url"])

    ## Uncomment the code below if running in a GUI
    ## and you want to open the URL in a browser
    ## use Firefox to open the HTTPS URL
    ## input("\nPress Enter to open NASA Picture of the Day in Firefox")
    ## webbrowser.open(decodeapod["url"])
if __name__ == "__main__":
    main()
 
