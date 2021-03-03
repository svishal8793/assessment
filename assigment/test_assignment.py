import unittest

import even_num_list


class TestAssignment(unittest.TestCase):
    def test_even_list_num(self):
        lst = even_num_list.get_even_valued_list([2, 1, 3, 4, 6])
        assert len(lst) == 2
        assert [2, 6] == lst

    def test_null_list(self):
        lst = even_num_list.get_even_valued_list([])
        assert lst is None

    def test_heterogenous_list(self):
        lst = even_num_list.get_even_valued_list([[2, 1, 3, 4, '6']])
        assert lst is None
