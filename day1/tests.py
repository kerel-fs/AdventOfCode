#!/usr/bin/env python3

import unittest
from inverse_captcha import get_solution


class TestInverseCaptchaMethod(unittest.TestCase):
    def test1(self):
        self.assertEqual(get_solution("1122"), 3)

    def test2(self):
        self.assertEqual(get_solution("1111"), 4)

    def test3(self):
        self.assertEqual(get_solution("1234"), 0)

    def test4(self):
        self.assertEqual(get_solution("91212129"), 9)


if __name__ == "__main__":
    unittest.main()
