import sqlite3
import json 
import requests

#connects to db
conn = sqlite3.connect("phonebook_database.db")

#link to db with cursor
c = conn.cursor()

def sortAlpha(column):
    c.execute(f"SELECT * FROM phonebook_personal ORDER BY {column} ASC LIMIT 10")
    return c.fetchall()

print(sortAlpha("last_name"))



#closing cursor
c.close()
#closing connection to db
conn.close()
