from utils.natal_utils import generate_natal_chart
from utils.geolocation_utils import get_lat_long
from utils.terminal_helpers import clear_terminal

def main():
    clear_terminal()
    location = input("Birth Place: ")
    birth_date, birth_time, latitude, longitude = get_lat_long(location)
    generate_natal_chart(birth_date, birth_time, latitude, longitude)

if __name__ == "__main__":
    main()
