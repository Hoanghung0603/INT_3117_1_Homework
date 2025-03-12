import unittest
from bike_rental_cal import calculate_rental_fee

class TestDataFlowCalculateRentalFee(unittest.TestCase):
    
    # Path 1
    def test_invalid_start_time(self):
        with self.assertRaises(ValueError) as context:
            calculate_rental_fee(4.5, 9.0, "sport")
        self.assertEqual(str(context.exception), "Invalid rental time")
    
    # Path 2
    def test_invalid_end_time(self):
        with self.assertRaises(ValueError) as context:
            calculate_rental_fee(13.0, 22.5, "regular")
        self.assertEqual(str(context.exception), "Invalid rental time")
    
    # Path 3
    def test_invalid_duration(self):
        with self.assertRaises(ValueError) as context:
            calculate_rental_fee(12.0, 12.0, "sport")
        self.assertEqual(str(context.exception), "Invalid rental duration")
    
    # Path 4
    def test_discount_10_percent(self):
        fee = calculate_rental_fee(9.3, 11.5, "regular")
        self.assertAlmostEqual(fee, 198000, places=6)
    
    # Path 5
    def test_no_discount(self):
        fee = calculate_rental_fee(7.3, 8.6, "regular")
        self.assertAlmostEqual(fee, 130000, places=6)
    
    # Path 6
    def test_discount_20_percent(self):
        fee = calculate_rental_fee(13.0, 16.0, "regular")
        self.assertAlmostEqual(fee, 240000, places=6)

if __name__ == "__main__":
    unittest.main()