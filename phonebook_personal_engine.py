# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 14:58:17 2019

@author: nahas
"""

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
    c.execute("DROP TABLE IF EXISTS phonebook_personal")
    c.execute("CREATE TABLE phonebook_personal(first_name TEXT, last_name TEXT, addressline1 TEXT, addressline2 TEXT, addressline3 TEXT, postcode TEXT, country TEXT, telephone_number REAL)")
    conn.commit()
    
create_table()

#"with" creates a temporary resource access and closes it after "with" ends
with open("mock_data_people.json") as f:
    data = json.load(f)
#pprint(data)
    
def personal_data_entry():
    for item in data:
#        method1
#        values_list = list(item.values())
#        print(values_list)
#        c.execute('''INSERT INTO phonebook_personal(first_name, last_name, addressline1, addressline2, addressline3, postcode, country, telephone_number) VALUES(?, ?, ?, ?, ?, ?, ?, ?)''', (values_list))
#        
        #method2
        c.execute('''INSERT INTO phonebook_personal(first_name, last_name, addressline1, addressline2, addressline3, postcode, country, telephone_number) VALUES(?, ?, ?, ?, ?, ?, ?, ?)''',
                  (item["first_name"], item["last_name"], item["address_line_1"], item["address_line_2"], item['address_line_3'],
                   item['postcode'],item['country'], item['telephone_number']))
        print(item["first_name"], item["last_name"], item["address_line_1"], item["address_line_2"], item['address_line_3'],
                   item['postcode'],item['country'], item['telephone_number'])
        conn.commit()

#remove data from db in order to avoid duplicate
#c.execute("DELETE FROM phonebook_personal")        
personal_data_entry()


def addColumnsToDb():
    c.execute('''ALTER TABLE phonebook_personal ADD x_coordinate REAL''')
    c.execute('''ALTER TABLE phonebook_personal ADD y_coordinate REAL''')
    conn.commit()
    
addColumnsToDb()



#closing cursor
c.close()
#closing connection to db
conn.close()
