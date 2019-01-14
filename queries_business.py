import sqlite3
import json 
import requests

#connects to db
conn = sqlite3.connect("phonebook_database.db")

#link to db with cursor
c = conn.cursor()

def getPostcodesList(tableName):
    c.execute(f"SELECT DISTINCT(postcode) FROM {tableName}")
#    return first element of each row to remove tuples from the list
#    I have now a list of strings instead of list of tuples with strings
    return [item[0] for item in c.fetchall()]
#    return c.fetchall()
    

#def searchTypeLoc(location, businessType):
#    businessType = businessType.title()
#    location = location.title()
#    c.execute("SELECT * FROM phonebook_business WHERE addressline2 = ? and business_type = ? LIMIT 50", (location, businessType,))
#    return c.fetchall()
#    
#print(searchTypeLoc("belfast", "AutOmotivE"))

def getBusinessByName(location, businessName):
    businessName = businessName.title()
    location = location.title()
    c.execute("SELECT * FROM phonebook_business WHERE addressline2 = ? and business_name = ? LIMIT 50", (location, businessName,))
    return c.fetchall()

print(getBusinessByName("dean", "zOOzzY"))









#closing cursor
c.close()
#closing connection to db
conn.close()