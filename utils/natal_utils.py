import ephem
import json
from datetime import datetime

from immanuel.classes.serialize import ToJSON
from immanuel import charts
from immanuel.const import chart
from immanuel.setup import settings

from utils.astrology_utils import get_chinese_zodiac
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
    
    # Can generate a composite chart with the following:
        # composite = charts.Composite(native, partner)
    
    # for object in natal.objects.values():
    #     print(f'Daytime: {natal.diurnal}')
    #     print(f'Moon phase: {natal.moon_phase}\n')

    #     for object in natal.objects.values():
    #         print(object)

    #     print()

    #     for index, aspects in natal.aspects.items():
    #         print(f'Aspects for {natal.objects[index].name}:')

    #         for aspect in aspects.values():
    #             print(f' - {aspect}')
    
    for objects in natal.objects.values():
        print(objects)
        
    # Prints json format
    # print(json.dumps(natal.objects, cls=ToJSON, indent=4))

    # Calculate and print Chinese zodiac sign
    # Use .triple() to get year, month, and day as a tuple
    
    year = observer.date.triple()[0]
    chinese_zodiac = get_chinese_zodiac(year)
    print()
    print(f"Chinese Zodiac - {chinese_zodiac}")