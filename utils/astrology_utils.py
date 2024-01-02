from decimal import Decimal, ROUND_HALF_UP

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