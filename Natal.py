from geopy.geocoders import Nominatim
import ephem

# Calculate Zodiac Sign
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

def get_zodiac_sign(constellation):
    # Mapping of constellation abbreviations to zodiac signs
    sign_mapping = {
        'Ari': 'Aries', 'Tau': 'Taurus', 'Gem': 'Gemini', 'Cnc': 'Cancer',
        'Leo': 'Leo', 'Vir': 'Virgo', 'Lib': 'Libra', 'Sco': 'Scorpio',
        'Sgr': 'Sagittarius', 'Cap': 'Capricorn', 'Aqr': 'Aquarius', 'Psc': 'Pisces'
    }
    
    return sign_mapping.get(constellation, 'Unknown')

def get_chinese_zodiac(year):
    year = int(year)
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
    remainder = round((year % 12) % 1, 3) # Round the three decimal remainder
    print(remainder)
    print(year)
    zodiac_index = int(remainder * 12) # Take the number to the left of the decimal
    return zodiac_signs[zodiac_index]

# Calculate Natal Chart
def generate_natal_chart(birth_date, birth_time, latitude, longitude):
    birth_datetime = f"{birth_date} {birth_time}"

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

    print("Planetary positions:")
    for planet in planets:
        planet.compute(observer)

        # Get the zodiac sign using the constellation function
        _, constellation_abbrev = ephem.constellation(planet)
        zodiac_sign = get_zodiac_sign(constellation_abbrev)
        print(f"{planet.name}: {planet.alt}° altitude, {planet.az}° azimuth")
        print(f"Zodiac Sign - {zodiac_sign}")
    chinese_zodiac = get_chinese_zodiac(observer.date.datetime().year)
    print(f"Chinese Zodiac - {chinese_zodiac}")
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
            _, constellation_abbrev = ephem.constellation(planet)
            zodiac_sign = get_zodiac_sign(constellation_abbrev)
            print(f"{planet.name}: {planet.alt}° altitude, {planet.az}° azimuth")
            print(f"Zodiac Sign - {zodiac_sign}")

    except Exception as e:
        print(f"Error: {e}")
        print("Some celestial bodies are not supported by ephem.")
        
# Find Longitude and Latitude of Birth Place
def get_lat_long(location):
    geolocator = Nominatim(user_agent="Soul_Ties")
    
    try:
        location_info = geolocator.geocode(location)
        if location_info:
            latitude, longitude = location_info.latitude, location_info.longitude
            
            # Validate and parse birth date
            while True:
                try:
                    date = input("Birth Date (Use two digit month, two digit day, and four digit year separated by '-'): ")
                    date_parts = [int(part) for part in date.split('-')]
                    if len(date_parts) == 3 and 1 <= date_parts[0] <= 12 and 1 <= date_parts[1] <= 31:
                        break
                    else:
                        print("Invalid date format. Please try again.")
                except ValueError:
                    print("Invalid date format. Please try again.")

            # Validate and parse birth time
            while True:
                try:
                    time = input("Birth Time (Please separate by ':'): ")
                    tod = input("am or pm: ")
                    split_time = [int(part) for part in time.split(':')]

                    # Check the time format
                    if len(split_time) == 2 and 0 <= split_time[0] <= 23 and 0 <= split_time[1] <= 59:
                        # Check the validity of the period (am/pm)
                        if tod.lower() == 'am' or tod.lower() == 'pm':
                            if tod.lower() == 'pm' and split_time[0] < 12:
                                split_time[0] += 12
                            time = f'{split_time[0]:02d}:{split_time[1]:02d}:00'
                            break
                            # Add an else block here to handle invalid periods
                        else:
                            print("Invalid period. Please enter 'am' or 'pm'.")
                    else:
                        print("Invalid time format. Please try again.")

                except ValueError:
                    print("Invalid time format. Please try again.")
            
            generate_natal_chart(date, time, latitude, longitude)
            
        else:
            print("Location not found.")
    except Exception as e:
        print(f"Error: {e}")
        
location = input("Birth Place: ")
get_lat_long(location)