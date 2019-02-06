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
#    deletes table phonebook_personal and all its contents
    c.execute("DROP TABLE IF EXISTS phonebook_personal")
    c.execute("CREATE TABLE phonebook_personal(first_name TEXT, last_name TEXT, addressline1 TEXT, addressline2 TEXT, addressline3 TEXT, postcode TEXT, country TEXT, telephone_number REAL)")
    conn.commit()

    
def personal_data_entry(c, conn, data):
    for item in data:
        c.execute('''INSERT INTO phonebook_personal(first_name, last_name, addressline1, addressline2, addressline3, postcode, country, telephone_number) VALUES(?, ?, ?, ?, ?, ?, ?, ?)''',
                  (item["first_name"], item["last_name"], item["address_line_1"], item["address_line_2"], item['address_line_3'],
                   item['postcode'],item['country'], item['telephone_number']))
        conn.commit()


def addColumnsToDb(c, conn):
    c.execute('''ALTER TABLE phonebook_personal ADD x_coordinate REAL''')
    c.execute('''ALTER TABLE phonebook_personal ADD y_coordinate REAL''')
    conn.commit()
    

if __name__ == "__main__":
    cursor, connection = get_db("phonebook_database.db")
    create_table(cursor, connection)
    
    #"with" creates a temporary resource access and closes it after "with" ends
    with open("mock_data_people.json") as f:
        data = json.load(f)       
        personal_data_entry(cursor, connection, data)
    
    addColumnsToDb(cursor, connection)
    cursor.close()
    connection.close()
