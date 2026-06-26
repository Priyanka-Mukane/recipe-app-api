"""

"""

from django.test import SimpleTestCase

from app import calc

class CalcTest(SimpleTestCase):

    def test_add_numbers(self):

        res = calc.add(5, 6)

        self.assertAlmostEqual(res, 12)

    
    def test_subtract_numbers(self):

        res = calc.subtract(5, 6)

        self.assertAlmostEqual(res, 5)
