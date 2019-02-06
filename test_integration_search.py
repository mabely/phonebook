from sort import currentLocation
from distance import distance
import os
import unittest
from unittest.mock import patch

# Tests function for finding user's current location, returning long/lat for hard-coded user input
def test_location():
    with patch("builtins.input", return_value = "SE17 2HP"):
        # first of all, this is a correct integration test: it tests your code vs 3rd party service (API)
        # good use of mocking, but it's easier to test if input is outside the function and passed as a parameter
        # the only thing missing is usage of unittest and assert as in unit tests
        # overall very good job ^^
        if currentLocation() == {'longitude': -0.091014, 'latitude': 51.486879}:
            return True, {'longitude': -0.091014, 'latitude': 51.486879}
        else:
            print('Failed to find current location')
            return False

# Tests the function for calculating distance between 2 sets of long/lat based on test_location output
def test_distance():
    # this is a unit test, please use assert
    if test_location:
        x = test_location() # not needed
        if distance(x[1]['latitude'], x[1]['longitude'], x[1]['latitude'], x[1]['longitude']) == 0:
            return True
        else:
            print('Failed to calculate distance correctly')
            return False


if __name__ == "__main__":
    print(test_location())
    print(test_distance())
    
