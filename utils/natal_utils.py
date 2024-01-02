import ephem
import json
from datetime import datetime

from immanuel.classes.serialize import ToJSON
from immanuel import charts
from immanuel.const import chart
from immanuel.setup import settings

from utils.astrology_utils import get_zodiac_sign, get_chinese_zodiac, calculate_zodiac_sign
# from utils.angles_utils import calculate_ascendant, calculate_descendant, calculate_midheaven, calculate_imum_coeli
from utils.terminal_helpers import clear_terminal

# Calculate Natal Chart
def generate_natal_chart(birth_date, birth_time, latitude, longitude):
        
    birth_datetime_str = f"{birth_date} {birth_time}"
    birth_datetime = datetime.strptime(birth_datetime_str, '%Y-%m-%d %H:%M')
    
    observer = ephem.Observer()
    observer.lat, observer.lon = str(latitude), str(longitude)
    observer.date = birth_datetime
    
    native = charts.Subject(
        datetime.fromisoformat(birth_datetime_str), 
        f'{latitude:.2f}n' if latitude > 0 else f'{abs(latitude):.2f}s', 
        f'{longitude:.2f}e' if longitude > 0 else f'{abs(longitude):.2f}w',
    )
    
    settings.objects.append(chart.ASC)
    settings.objects.append(chart.DESC)
    settings.objects.append(chart.MC)
    settings.objects.append(chart.IC)
    settings.objects.append(chart.TRUE_NORTH_NODE)
    settings.objects.append(chart.TRUE_SOUTH_NODE)
    settings.objects.append(chart.CHIRON)
    settings.objects.append(chart.LILITH)
    settings.objects.append(chart.PHOLUS)
    settings.objects.append(chart.CERES)
    settings.objects.append(chart.PALLAS)
    settings.objects.append(chart.JUNO)
    settings.objects.append(chart.VESTA)
    settings.objects.append(chart.VERTEX)
    
    natal = charts.Natal(native)
    
    clear_terminal()
    
    for object in natal.objects.values():
        print(f'Daytime: {natal.diurnal}')
        print(f'Moon phase: {natal.moon_phase}\n')

        for object in natal.objects.values():
            print(object)

        print()

        for index, aspects in natal.aspects.items():
            print(f'Aspects for {natal.objects[index].name}:')

            for aspect in aspects.values():
                print(f' - {aspect}')
        
    # Prints json format
    # print(json.dumps(natal.objects, cls=ToJSON, indent=4))

# Calculate Natal Chart
# def generate_natal_chart(birth_date, birth_time, latitude, longitude):
#     birth_datetime_str = f"{birth_date} {birth_time}"
#     birth_datetime = datetime.strptime(birth_datetime_str, '%m-%d-%Y %H:%M:%S')

#     observer = ephem.Observer()
#     observer.lat, observer.lon = str(latitude), str(longitude)
#     observer.date = birth_datetime

#     # Calculate and print planetary positions
#     planets = [
#         ephem.Sun(),
#         ephem.Moon(),
#         ephem.Mercury(),
#         ephem.Venus(),
#         ephem.Mars(),
#         ephem.Jupiter(),
#         ephem.Saturn(),
#         ephem.Uranus(),
#         ephem.Neptune(),
#         ephem.Pluto(),
#     ]
    
#     clear_terminal()
#     # Calculate Planetary Positions
#     print("Planetary positions:")
#     for planet in planets:
#         planet.compute(observer)

#         # Get the zodiac sign based on the degree
#         zodiac_sign = get_zodiac_sign(planet.az)
        
#         # Print the information
#         print(f"{planet.name}:")
#         print(f"   Sign: {zodiac_sign}")
#         print(f"   Degree: {planet.az}°")
#         print(f"   House: {calculate_zodiac_sign(planet.az - ascendant)}")

#     # Calculate and print additional celestial bodies (if supported by ephem)
#     try:
#         additional_planets = [
#             ephem.North_Node(), ephem.South_Node(),
#             ephem.Lilith(), ephem.Juno(), ephem.Vesta(),
#             ephem.Ceres(), ephem.Pallas(), ephem.Chiron(), ephem.Eros()
#         ]

#         for planet in additional_planets:
#             planet.compute(observer)

#             # Get the zodiac sign based on the degree
#             zodiac_sign = get_zodiac_sign(planet.az)
            
#             # Print the information
#             print(f"{planet.name}:")
#             print(f"   Sign: {zodiac_sign}")
#             print(f"   Degree: {planet.az}°")
#             print(f"   House: {calculate_zodiac_sign(planet.az - ascendant)}")

#     except Exception as e:
#         print(f"Error: {e}")
#         print("Some celestial bodies are not supported by ephem.")


#     # Calculate AC, DC, MC, and IC
    
#     # Calculate Ascendant (AC)
#     ascendant = calculate_ascendant(observer)
#     print(f"Ascendant: {ascendant}")
    
#     # Calculate Descendant (DC)
#     descendant = calculate_descendant(observer)
#     print(f"Descendant: {descendant}")

#     # Calculate Midheaven (MC)
#     mc = calculate_midheaven(observer)
#     print(f"Midheaven (MC): {mc}")

#     # Calculate Imum Coeli (IC)
#     ic = calculate_imum_coeli(observer)
#     print(f"Imum Coeli (IC): {ic}")

    # Calculate and print Chinese zodiac sign
    # Use .triple() to get year, month, and day as a tuple
    
    year = observer.date.triple()[0]
    chinese_zodiac = get_chinese_zodiac(year)
    print(f"Chinese Zodiac - {chinese_zodiac}")