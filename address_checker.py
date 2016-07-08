import requests
x = (input("enter number of addresses to check: "))

for i in range(int(x)):
    street = input('enter a street address:\n')
    streetparts = street.split(" ")

    response = requests.get("https://gisapps.cityofchicago.org/kiosk/jsp/maptags.jsp?service=mapsplats_transonly&mapaction=address&adr_streetnum="+streetparts[0]+"+&adr_direction="+streetparts[1]+"&adr_streetname="+streetparts[2]+"&adr_streettype="+streetparts[3])
    text = response.text
    where = text.find('No location')
    if text[where:where+11] == "No location":
        print ("invalid address\n")
    else:
        print ("valid address\n")
