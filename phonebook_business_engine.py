# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 12:18:10 2019

@author: mag
"""
import sqlite3
import json
from pprint import pprint 

#connects to db
conn = sqlite3.connect("phonebook_database.db")

#link to db with cursor
c = conn.cursor()

def create_table():
    c.execute("DROP TABLE IF EXISTS phonebook_business")
    c.execute("CREATE TABLE phonebook_business(business_name TEXT, addressline1 TEXT, addressline2 TEXT, addressline3 TEXT, postcode TEXT, country TEXT, telephone_number REAL, business_type TEXT)")
    conn.commit()
    
create_table()

with open("mock_data_business.json") as f:
    data = json.load(f)
#pprint(data)
    
def business_data_entry():
    for item in data:
#        method1
#        values_list = list(item.values())
#        c.execute('''INSERT INTO phonebook_business(business_name, addressline1, addressline2, addressline3, postcode, country, telephone_number, business_type) VALUES(?, ?, ?, ?, ?, ?, ?, ?)''', (values_list))
        
#        method2
        c.execute('''INSERT INTO phonebook_business(business_name, addressline1, addressline2, addressline3, postcode, country, telephone_number, business_type) VALUES(?, ?, ?, ?, ?, ?, ?, ?)''',
                  (item["business_name"], item["address_line_1"], item["address_line_2"], item['address_line_3'],
                   item['postcode'],item['country'], item['telephone_number'], item['business_category']))

        conn.commit()

#remove data from db in order to avoid duplicate
#c.execute("DELETE FROM phonebook_business")  
business_data_entry()

def addColumnsToDb():
    c.execute('''ALTER TABLE phonebook_business ADD x_coordinate REAL''')
    c.execute('''ALTER TABLE phonebook_business ADD y_coordinate REAL''')
    conn.commit()
    
addColumnsToDb()

#closing cursor
c.close()
#closing connection to db
conn.close()