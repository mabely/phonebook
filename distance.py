import sqlite3
import json 
import requests
from math import pi, sin, cos, sqrt, atan2

#connects to db
conn = sqlite3.connect("phonebook_database.db")

#link to db with cursor
c = conn.cursor()


def getBusinessByType(location, businessType):
    businessType = businessType.title()
    location = location.upper()
    c.execute("SELECT * FROM phonebook_business WHERE postcode = ? and business_type = ?", (location, businessType,))
#    return c.fetchall()
    return [item[8:10] for item in c.fetchall()]

currentLat = 51.486879
currentLon = -0.091014
#print(getBusinessByType("EC3M 1AA", "Shoes"))

lon1 = getBusinessByType("OX7 3AA", "jewelery")[0][0]
print(lon1)
lat1 = getBusinessByType("OX7 3AA", "jewelery")[0][1]
print(lat1)

def distance(lat1, lng1, lat2, lng2): 
    #return distance as meter if you want km distance, remove "* 1000" 
    radius = 6371

    dLat = (lat2-lat1) * pi/180 
    dLng = (lng2-lng1) * pi/180 

    lat1 = lat1 * pi/180 
    lat2 = lat2 * pi/180 

    val = sin(dLat/2) * sin(dLat/2) + sin(dLng/2) * sin(dLng/2) * cos(lat1) * cos(lat2)  
    ang = 2 * atan2(sqrt(val), sqrt(1-val)) 
    return round(radius * ang,2)

print(distance(currentLat, currentLon, lat1, lon1),"km")


#closing cursor
c.close()
#closing connection to db
conn.close()