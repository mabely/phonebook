import sqlite3
import json 
import requests

#connects to db
conn = sqlite3.connect("phonebook_database.db")

#link to db with cursor
c = conn.cursor()

#def searchByName(location, name):
#    name = name.title()
#    location = location.title()
#    c.execute("SELECT * FROM phonebook_personal WHERE addressline2 = ? and last_name = ? LIMIT 50", (location, name,))
#    return c.fetchall()
#
#print(searchByName("buckland", "abade"))
#    c.execute("SELECT * FROM phonebook_personal WHERE addressline2 = ? and last_name = ? LIMIT 50", (location, name,))
#    return c.fetchall()

def sortAlpha(column):
    c.execute(f"SELECT * FROM phonebook_personal ORDER BY {column} ASC LIMIT 10")
    return c.fetchall()


print(sortAlpha("last_name"))


#def gatherDbInfo(c):
#    c.execute(''')
#    


#closing cursor
c.close()
#closing connection to db
conn.close()