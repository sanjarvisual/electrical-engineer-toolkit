import unittest

from eetoolkit.electrical.ohms_law import calculate


class TestOhmsLaw(unittest.TestCase):

    def test_voltage_and_resistance(self):
        result = calculate(voltage=12, resistance=6)

        self.assertEqual(result["current"], 2)
        self.assertEqual(result["power"], 24)

    def test_voltage_and_current(self):
        result = calculate(voltage=12, current=2)

        self.assertEqual(result["resistance"], 6)

    def test_current_and_resistance(self):
        result = calculate(current=2, resistance=6)

        self.assertEqual(result["voltage"], 12)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            calculate(voltage=12)


if __name__ == "__main__":
    unittest.main()
