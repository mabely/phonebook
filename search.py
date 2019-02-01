import sqlite3
import json 
import requests
from phonebook_personal_engine import get_db
from sort import *
from os.path import exists



def main():
    # Establishes connection to db
    db_path = '/Users/Me/Desktop/btfurther/module2/phonebook_project/phonebook_database.db'
    if check_db(db_path):
        c, conn = connect_db(db_path)
        print('connection established')
    menu()

def check_db(db_path):
    #initializes path to db
    if exists(db_path):
        return True
    else:
        return False

def connect_db(db_path):
    try:
        if check_db(db_path):
            #connects to db
            conn = sqlite3.connect("phonebook_database.db")
            #link to db with cursor
            c = conn.cursor()
            return c, conn
        else:
            print('Database does not exist.')
            return False, False
    except:
        print('Something went wrong with connecting to database.')

def menu():
    menu_pb = (input('Search for a person or business (P/B)? ')).lower()
    menu_pb = menu_pb.strip()
    try:
        if menu_pb == 'p':
            search_p()
        elif menu_pb == 'b':
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
            returned_results = searchLocNameP()
            sort_p(returned_results)
        elif search_options_p == 2:
            returned_results = searchPostcodeNameP()
            sort_p(returned_results)
        elif search_options_p == 3:
            returned_results = searchPostcodeP()
            sort_p(returned_results)
        else:
            print('Sorry we did not recognise that, please try again.)')
            # search_p()
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
            returned_results = searchTypeLocB()
            sort_b(returned_results)
        elif search_options_p == 2:
            returned_results = searchNameCityB()
            sort_b(returned_results)
        elif search_options_p == 3:
            returned_results = searchPostcodeTypeB()
            sort_b(returned_results)
        elif search_options_p == 4:
            returned_results = searchPostcodeNameB()
            sort_b(returned_results)
        elif search_options_p == 5:
            returned_results = searchPostcodesB()
            sort_b(returned_results)
        else:
            print('Sorry we did not recognise that, please try again.')
            # search_b()
    except ValueError:
            print('Please enter a number.')
            # search_p()


##### PERSON QUERIES #####

def searchLocNameP():
    name = (input("Provide surname: ")).title()
    location = (input("Provide city: ")).title()
    c, conn = connect_db(db_path)
    c.execute("SELECT * FROM phonebook_personal WHERE addressline2 = ? and last_name = ? LIMIT 50", (location, name,))
    returned_results = c.fetchall()
    conn.commit()
    print(returned_results)
    return returned_results

def searchPostcodeNameP():
    name = (input("Provide surname: ")).title()
    postcode = (input("Provide postcode: ")).upper()

    c.execute("SELECT * FROM phonebook_personal WHERE postcode = ? and last_name = ? LIMIT 50", (postcode, name,))
    returned_results = c.fetchall()
    print(returned_results)
    return returned_results

def searchPostcodeP():
    postcode = (input("Provide postcode: ")).upper()

    c.execute("SELECT * FROM phonebook_personal WHERE postcode = ? LIMIT 50", (postcode,))
    returned_results = c.fetchall()
    print(returned_results)
    return returned_results

##### BUSINESS QUERIES #####

def searchTypeLocB():
    location = (input("Provide city: ")).title()
    businessType = (input("Provide business type: ")).title()
    c.execute("SELECT * FROM phonebook_business WHERE addressline2 = ? and business_type = ? LIMIT 50", (location, businessType,))
    returned_results = c.fetchall()
    print(returned_results)
    return returned_results

def searchNameCityB():
    location = (input("Provide city: ")).title()
    businessName = (input("Provide business name: ")).title()
    c.execute("SELECT * FROM phonebook_business WHERE addressline2 = ? and business_name = ? LIMIT 50", (location, businessName,))
    returned_results = c.fetchall()
    print(returned_results)
    return returned_results

def searchPostcodeTypeB():
    postcode = (input("Provide postcode: ")).upper()
    businessType = (input("Provide business type: ")).title()
    c.execute("SELECT * FROM phonebook_business WHERE postcode = ? and business_type = ? LIMIT 50", (postcode, businessType,))
    returned_results = c.fetchall()
    print(returned_results)
    return returned_results

def searchPostcodeNameB():
    postcode = (input("Provide postcode: ")).upper()
    businessName = (input("Provide business name: ")).title()
    c.execute("SELECT * FROM phonebook_business WHERE postcode = ? and business_name = ? LIMIT 50", (postcode, businessName,))
    returned_results = c.fetchall()
    print(returned_results)
    return returned_results

def searchPostcodesB():
    postcode = (input("Provide postcode: ")).upper()
    c.execute(f"SELECT * FROM phonebook_business WHERE postcode = ? LIMIT 50", (postcode,))
#    return first element of each row to remove tuples from the list
#    I have now a list of strings instead of list of tuples with strings
    # return [item[0] for item in c.fetchall()]
    returned_results = c.fetchall()
    print(returned_results)
    return returned_results

# returned_results = [('Saundra', 'Crutch', '51838 North Hill', 'Upton', 'England', 'WF9 1QA', 'United Kingdom', '0259 246 0508', None, None), ('Wilbert', 'Watsham', '01 Eastlawn Drive', 'Upton', 'England', 'WF9 1QA', 'United Kingdom', '0296 420 4586', None, None)]
def format_results(returned_results):
    for item in returned_results:
        print(item,end='\n')


main()

# def close_db(db_path):
#     #closing cursor
# c.close()
# #closing connection to db
# conn.close()

