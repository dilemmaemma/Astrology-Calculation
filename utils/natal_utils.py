import ephem
from datetime import datetime
from utils.astrology_utils import get_zodiac_sign, get_chinese_zodiac, calculate_zodiac_sign
from utils.angles_utils import calculate_ascendant, calculate_descendant, calculate_midheaven, calculate_imum_coeli
from utils.terminal_helpers import clear_terminal

# Calculate Natal Chart
def generate_natal_chart(birth_date, birth_time, latitude, longitude):
    birth_datetime_str = f"{birth_date} {birth_time}"
    birth_datetime = datetime.strptime(birth_datetime_str, '%m-%d-%Y %H:%M:%S')

    observer = ephem.Observer()
    observer.lat, observer.lon = str(latitude), str(longitude)
    observer.date = birth_datetime

    # Calculate and print planetary positions
    planets = [
        ephem.Sun(),
        ephem.Moon(),
        ephem.Mercury(),
        ephem.Venus(),
        ephem.Mars(),
        ephem.Jupiter(),
        ephem.Saturn(),
        ephem.Uranus(),
        ephem.Neptune(),
        ephem.Pluto(),
    ]
    
    clear_terminal()
    # Calculate Planetary Positions
    print("Planetary positions:")
    for planet in planets:
        planet.compute(observer)

        # Get the zodiac sign based on the degree
        zodiac_sign = get_zodiac_sign(planet.az)
        
        # Print the information
        print(f"{planet.name}:")
        print(f"   Sign: {zodiac_sign}")
        print(f"   Degree: {planet.az}°")
        print(f"   House: {calculate_zodiac_sign(planet.az - ascendant)}")

    # Calculate and print additional celestial bodies (if supported by ephem)
    try:
        additional_planets = [
            ephem.North_Node(), ephem.South_Node(),
            ephem.Lilith(), ephem.Juno(), ephem.Vesta(),
            ephem.Ceres(), ephem.Pallas(), ephem.Chiron(), ephem.Eros()
        ]

        for planet in additional_planets:
            planet.compute(observer)

            # Get the zodiac sign based on the degree
            zodiac_sign = get_zodiac_sign(planet.az)
            
            # Print the information
            print(f"{planet.name}:")
            print(f"   Sign: {zodiac_sign}")
            print(f"   Degree: {planet.az}°")
            print(f"   House: {calculate_zodiac_sign(planet.az - ascendant)}")

    except Exception as e:
        print(f"Error: {e}")
        print("Some celestial bodies are not supported by ephem.")


    # Calculate AC, DC, MC, and IC
    
    # Calculate Ascendant (AC)
    ascendant = calculate_ascendant(observer)
    print(f"Ascendant: {ascendant}")
    
    # Calculate Descendant (DC)
    descendant = calculate_descendant(observer)
    print(f"Descendant: {descendant}")

    # Calculate Midheaven (MC)
    mc = calculate_midheaven(observer)
    print(f"Midheaven (MC): {mc}")

    # Calculate Imum Coeli (IC)
    ic = calculate_imum_coeli(observer)
    print(f"Imum Coeli (IC): {ic}")

    # Calculate and print Chinese zodiac sign
    # Use .triple() to get year, month, and day as a tuple
    
    year = observer.date.triple()[0]
    chinese_zodiac = get_chinese_zodiac(year)
    print(f"Chinese Zodiac - {chinese_zodiac}")