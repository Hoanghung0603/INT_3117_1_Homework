import unittest
from bike_rental_cal import calculate_rental_fee

class TestBlackBoxCalculateRentalFee(unittest.TestCase):
    # Kiểm thử giá trị biên cho end_hour (với start_hour cố định = 13.00, bike_type là "regular")
    def test_end_hour_boundaries(self):
        start_hour = 13.00
        btype = "regular"
        # (end_hour, expected_output)
        test_cases = [
            (5.00, "Invalid rental duration"),   
            (5.02, "Invalid rental duration"),   
            (13.00, "Invalid rental duration"),  
            (20.98, 638400),                      
            (21.00, 640000),                      
            (4.98, "Invalid rental time"),        
            (21.02, "Invalid rental time"),       
        ]
        for end_hour, expected in test_cases:
            with self.subTest(end_hour=end_hour):
                if isinstance(expected, str):
                    with self.assertRaises(ValueError) as error_context:
                        calculate_rental_fee(start_hour, end_hour, btype)
                    self.assertEqual(str(error_context.exception), expected)
                else:
                    result = calculate_rental_fee(start_hour, end_hour, btype)
                    self.assertAlmostEqual(result, expected, places = 6)

    # Kiểm thử giá trị biên cho start_hour (với end_hour cố định = 13.00, bike_type là "regular")
    def test_start_hour_boundaries(self):
        end_hour = 13.00
        btype = "regular"
        # (start_hour, expected_output)
        test_cases = [
            (5.00, 640000),                      
            (5.02, 638400),                       
            (20.98, "Invalid rental duration"),   
            (21.00, "Invalid rental duration"),   
            (4.98, "Invalid rental time"),        
            (21.02, "Invalid rental time"),       
        ]
        for start_hour, expected in test_cases:
            with self.subTest(start_hour=start_hour):
                if isinstance(expected, str):
                    with self.assertRaises(ValueError) as error_context:
                        calculate_rental_fee(start_hour, end_hour, btype)
                    self.assertEqual(str(error_context.exception), expected)
                else:
                    result = calculate_rental_fee(start_hour, end_hour, btype)
                    self.assertAlmostEqual(result, expected, places=6)

    # Kiểm thử theo bảng quyết định
    def test_decision_table(self):
        #((start_hour, end_hour, bike_type), expected_output)
        test_cases = [
            ((4.00, 7.00, "regular"), "Invalid rental time"),      
            ((15.00, 14.00, "regular"), "Invalid rental duration"), 
            ((8.00, 10.50, "regular"), 225000),                      
            ((14.00, 17.10, "regular"), 248000),                    
            ((7.00, 8.00, "regular"), 100000),                      
            ((20.00, 22.00, "sport"), "Invalid rental time"),      
            ((10.50, 8.20, "sport"), "Invalid rental duration"),   
            ((17.00, 19.20, "sport"), 297000),                       
            ((6.00, 9.40, "sport"), 408000),                       
            ((11.00, 11.50, "sport"), 75000),                       
        ]
        for (start_hour, end_hour, bike_type), expected in test_cases:
            with self.subTest(start_hour=start_hour, end_hour=end_hour, bike_type=bike_type):
                if isinstance(expected, str):
                    with self.assertRaises(ValueError) as error_context:
                        calculate_rental_fee(start_hour, end_hour, bike_type)
                    self.assertEqual(str(error_context.exception), expected)
                else:
                    result = calculate_rental_fee(start_hour, end_hour, bike_type)
                    self.assertAlmostEqual(result, expected, places=6)

if __name__ == '__main__':
    unittest.main()