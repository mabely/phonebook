import sqlite3
import json 
import requests
from coords import getPostcodesList, updateLonLat, updateTable, runAll

#connects to db
conn = sqlite3.connect("phonebook_database.db")

#link to db with cursor
c = conn.cursor()

with open('google_key.secret') as f:
    data = json.load(f)
print(data)
apiKey = data["apikey"]


# def getPostcodesList(tableName):
#     c.execute(f"SELECT DISTINCT(postcode) FROM {tableName}")
# #    return first element of each row to remove tuples from the list
# #    I have now a list of strings instead of list of tuples with strings
#     return [item[0] for item in c.fetchall()]
# #    return c.fetchall()
    

def queryApi(postcode):
   # query the api to get lat & lon for each postcode, supply postcodes list in a json
    r = requests.post(f"https://maps.googleapis.com/maps/api/geocode/json?components=postal_code:{postcode}|country:GB&key={apiKey}")
    # print(r.json())
    print(json.dumps(r.json(), indent=4, sort_keys=True))  
    # result = {
    #   "query": postcode,
    #   "result": {
    #     "latitude": r.json()[][][]
    #     "longitude": ???
    #   }
    # }
    #get result list from api response 
    # return r.json().get("result") 
       
queryApi("NW64HJ")
# def updateLonLat(tableName, postcode, latitude, longitude):
#     c.execute(f'''UPDATE {tableName}
#               SET y_coordinate = ?, x_coordinate = ?
#               WHERE postcode = ?''', (latitude, longitude, postcode))
#     conn.commit()


# def updateTable(postcodeMappingList, tableName):
#     for item in postcodeMappingList:
#         if item["result"] != None:
#             updateLonLat(tableName, item["query"], item["result"]["latitude"], item["result"]["longitude"])
#         else:
#             print(f"Result not found for: {item['query']}")


# def runAll(tableName):
#     postcodes = getPostcodesList(tableName)
#     mappingList = queryApi(postcodes)
#     updateTable(mappingList, tableName)

# runAll("phonebook_personal")
# runAll("phonebook_business")

getPostcodesList("phonebook_personal")

#closing cursor
c.close()
#closing connection to db
conn.close()