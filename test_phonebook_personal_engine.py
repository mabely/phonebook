import unittest
from phonebook_personal_engine import *

class Get_db_test(unittest.TestCase):
    def test_db_conn(self):
        self.assertIsNotNone(get_db("phonebook_database.db"))

if __name__ == '__main__':
    unittest.main()

