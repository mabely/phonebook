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
    

def getBusinessByType(businessType):
    c.execute("SELECT * FROM phonebook_business WHERE business_type = ?", (businessType,))
    return c.fetchall()


print(getBusinessByType("Music"))



#closing cursor
c.close()
#closing connection to db
conn.close()