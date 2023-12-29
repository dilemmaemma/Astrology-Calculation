from decimal import Decimal, ROUND_HALF_UP

# Calculate Western Zodiac Sign Degree
def calculate_zodiac_sign(degree):
    degree = degree % 360
    
    sign_ranges = [
        (0, 30), (30, 60), (60, 90), (90, 120),
        (120, 150), (150, 180), (180, 210), (210, 240),
        (240, 270), (270, 300), (300, 330), (330, 360)
    ]

    for i, (start, end) in enumerate(sign_ranges, start=1):
        if start <= degree < end:
            return i

    return None

# Calculate Western Zodiac Sign
def get_zodiac_sign(degree):
    sign_mapping = {
        1: 'Aries', 2: 'Taurus', 3: 'Gemini', 4: 'Cancer',
        5: 'Leo', 6: 'Virgo', 7: 'Libra', 8: 'Scorpio',
        9: 'Sagittarius', 10: 'Capricorn', 11: 'Aquarius', 12: 'Pisces'
    }
    
    sign_number = calculate_zodiac_sign(degree)
    return sign_mapping.get(sign_number, 'Unknown')

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