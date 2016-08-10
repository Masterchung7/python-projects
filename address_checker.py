import requests

while True:
    addresses = input('enter a street address:\n')
    text = addresses.split(", ")
    for i in range(len(text)):
        print(text[i])
        splittext = text[i].split()
        address = "+".join(splittext[2:-1])
        street = splittext[0] + " " + splittext[1] + " " + address + " " + splittext[-1]
    
        streetparts = street.split(" ")
        response = requests.get("https://gisapps.cityofchicago.org/kiosk/jsp/maptags.jsp?service=mapsplats_transonly&mapaction=address&adr_streetnum="+streetparts[0]+"+&adr_direction="+streetparts[1]+"&adr_streetname="+streetparts[2]+"&adr_streettype="+streetparts[3])
        webpage = response.text
        where = webpage.find('No location')
        if webpage[where:where+11] == "No location":
            print ("invalid address\n")
            #print ("https://gisapps.cityofchicago.org/kiosk/jsp/maptags.jsp?service=mapsplats_transonly&mapaction=address&adr_streetnum="+streetparts[0]+"+&adr_direction="+streetparts[1]+"&adr_streetname="+streetparts[2]+"&adr_streettype="+streetparts[3]+"\n")
        else:
            print ("valid address\n")
            print ("https://gisapps.cityofchicago.org/kiosk/jsp/maptags.jsp?service=mapsplats_transonly&mapaction=address&adr_streetnum="+streetparts[0]+"+&adr_direction="+streetparts[1]+"&adr_streetname="+streetparts[2]+"&adr_streettype="+streetparts[3]+"\n\n")
    
