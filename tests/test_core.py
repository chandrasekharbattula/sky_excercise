import unittest
from unittest import TestCase

from main.core import determine_call_cost, determine_most_called_number, MobileBill


class CoreTest(TestCase):
    def test_determine_call_cost_more_than_3min(self):
        call_cost = determine_call_cost("00:03:10")
        self.assertEqual(call_cost, 5.7)

    def test_determine_call_cost_less_than_3min(self):
        call_cost = determine_call_cost("00:01:01")
        self.assertEqual(call_cost, 3.1)

    def test_determine_most_called_number(self):
        call_log = [['A', '555-333-212', '00:02:03'], ['B', '555-333-212', '00:02:01'],
                    ['A', '555-333-211', '00:01:03'], ['B', '555-333-213', '00:01:03']]
        phone_no = determine_most_called_number(call_log)
        self.assertEqual(phone_no, '555-333-212')

    def test_total_cost_called_number(self):
        call_log = [['A', '555-333-212', '00:02:03'], ['B', '555-333-212', '00:02:01'],
                    ['A', '555-333-211', '00:01:03']]
        total_call_cost_for_each_customer = MobileBill(call_log).total_cost_for_each_customer()
        count_of_customers = len(total_call_cost_for_each_customer)
        self.assertEqual(count_of_customers, 1)


if __name__ == '__main__':
    unittest.main()
