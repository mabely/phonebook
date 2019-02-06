import sqlite3
import json


def get_db(db_name):
    try:
        if db_name != "phonebook_database.db":
            raise OSError('Wrong database name')
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        # print('Done')
        return c, conn
    except Exception as e:
        print(e)
        return None


def create_table(c, conn):
    c.execute("DROP TABLE IF EXISTS phonebook_business")
    c.execute("CREATE TABLE phonebook_business(business_name TEXT, addressline1 TEXT, addressline2 TEXT, addressline3 TEXT, postcode TEXT, country TEXT, telephone_number REAL, business_type TEXT)")
    conn.commit()
    
    
def business_data_entry(c, conn, data):
    for item in data:
        c.execute('''INSERT INTO phonebook_business(business_name, addressline1, addressline2, addressline3, postcode, country, telephone_number, business_type) VALUES(?, ?, ?, ?, ?, ?, ?, ?)''',
                  (item["business_name"], item["address_line_1"], item["address_line_2"], item['address_line_3'],
                   item['postcode'],item['country'], item['telephone_number'], item['business_category']))

        conn.commit()
        

def addColumnsToDb(c, conn):
    c.execute('''ALTER TABLE phonebook_business ADD x_coordinate REAL''')
    c.execute('''ALTER TABLE phonebook_business ADD y_coordinate REAL''')
    conn.commit()
    

if __name__ == "__main__":
    cursor, connection = get_db("phonebook_database.db")
    create_table(cursor, connection)
    
    #"with" creates a temporary resource access and closes it after "with" ends
    with open("mock_data_business.json") as f:
        data = json.load(f)       
        business_data_entry(cursor, connection, data)
    
    addColumnsToDb(cursor, connection)
    cursor.close()
    connection.close()