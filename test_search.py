import unittest
from search import search_p, correct_postcode

# True or false removed from the menu function
# class Menu_test(unittest.TestCase):
#     def test_uppercase(self):
#         self.assertTrue(menu())

class Search_test(unittest.TestCase):
    # def setUp(self):
    #     self.option = search_p()
#    def test_option(self):
#        option_p = search_p()
#        self.assertLess(option_p, 4)
        
    def test_correct_postcode(self):
        self.assertEqual(correct_postcode("WF9 1QA"), "WF9 1QA")
        self.assertEqual(correct_postcode("WF91QA"), "WF9 1QA")
        self.assertEqual(correct_postcode("SW19 1ZW"), "SW19 1ZW")
        self.assertEqual(correct_postcode("SW191ZW"), "SW19 1ZW")
        self.assertEqual(correct_postcode(""), "")

if __name__ == '__main__':
    unittest.main()
