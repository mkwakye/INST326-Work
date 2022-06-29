""" Pytest for get_cost() """

"""
Names: Nicholas Rudiger, Michael Kwakye
Emails: nicrudiger@gmail.com, mkwakye99@gmail.com
Assignment: Exercise 2
Date: 2_16_21

"""

import sys
import bulk_pricing as bp

def test_bulk_pricing_function():
    """ function that tests some
    cases within the bulk_pricing program
    """
    assert bp.get_cost(9) == 6.75
    assert bp.get_cost(0) == 0.0
    assert bp.get_cost(300) == 210.0
    assert bp.get_cost(70) == 50.4
    assert bp.get_cost(2000) == 1340.0
    