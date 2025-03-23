import unittest
from bike_rental_cal import calculate_rental_fee

class TestDataDrivenCalculateRentalFee(unittest.TestCase):
    # TC1: start_hour = -2.0, end_hour = 8.0, bike_type = "sport"
    def test_case_1(self):
        with self.assertRaises(ValueError) as context:
            calculate_rental_fee(-2.0, 8.0, "sport")
        self.assertEqual(str(context.exception), "Invalid rental time")

    # TC2: start_hour = 8.5, end_hour = 22.3, bike_type = "sport"
    def test_case_2(self):
        with self.assertRaises(ValueError) as context:
            calculate_rental_fee(8.5, 22.3, "sport")
        self.assertEqual(str(context.exception), "Invalid rental time")

    # TC3: start_hour = 9.0, end_hour = 7.6, bike_type = "sport"
    def test_case_3(self):
        with self.assertRaises(ValueError) as context:
            calculate_rental_fee(9.0, 7.6, "sport")
        self.assertEqual(str(context.exception), "Invalid rental duration")

    # TC4: start_hour = 10.5, end_hour = 12.5, bike_type = "regular"
    def test_case_4(self):
        fee = calculate_rental_fee(10.5, 12.5, "regular")
        self.assertAlmostEqual(fee, 180000)

    # TC5: start_hour = 13.4, end_hour = 15.8, bike_type = "sport"
    def test_case_5(self):
        fee = calculate_rental_fee(13.4, 15.8, "sport")
        self.assertAlmostEqual(fee, 324000)

    # TC6: start_hour = 7.3, end_hour = 8.0, bike_type = "sport"
    def test_case_6(self):
        fee = calculate_rental_fee(7.3, 8.0, "sport")
        self.assertAlmostEqual(fee, 105000)

    # TC7: start_hour = 8.8, end_hour = 12.0, bike_type = "regular"
    def test_case_7(self):
        fee = calculate_rental_fee(8.8, 12.0, "regular")
        self.assertAlmostEqual(fee, 256000)

    # TC8: start_hour = 16.2, end_hour = 17.5, bike_type = "regular"
    def test_case_8(self):
        fee = calculate_rental_fee(16.2, 17.5, "regular")
        self.assertAlmostEqual(fee, 130000)

    # TC9: start_hour = 17.4, end_hour = 16.7, bike_type = "regular"
    def test_case_9(self):
        with self.assertRaises(ValueError) as context:
            calculate_rental_fee(17.4, 16.7, "regular")
        self.assertEqual(str(context.exception), "Invalid rental duration")

    # TC10: start_hour = 7.5, end_hour = 10.8, bike_type = "sport"
    def test_case_10(self):
        fee = calculate_rental_fee(7.5, 10.8, "sport")
        self.assertAlmostEqual(fee, 396000)

    # TC11: start_hour = 13.6, end_hour = 16.6, bike_type = "regular"
    def test_case_11(self):
        fee = calculate_rental_fee(13.6, 16.6, "regular")
        self.assertAlmostEqual(fee, 240000)

if __name__ == "__main__":
    unittest.main(verbosity=2)