# start_hour và end_hour có kiểu float, được làm tròn đến 3 chữ số thập phân 
def calculate_rental_fee(start_hour, end_hour, bike_type):
    if start_hour < 5.0 or start_hour > 21.0 or end_hour < 5.0 or end_hour > 21.0:
        raise ValueError("Invalid rental time")
    rental_duration = end_hour - start_hour
    hourly_rate = 150000 if bike_type == "sport" else 100000
    if rental_duration <= 0:
        raise ValueError("Invalid rental duration")
    
    if 2 <= rental_duration < 3:
        hourly_rate *= 0.9 # 10% discount
    elif rental_duration >= 3:
        hourly_rate *= 0.8 # 20% discount
    return hourly_rate * rental_duration