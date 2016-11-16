from unittest import TestCase, main as run_tests

from sorts import bubble_sort, selection_sort, insertion_sort, shell_sort

int_sort_list = [
                    55, 54, 3, 2, 100, 33, 99, 939, 20093, 30039, 34, 7, 435, 3,
                    1, 4, 34, 7, 4, 2, 76, 467, 3, 4, 6, 46, 75, 68, 5, 5, 56,
                    5, 65, 674, 2, 536, 45, 3, 6, 363, 5, 3456, 345, 456, 45, 5,
                    4, 58, 8, 67, 678, 67, 56, 7, 4, 635, 3, 3, 21, 2
                ], [
                    1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5,
                    5, 6, 6, 7, 7, 7, 8, 21, 33, 34, 34, 45, 45, 46, 54, 55, 56,
                    56, 58, 65, 67, 67, 68, 75, 76, 99, 100, 345, 363, 435, 456,
                    467, 536, 635, 674, 678, 939, 3456, 20093, 30039
                ]

str_sort_list = [
                    'apple juice', 'butter', 'carrot', 'banana', 'apple',
                    'apple',
                ], [
                    'apple', 'apple', 'apple juice', 'banana', 'butter',
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


class ShellSortTest(TestCase):
    def test_is_sorted(self):
        a = int_sort_list[0].copy()
        shell_sort(a)
        self.assertEqual(a, int_sort_list[1])
        b = str_sort_list[0].copy()
        shell_sort(b)
        self.assertEqual(b, str_sort_list[1])


if __name__ == '__main__':
    run_tests()
