import unittest
from search import *

# True or false removed from the menu function
# class Menu_test(unittest.TestCase):
#     def test_uppercase(self):
#         self.assertTrue(menu())

class Search_test(unittest.TestCase):
    # def setUp(self):
    #     self.option = search_p()

    def test_option(self):
        option_p = search_p()
        self.assertLess(option_p, 4)
# Need to figure out how to hard code user inputs for these tests! Below does not work
    # def test_str(self):
    #     self.assertRaises(ValueError, option_p):


if __name__ == '__main__':
    unittest.main()



    