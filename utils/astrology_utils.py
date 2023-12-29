from decimal import Decimal, ROUND_HALF_UP

# Calculate Western Zodiac Sign
def calculate_zodiac_sign(azimuth):
    # Define azimuth ranges for each zodiac sign
    sign_ranges = [
        (0, 30), (30, 60), (60, 90), (90, 120),
        (120, 150), (150, 180), (180, 210), (210, 240),
        (240, 270), (270, 300), (300, 330), (330, 360)
    ]

    for i, (start, end) in enumerate(sign_ranges, start=1):
        if start <= azimuth < end:
            return i  # Return the zodiac sign number (1 to 12)

    return None  # Return None if no match is found

# Assign Western Zodiac sign a name
def get_zodiac_sign(constellation):
    # Mapping of constellation abbreviations to zodiac signs
    sign_mapping = {
        'Ari': 'Aries', 'Tau': 'Taurus', 'Gem': 'Gemini', 'Cnc': 'Cancer',
        'Leo': 'Leo', 'Vir': 'Virgo', 'Lib': 'Libra', 'Sco': 'Scorpio',
        'Sgr': 'Sagittarius', 'Cap': 'Capricorn', 'Aqr': 'Aquarius', 'Psc': 'Pisces'
    }
    
    return sign_mapping.get(constellation, 'Unknown')

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