from decimal import Decimal, ROUND_HALF_UP

# Calculate Western Zodiac Sign
def get_zodiac_sign(degrees):
    # Define zodiac sign ranges (degrees)
    sign_ranges = [
        (0, 30), (30, 60), (60, 90), (90, 120),
        (120, 150), (150, 180), (180, 210), (210, 240),
        (240, 270), (270, 300), (300, 330), (330, 360)
    ]

    for i, (start, end) in enumerate(sign_ranges, start=1):
        if start <= degrees < end:
            return i  # Return the zodiac sign number (1 to 12)

    return None  # Return None if no match is found

# Calculate Chinese Zodiac sign
def get_chinese_zodiac(year):
    
    year = Decimal(year)
    
    # Calculate the remainder with precision
    remainder = (year % Decimal(12)).quantize(Decimal('0.000'), rounding=ROUND_HALF_UP)
    
    # Define the Chinese zodiac signs
    zodiac_signs = [
        'Monkey', 
        'Rooster', 
        'Dog', 
        'Pig', 
        'Rat', 
        'Ox', 
        'Tiger', 
        'Rabbit', 
        'Dragon', 
        'Snake', 
        'Horse', 
        'Sheep'
    ]
    return zodiac_signs[round(remainder)]