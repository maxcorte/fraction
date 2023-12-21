import unittest
from main import Fraction


class TestFraction(unittest.TestCase):
    def test_initialization(self):
        fraction = Fraction(0, 1)
        self.assertEqual(fraction.numerateur, 0)
        self.assertEqual(fraction.denominateur, 1)
        fraction2 = Fraction(5, 10)
        self.assertEqual(fraction2.numerateur, 1)
        self.assertEqual(fraction2.denominateur, 2)
        fraction3 = Fraction(1, 4)
        self.assertEqual(fraction3.numerateur, 1)
        self.assertEqual(fraction3.denominateur, 4)
        self.assertRaises(ZeroDivisionError, Fraction, 6, 0)

    def test_addition(self):
        fraction1 = Fraction(1, 2)
        fraction2 = Fraction(3, 4)
        fraction3 = Fraction(1, 4)
        fraction4 = Fraction(0, 4)
        result = fraction2 + fraction3
        result2 = fraction1 + fraction2
        result3 = fraction1 + fraction4
        result4 = fraction1 + fraction3
        self.assertEqual(result, Fraction(1, 1))
        self.assertEqual(result2, Fraction(5, 4))
        self.assertEqual(result3, Fraction(1, 2))
        self.assertEqual(result4, Fraction(3, 4))

    def test_subtraction(self):
        fraction1 = Fraction(1, 2)
        fraction2 = Fraction(3, 4)
        fraction3 = Fraction(1, 4)
        fraction4 = Fraction(0, 4)
        result = fraction2 - fraction3
        result2 = fraction1 - fraction2
        result3 = fraction1 - fraction4
        result4 = fraction1 - fraction3
        self.assertEqual(result, Fraction(1, 2))
        self.assertEqual(result2, Fraction(-1, 4))
        self.assertEqual(result3, Fraction(1, 2))
        self.assertEqual(result4, Fraction(1, 4))

    def test_multiplication(self):
        fraction1 = Fraction(2, 3)
        fraction2 = Fraction(1, 2)
        fraction3 = Fraction(0, 2)
        fraction4 = Fraction(16, 4)
        result = fraction1 * fraction2
        result2 = fraction1 * fraction3
        result3 = fraction1 * fraction4
        result4 = fraction2 * fraction3
        self.assertEqual(result, Fraction(1, 3))
        self.assertEqual(result2, Fraction(0, 1))
        self.assertEqual(result3, Fraction(8, 3))
        self.assertEqual(result4, Fraction(0, 1))

    def test_division(self):
        fraction1 = Fraction(2, 3)
        fraction2 = Fraction(1, 2)
        fraction3 = Fraction(16, 4)
        self.assertRaises(ZeroDivisionError, Fraction, 2, 0)
        result = fraction1 / fraction2
        result2 = fraction1 / fraction3
        result3 = fraction2 / fraction3
        self.assertEqual(result, Fraction(4, 3))
        self.assertEqual(result2, Fraction(1, 6))
        self.assertEqual(result3, Fraction(1, 8))

    def test_power(self):
        fraction = Fraction(2, 3)
        fraction2 = Fraction(1, 2)
        result = fraction ** 2
        result2 = fraction2 ** 8
        self.assertEqual(result, Fraction(4, 9))
        self.assertEqual(result2, Fraction(1, 256))
        with self.assertRaises(ValueError):
            fraction ** -1
            fraction ** 0
            fraction ** 1.5

    def test_nombre_mixte(self):
        fraction = Fraction(2, 3)
        fraction2 = Fraction(1, 2)
        fraction3 = Fraction(5, 2)
        fraction4 = Fraction(0, 2)
        fraction5 = Fraction(2, 1)
        result = fraction.nombre_mixte()
        result2 = fraction2.nombre_mixte()
        self.assertEqual(result, "2/3")
        self.assertEqual(result2, "1/2")
        self.assertEqual(fraction3.nombre_mixte(), "2 + 1/2")
        with self.assertRaises(ValueError):
            fraction4.nombre_mixte()
            fraction5.nombre_mixte()

    def test_equality(self):
        fraction1 = Fraction(2, 3)
        fraction2 = Fraction(4, 6)
        fraction3 = Fraction(1, 2)
        fraction4 = Fraction(0, 2)
        fraction5 = Fraction(0, 1)
        self.assertEqual(fraction1 == fraction2, True)
        self.assertEqual(fraction1 == fraction3, False)
        self.assertEqual(fraction4 == fraction5, True)

    def test_float_conversion(self):
        fraction = Fraction(12, 3)
        fraction2 = Fraction(1, 1)
        fraction3 = Fraction(1, 4)
        result2 = fraction3.__float__()
        self.assertEqual(result2, 0.25)
        with self.assertRaises(ValueError):
            fraction.__float__()
            fraction2.__float__()

    def test_zero_check(self):
        fraction = Fraction(0, 5)
        fraction2 = Fraction(1, 5)
        self.assertEqual(fraction.est_nulle(), True)
        self.assertEqual(fraction2.est_nulle(), False)

    def test_integer_check(self):
        fraction = Fraction(7, 1)
        fraction2 = Fraction(7, 5)
        fraction3 = Fraction(-2, 1)
        self.assertEqual(fraction.est_entiere(), True)
        self.assertEqual(fraction2.est_entiere(), False)
        self.assertEqual(fraction3.est_entiere(), True)

    def test_proper_fraction_check(self):
        fraction = Fraction(5, 3)
        fraction2 = Fraction(4, 1)
        fraction3 = Fraction(0, 1)
        fraction4 = Fraction(1, 2)
        self.assertEqual(fraction.est_une_fraction_propre(), False)
        self.assertEqual(fraction4.est_une_fraction_propre(), True)
        with self.assertRaises(ValueError):
            fraction2.est_une_fraction_propre()
            fraction3.est_une_fraction_propre()

    def test_unitary_fraction_check(self):
        fraction = Fraction(1, 5)
        fraction2 = Fraction(5, 1)
        fraction3 = Fraction(0, 7)
        fraction4 = Fraction(7, 14)
        fraction5 = Fraction(3, 2)
        self.assertEqual(fraction.est_unitaire(), True)
        self.assertEqual(fraction4.est_unitaire(), True)
        self.assertEqual(fraction5.est_unitaire(), False)
        with self.assertRaises(ValueError):
            fraction2.est_unitaire()
            fraction3.est_unitaire()

    def test_adjacent_check(self):
        fraction1 = Fraction(2, 3)
        fraction2 = Fraction(3, 4)
        fraction3 = Fraction(5, 2)
        fraction4 = Fraction(0, 1)
        self.assertEqual(fraction1.est_adjacente(fraction2), True)
        self.assertEqual(fraction3.est_adjacente(fraction2), False)
        self.assertEqual(fraction4.est_adjacente(fraction2), False)

    def test_str_representation(self):
        fraction = Fraction(3, 4)
        self.assertEqual(str(fraction), "3/4")

        fraction = Fraction(5, 2)
        self.assertEqual(str(fraction), "5/2")

        fraction = Fraction(6, 1)
        self.assertEqual(str(fraction), "6/1")

        fraction = Fraction(0, 8)
        self.assertEqual(str(fraction), "0/1")

    def test_other_param(self):
        fraction = Fraction(3, 4)
        fraction2 = Fraction(5, 2)
        other = 5
        result = fraction.other_param(fraction2)
        self.assertEqual(result, fraction2)
        self.assertEqual(fraction.other_param(other), Fraction(5, 1))
        with self.assertRaises(ValueError):
            fraction.other_param("2")

    def test_ppcm(self):
        fractions = Fraction(6, 4)
        result = fractions.ppcm(6, 4)
        self.assertEqual(result, 12)


if __name__ == '__main__':
    unittest.main()
