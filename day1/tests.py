#!/usr/bin/env python3

import unittest
from inverse_captcha import get_solution_part1, get_solution_part2


class TestInverseCaptchaPart1Method(unittest.TestCase):
    def test1(self):
        self.assertEqual(get_solution_part1("1122"), 3)

    def test2(self):
        self.assertEqual(get_solution_part1("1111"), 4)

    def test3(self):
        self.assertEqual(get_solution_part1("1234"), 0)

    def test4(self):
        self.assertEqual(get_solution_part1("91212129"), 9)


class TestInverseCaptchaPart2Method(unittest.TestCase):
    def test1(self):
        self.assertEqual(get_solution_part2("1212"), 6)

    def test2(self):
        self.assertEqual(get_solution_part2("1221"), 0)

    def test3(self):
        self.assertEqual(get_solution_part2("123425"), 4)

    def test4(self):
        self.assertEqual(get_solution_part2("123123"), 12)

    def test5(self):
        self.assertEqual(get_solution_part2("12131415"), 4)


if __name__ == "__main__":
    unittest.main()
