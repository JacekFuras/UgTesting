import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Jacek', 'Furas', 50000)
        self.emp_2 = Employee('Karol', 'Jedrzejewski', 60000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Jacek.Furas@email.com')
        self.assertEqual(self.emp_2.email, 'Karol.Jedrzejewski@email.com')

        self.emp_1.first = 'Karol'
        self.emp_2.first = 'Jacek'

        self.assertEqual(self.emp_1.email, 'Karol.Furas@email.com')
        self.assertEqual(self.emp_2.email, 'Jacek.Jedrzejewski@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Jacek Furas')
        self.assertEqual(self.emp_2.fullname, 'Karol Jedrzejewski')

        self.emp_1.first = 'Karol'
        self.emp_2.first = 'Jacek'

        self.assertEqual(self.emp_1.fullname, 'Karol Furas')
        self.assertEqual(self.emp_2.fullname, 'Jacek Jedrzejewski')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()