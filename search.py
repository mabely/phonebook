import sqlite3
import json 
import requests

#connects to db
conn = sqlite3.connect("phonebook_database.db")

#link to db with cursor
c = conn.cursor()

##### INPUTS USED AS ARGS #####

name = input("Provide surname: ")
location = input("Provide city: ")
businessType = input("Provide business type: ")
businessName = input("Provide business name: ")

##### PERSON #####

#SORTING NEEDS TO BE ADDED HERE
#Below location takes only surname, city - eg. London. 

def searchLocNameP(location, name):
    name = name.title()
    location = location.title()
    c.execute("SELECT * FROM phonebook_personal WHERE addressline2 = ? and last_name = ? LIMIT 50", (location, name,))
    
#    print(c.fetchall())
    return c.fetchall()

#Below tests above function.
#print(searchLocNameP(location,name))
#print(searchLocNameP("buckland", "abade"))


##### BUSINESS #####

def searchTypeLocB(location, businessType):
    businessType = businessType.title()
    location = location.title()
    c.execute("SELECT * FROM phonebook_business WHERE addressline2 = ? and business_type = ? LIMIT 50", (location, businessType,))
#    print(c.fetchall())
    return c.fetchall()

#print(searchTypeLocB(location, businessType))
#print(searchTypeLocB("belfast", "AutOmotivE"))

def searchNameB(location, businessName):
    businessName = businessName.title()
    location = location.title()
    c.execute("SELECT * FROM phonebook_business WHERE addressline2 = ? and business_name = ? LIMIT 50", (location, businessName,))
#    print(c.fetchall())
    return c.fetchall()

print(searchNameB(location, businessName))
#Below tests above function.
#print(searchNameB("dean", "zOOzzY"))


#closing cursor
c.close()
#closing connection to db
conn.close()

