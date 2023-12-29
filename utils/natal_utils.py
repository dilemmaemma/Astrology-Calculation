import ephem
from datetime import datetime
from utils.astrology_utils import get_zodiac_sign, get_chinese_zodiac
from utils.terminal_helpers import clear_terminal

# Calculate Natal Chart
def generate_natal_chart(birth_date, birth_time, latitude, longitude):
    birth_datetime_str = f"{birth_date} {birth_time}"
    birth_datetime = datetime.strptime(birth_datetime_str, '%m-%d-%Y %H:%M:%S')

    # Create an observer at the specified location
    observer = ephem.Observer()
    observer.lat, observer.lon = str(latitude), str(longitude)

    # Set the observer's date and time
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

    print("Planetary positions:")
    for planet in planets:
        planet.compute(observer)

        # Get the zodiac sign using the constellation function
        constellation_abbrev = ephem.constellation(planet)[1]
        zodiac_sign = get_zodiac_sign(planet.az % 360)
        print(f"{planet.name}: {planet.alt}° altitude, {planet.az}° azimuth")
        print(f"Zodiac Sign - {zodiac_sign}")

    # Calculate and print additional celestial bodies (if supported by ephem)
    try:
        additional_planets = [
            ephem.North_Node(),
            ephem.South_Node(),
            ephem.Lilith(),
            ephem.Juno(),
            ephem.Vesta(),
            ephem.Ceres(),
            ephem.Pallas(),
            ephem.Chiron(),
            ephem.Eros()
        ]

        for planet in additional_planets:
            planet.compute(observer)

            # Get the zodiac sign using the constellation function
            constellation_abbrev = ephem.constellation(planet)[1]
            zodiac_sign = get_zodiac_sign(constellation_abbrev) if constellation_abbrev else 'Unknown'
            print(f"{planet.name}: {planet.alt}° altitude, {planet.az}° azimuth")
            print(f"Zodiac Sign - {zodiac_sign}")

    except Exception as e:
        print(f"Error: {e}")
        print("Some celestial bodies are not supported by ephem.")
        
    # Use .triple() to get year, month, and day as a tuple
    year = observer.date.triple()[0]
    chinese_zodiac = get_chinese_zodiac(year)
    print(f"Chinese Zodiac - {chinese_zodiac}")