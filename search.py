import sqlite3
from phonebook_personal_engine import get_db
from sort import *

def menu(cursor):
    menu_pb = (input('Search for a person or business (P/B)? ')).lower()
    menu_pb = menu_pb.strip()
    try:
        if menu_pb == 'p':
            search_p(cursor)
        elif menu_pb == 'b':
            # This needs to call the search_b()
            search_b(cursor)
        else:
            print('Sorry we did not recognise that, please try again.)')
            menu(cursor)
        # return True
    except Exception as e:
        print(e)
        return False

##### SEARCH MENUS #####

def search_p(cursor):
    try:
        search_options_p = int(input('''What do you want to search by?
    1 Surname & City
    2 Surname & Postcode
    3 Postcode
    (Select 1, 2 or 3)
    '''))
        # None - kind of "empty" value, we do it because we don't want to forget creating this variable
        # in all if elif else paths. It is useful when reading this variable later - we will not get an Exception
        returned_results = None
        if search_options_p == 1:
            returned_results = searchLocNameP(cursor)
        elif search_options_p == 2:
            returned_results = searchPostcodeNameP(cursor)
        elif search_options_p == 3:
            returned_results = searchPostcodeP(cursor)
        else:
            print('Sorry we did not recognise that, please try again.')
        
        if returned_results is None: 
            #all search functions can return None for no search results, we want user to search again
            search_p(cursor)
        else:
            sort_p(returned_results)
            
    except ValueError:
            print('Please type a number.')
            search_p(cursor)


def search_b(cursor):
    try:
        search_options_p = int(input('''What do you want to search by?
    1 Business Type & City
    2 Business Name & City
    3 Postcode & Business Type
    4 Postcode & Business Name
    5 Postcode
    (Select 1/2/3/4/5)
    '''))
        returned_results = None
        if search_options_p == 1:
            returned_results = searchTypeLocB(cursor)
        elif search_options_p == 2:
            returned_results = searchNameCityB(cursor)
        elif search_options_p == 3:
            returned_results = searchPostcodeTypeB(cursor)
        elif search_options_p == 4:
            returned_results = searchPostcodeNameB(cursor)
        elif search_options_p == 5:
            returned_results = searchPostcodesB(cursor)
        else:
            print('Sorry we did not recognise that, please try again.')
            
        if returned_results is None:
            search_b(cursor)
        else:
            sort_b(returned_results) 
            
    except ValueError:
            print('Please enter a number.')
            search_b(cursor)


def correct_postcode(postcode):
    if len(postcode) < 6:
        return postcode + "%"
    elif len(postcode) >= 6 and postcode[-4] != " ":
        return postcode[:-3] + " " + postcode[-3:]
    return postcode
        

def isResultEmpty(returned_results):
    if returned_results == []:
        print("We could not find any matches. Please try again.")
        return None 
    else:
        print(format_results(returned_results))
        return returned_results


##### PERSON QUERIES #####
def searchLocNameP(cursor):
    name = (input("Provide surname: ")).title()
    location = (input("Provide city: ")).title()

    cursor.execute("SELECT * FROM phonebook_personal WHERE addressline2 = ? and last_name = ? LIMIT 50", (location, name,))
    returned_results = cursor.fetchall()
    
    return isResultEmpty(returned_results)



def searchPostcodeNameP(cursor):
    name = (input("Provide surname: ")).title()
    postcode = correct_postcode(input("Provide postcode: ")).upper()

    cursor.execute("SELECT * FROM phonebook_personal WHERE postcode LIKE ? and last_name = ? LIMIT 50", (postcode, name,))
    returned_results = cursor.fetchall()
    
    return isResultEmpty(returned_results)
    

def searchPostcodeP(cursor):
    postcode = correct_postcode(input("Provide postcode: ")).upper()

    cursor.execute("SELECT * FROM phonebook_personal WHERE postcode LIKE ? LIMIT 50", (postcode,))
    returned_results = cursor.fetchall()

    return isResultEmpty(returned_results)


##### BUSINESS QUERIES #####
def searchTypeLocB(cursor):
    location = (input("Provide city: ")).title()
    businessType = (input("Provide business type: ")).title()
    cursor.execute("SELECT * FROM phonebook_business WHERE addressline2 = ? and business_type = ? LIMIT 50", (location, businessType,))

    returned_results = cursor.fetchall()
    
    return isResultEmpty(returned_results)


def searchNameCityB(cursor):
    location = (input("Provide city: ")).title()
    businessName = (input("Provide business name: ")).title()
    cursor.execute("SELECT * FROM phonebook_business WHERE addressline2 = ? and business_name = ? LIMIT 50", (location, businessName,))
    returned_results = cursor.fetchall()

    return isResultEmpty(returned_results)

def searchPostcodeTypeB(cursor):
    postcode = correct_postcode(input("Provide postcode: ")).upper()
    businessType = (input("Provide business type: ")).title()
    cursor.execute("SELECT * FROM phonebook_business WHERE postcode LIKE ? and business_type = ? LIMIT 50", (postcode, businessType,))
    returned_results = cursor.fetchall()

    return isResultEmpty(returned_results)


def searchPostcodeNameB(cursor):
    postcode = correct_postcode(input("Provide postcode: ")).upper()
    businessName = (input("Provide business name: ")).title()
    cursor.execute("SELECT * FROM phonebook_business WHERE postcode LIKE ? and business_name = ? LIMIT 50", (postcode, businessName,))
    returned_results = cursor.fetchall()

    return isResultEmpty(returned_results)


def searchPostcodesB(cursor):
    postcode = correct_postcode(input("Provide postcode: ")).upper()
    cursor.execute(f"SELECT * FROM phonebook_business WHERE postcode LIKE ? LIMIT 50", (postcode,))
    returned_results = cursor.fetchall()
    
    return isResultEmpty(returned_results)
    
    
def format_results(returned_results):
    i = "\n".join([str(item) for item in returned_results])
    return i 


if __name__ == "__main__":
    with sqlite3.connect("phonebook_database.db") as conn: #"with" closes the connection after it ends
        c = conn.cursor()
        menu(c)
        c.close()
