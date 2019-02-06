import unittest
import phonebook_business_engine
import phonebook_personal_engine
import os


class Db_test(unittest.TestCase):    
    def test_1get_db(self):
        cursor, connection = phonebook_business_engine.get_db("phonebook_database.db")
        self.assertIsNotNone(cursor)
        self.assertIsNotNone(connection)
        self.assertTrue(os.path.isfile("phonebook_database.db"))
        cursor.close()
        connection.close()
        
    def test_2create_table(self):
        cursor, connection = phonebook_business_engine.get_db("phonebook_database.db")
        phonebook_business_engine.create_table(cursor, connection)
        try:
            cursor.execute("select * from phonebook_business")
            returned_results = cursor.fetchall()
            self.assertEqual(0, len(returned_results))
        except Exception:
            self.assertEqual(True, False)
        cursor.close()
        connection.close()
        
    def test_3business_data_entry(self):
        cursor, connection = phonebook_business_engine.get_db("phonebook_database.db")
        data = [{"business_name":"Buzzshare","address_line_1":"6 Atwood Pass","address_line_2":"Newton","address_line_3":"Scotland","postcode":"IV10 8AA","country":"United Kingdom","telephone_number":"0267 682 1503","business_category":"Home"}]
        try:
            phonebook_business_engine.business_data_entry(cursor, connection, data)
            cursor.execute("select * from phonebook_business")
            returned_results = cursor.fetchall()
            self.assertEqual(1, len(returned_results))
            self.assertEqual("Buzzshare", returned_results[0][0])
            self.assertEqual("6 Atwood Pass", returned_results[0][1])
            self.assertEqual("Home", returned_results[0][-1])
            
        except Exception:
            self.assertEqual(True, False)
        cursor.close()
        connection.close()
        

if __name__ == '__main__':
    if os.path.isfile("phonebook_database.db"):
        os.remove("phonebook_database.db")
    unittest.main()
