"""
Contains all of the unit tests for
random_person_generator.py.
Since the random module was used heavily
in random_person_generator.py, mock objects
were used to facilitate testing.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).absolute().parent.parent))

import unittest
import random_person_generator as r
from unittest.mock import patch


class TestRandomPerson(unittest.TestCase):

    @patch('random_person_generator.male_first_name')
    def test_read_male_first_names(self, mocked):
        mocked.return_value = 'Matt'
        self.assertEqual(r.male_first_name(), 'Matt')

    @patch('random_person_generator.female_first_name')
    def test_read_female_first_names(self, mocked):
        mocked.return_value = 'Jenny'
        self.assertEqual(r.female_first_name(), 'Jenny')

    @patch('random_person_generator.surname')
    def test_read_surnames(self, mocked):
        mocked.return_value = 'King'
        self.assertEqual(r.surname(), 'King')

    @patch('random_person_generator.generate_random_name')
    def test_read_full_name(self, mocked):
        mocked.return_value = 'Jenny King'
        self.assertEqual(r.generate_random_name(), 'Jenny King')

    @patch('random_person_generator.random_age')
    def test_read_age(self, mocked):
        mocked.return_value = 5
        self.assertEqual(r.random_age(), 5)

    def test_read_age_min_out_of_range(self):
        try:
            result = r.random_age(min=-5, max=50)
        except Exception as e:
            self.assertIsInstance(e, ValueError)
        else:
            self.fail("Did not raise exception")

    def test_read_age_max_out_of_range(self):
        try:
            result = r.random_age(min=3, max=150)
        except Exception as e:
            self.assertIsInstance(e, ValueError)
        else:
            self.fail("Did not raise exception")

    @patch('random_person_generator.random_email_service')
    def test_read_email_service(self, mocked):
        mocked.return_value = 'yahoo'
        self.assertEqual(r.random_email_service(), 'yahoo')

    def test_generate_random_phone_digit_nonZero(self):
        self.assertTrue(1 <= r.generate_random_phone_digit() <= 9)

    def test_generate_random_phone_digit_withZero(self):
        self.assertTrue(0 <= r.generate_random_phone_digit(False) <= 9)

    @patch('random_person_generator.random_phone_number')
    def test_read_phone_number(self, mocked):
        mocked.return_value = '123-456-7899'
        self.assertEqual(r.random_phone_number(), '123-456-7899')

    def test_read_phone_number_first_digit_not_zero(self):
        self.assertNotEqual(r.random_phone_number()[0], '0')

    def test_read_phone_has_correct_length(self):
        self.assertEqual(len(r.random_phone_number()), 12)

    def test_read_phone_has_dashes_as_separators(self):
        result = r.random_phone_number()
        self.assertEqual(result[3], '-')
        self.assertEqual(result[7], '-')

    @patch('random_person_generator.create_occupation')
    def test_create_occupation(self, mocked):
        mocked.return_value = 'astronaut'
        self.assertEqual(r.create_occupation(age=50), 'astronaut')

    def test_create_occupation_young_person(self):
        self.assertEqual(r.create_occupation(age=3), 'NA')

    def test_create_occupation_teenager(self):
        self.assertEqual(r.create_occupation(age=16), 'student')

    def test_create_occupation_invalid_age(self):
        try:
            result = r.create_occupation(age=-5)
        except Exception as e:
            self.assertIsInstance(e, ValueError)
        else:
            self.fail("Did not raise exception")

    @patch('random_person_generator.create_person')
    def test_create_person(self, mocked):
        mocked.return_value = {
            'first_name': 'Darnell',
            'last_name': 'Tannenbaum',
            'email': 'darnell.tannenbaum@aol.com',
            'sex': 'female',
            'age': 20,
            'job': 'programmer',
            'phone': '232-40-882'
            }
        expected_output = {
            'first_name': 'Darnell',
            'last_name': 'Tannenbaum',
            'email': 'darnell.tannenbaum@aol.com',
            'sex': 'female',
            'age': 20,
            'job': 'programmer',
            'phone': '232-40-882'
        }
        self.assertDictEqual(r.create_person(), expected_output)


if __name__ == '__main__':
    unittest.main()
