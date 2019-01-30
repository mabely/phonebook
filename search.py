import sqlite3
import json 
import requests
from phonebook_personal_engine import get_db

#connects to db
conn = sqlite3.connect("phonebook_database.db")
#link to db with cursor
c = conn.cursor()


def main():
    # db_name = "phonebook_database.db"
    # get_db(db_name)
    menu()

def menu():
    menu_pb = (input('Search for a person or business (P/B)? ')).lower()
    menu_pb = menu_pb.strip()
    try:
        # menu_pb = menu_pb.lower()
        if menu_pb == 'p':
            search_p()
        elif menu_pb == 'b':
            # This needs to call the search_b()
            search_b()
        else:
            print('Sorry we did not recognise that, please try again.)')
            menu()
        # return True
    except Exception as e:
        print(e)
        return False

##### SEARCH MENUS #####

def search_p():
    search_options_p = int(input('''What do you want to search by?
    1 Surname & City
    2 Surname & Postcode
    3 Postcode
    (1/2/3)
    '''))
    try:
        if search_options_p == 1:
            searchLocNameP()
        elif search_options_p == 2:
            searchPostcodeNameP()
        elif search_options_p == 3:
            searchPostcodeP()
        else:
            print('Sorry we did not recognise that, please try again.)')
                
    except ValueError:
            print('Please type a number.')
            search_p()

    # return search_options_p

def search_b():
    search_options_p = int(input('''What do you want to search by?
    1 Business Type & City
    2 Business Name & City
    3 Postcode & Business Type
    4 Postcode & Business Name
    5 Postcode
    (1/2/3/4/5)
    '''))
    try:
        if search_options_p == 1:
            searchTypeLocB()
        elif search_options_p == 2:
            searchNameCityB()
        elif search_options_p == 3:
            searchPostcodeTypeB()
        elif search_options_p == 4:
            searchPostcodeNameB()
        elif search_options_p == 5:
            searchPostcodesB()
        else:
            print('Sorry we did not recognise that, please try again.)')
                
    except ValueError:
            print('Please type a number.')
            search_p()


##### PERSON QUERIES #####

def searchLocNameP():
    name = (input("Provide surname: ")).title()
    location = (input("Provide city: ")).title()

    c.execute("SELECT * FROM phonebook_personal WHERE addressline2 = ? and last_name = ? LIMIT 50", (location, name,))
    
    # print(c.fetchall())
    return c.fetchall()

def searchPostcodeNameP():
    name = (input("Provide surname: ")).title()
    postcode = (input("Provide postcode: ")).upper()

    c.execute("SELECT * FROM phonebook_personal WHERE postcode = ? and last_name = ? LIMIT 50", (postcode, name,))

    # print(c.fetchall())
    return c.fetchall()

def searchPostcodeP():
    postcode = (input("Provide postcode: ")).upper()

    c.execute("SELECT * FROM phonebook_personal WHERE postcode = ? LIMIT 50", (postcode,))

    print(c.fetchall())
    return c.fetchall()

##### BUSINESS QUERIES #####

def searchTypeLocB():
    location = (input("Provide city: ")).title()
    businessType = (input("Provide business type: ")).title()
    c.execute("SELECT * FROM phonebook_business WHERE addressline2 = ? and business_type = ? LIMIT 50", (location, businessType,))
    print(c.fetchall())
    return c.fetchall()

def searchNameCityB():
    location = (input("Provide city: ")).title()
    businessName = (input("Provide business name: ")).title()
    c.execute("SELECT * FROM phonebook_business WHERE addressline2 = ? and business_name = ? LIMIT 50", (location, businessName,))
    print(c.fetchall())
    return c.fetchall()

def searchPostcodeTypeB():
    postcode = (input("Provide postcode: ")).upper()
    businessType = (input("Provide business type: ")).title()
    c.execute("SELECT * FROM phonebook_business WHERE postcode = ? and business_type = ? LIMIT 50", (postcode, businessType,))
    print(c.fetchall())
    return c.fetchall()

def searchPostcodeNameB():
    postcode = (input("Provide postcode: ")).upper()
    businessName = (input("Provide business name: ")).title()
    c.execute("SELECT * FROM phonebook_business WHERE postcode = ? and business_name = ? LIMIT 50", (postcode, businessName,))
    print(c.fetchall())
    return c.fetchall()

def searchPostcodesB():
    postcode = (input("Provide postcode: ")).upper()
    c.execute(f"SELECT * FROM phonebook_business WHERE postcode = ? LIMIT 50", (postcode,))
#    return first element of each row to remove tuples from the list
#    I have now a list of strings instead of list of tuples with strings
    # return [item[0] for item in c.fetchall()]
    print(c.fetchall())
    return c.fetchall()

main()


#closing cursor
c.close()
#closing connection to db
conn.close()

