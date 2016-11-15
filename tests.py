from unittest import TestCase, main as run_tests

from sorts import bubble_sort, selection_sort, insertion_sort

int_sort_list = [55, 54, 3, 2, 100], [2, 3, 54, 55, 100]
str_sort_list = ['apple juice', 'butter', 'carrot', 'banana', 'apple'], [
    'apple',
    'apple juice',
    'banana',
    'butter',
    'carrot',
]


class BubbleSortTest(TestCase):
    def test_is_sorted(self):
        a = int_sort_list[0].copy()
        bubble_sort(a)
        self.assertEqual(a, int_sort_list[1])
        b = str_sort_list[0].copy()
        bubble_sort(b)
        self.assertEqual(b, str_sort_list[1])


class SelectionSortTest(TestCase):
    def test_is_sorted(self):
        a = int_sort_list[0].copy()
        selection_sort(a)
        self.assertEqual(a, int_sort_list[1])
        b = str_sort_list[0].copy()
        selection_sort(b)
        self.assertEqual(b, str_sort_list[1])


class InsertionSortTest(TestCase):
    def test_is_sorted(self):
        a = int_sort_list[0].copy()
        insertion_sort(a)
        self.assertEqual(a, int_sort_list[1])
        b = str_sort_list[0].copy()
        insertion_sort(b)
        self.assertEqual(b, str_sort_list[1])


if __name__ == '__main__':
    run_tests()
