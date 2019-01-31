import sqlite3
import json 
import requests

conn = sqlite3.connect("phonebook_database.db")
c = conn.cursor()


def sort_p(returned_results):
    sort_yn = (input('''Do you want to sort? (y/n) ''')).lower()
    try:
        if sort_yn == 'y':
            sort_options_p = int(input(
'''What do you want to sort by?
1 Surname
2 Postcode
3 City
(1/2/3)
'''))

            if sort_options_p == 1:
                sortSurname(returned_results)
            elif sort_options_p == 2:
                sortPostcode(returned_results)
            elif sort_options_p == 3:
                sortCity(returned_results)
            else:
                print('Sorry we did not recognise that, please try again.')
                sort_p(returned_results)

        elif sort_yn == 'n':
                pass
        else:
            print('Sorry we did not recognise that, please try again.')
            sort_p(returned_results)

    except ValueError:
        print('Please enter a number.')


def sortSurname(returned_results):
    x = list(returned_results)
    y = sorted(x, key=lambda s:s[1])
    print(y)
    return y

def sortPostcode(returned_results):
    x = list(returned_results)
    y = sorted(x, key=lambda s:s[5])
    print(y)
    return y

def sortCity(returned_results):
    x = list(returned_results)
    y = sorted(x, key=lambda s:s[3])
    print(y)
    return y
  

# BUSINESS

def sort_b(returned_results):
    sort_yn = (input('''Do you want to sort? (y/n) ''')).lower()
    try:
        if sort_yn == 'y':
            sort_options_b = int(input(
'''What do you want to sort by?
1 Business Type
2 Business Name
3 City
4 Postcode
(1/2/3/4)
'''))

            if sort_options_b == 1:
                sortBusType(returned_results)
            elif sort_options_b == 2:
                sortBusName(returned_results)
            elif sort_options_b == 3:
                sortCity2(returned_results)
            elif sort_options_b == 4:
                sortPostcode2(returned_results)
            else:
                print('Sorry we did not recognise that, please try again.')
                sort_p(returned_results)

        elif sort_yn == 'n':
                pass
        else:
            print('Sorry we did not recognise that, please try again.')
            sort_p(returned_results)

    except ValueError:
        print('Please enter a number.')

def sortBusType(returned_results):
    x = list(returned_results)
    y = sorted(x, key=lambda s:s[7])
    print(y)
    return y

def sortBusName(returned_results):
    x = list(returned_results)
    y = sorted(x, key=lambda s:s[0])
    print(y)
    return y

def sortCity2(returned_results):
    x = list(returned_results)
    y = sorted(x, key=lambda s:s[2])
    print(y)
    return y

def sortPostcode2(returned_results):
    x = list(returned_results)
    y = sorted(x, key=lambda s:s[4])
    print(y)
    return y


# returned_results = ('Kimia', '61 Lindbergh Street', 'Birmingham', 'England', 'B41 1NT', 'United Kingdom', '0862 535 3144', 'Electronics', None, None), ('Dynazzy', '2 La Follette Road', 'Burmingham', 'England', 'B40 1NT', 'United Kingdom', '0123 473 8784', 'Kids', None, None), ('Divavu', '56316 Anderson Road', 'Birmingham', 'England', 'B40 1NT', 'United Kingdom', '0957 844 1467', 'Jewelery', None, None)

# sort_p(returned_results)
# sort_b(returned_results)


#closing cursor
c.close()
#closing connection to db
conn.close()



# GETS USER LOCATION AND FINDS LONG AND LAT - FOR SORTING
# def currentLocation():
#     inputLocation = input("What's your current location? ")    
#     inputLocation = inputLocation.replace(" ", "")
#     r = requests.get(f"http://api.postcodes.io/postcodes/{inputLocation}")
#     lat = r.json().get("result")["latitude"]
#     lon = r.json().get("result")["longitude"]
#     print(lon, lat)
#     return lon, lat

# # currentLocation()