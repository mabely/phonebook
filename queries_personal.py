import sqlite3
import json 
import requests

#connects to db
conn = sqlite3.connect("phonebook_database.db")

#link to db with cursor
c = conn.cursor()

