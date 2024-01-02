from geopy.geocoders import Nominatim

# Find Longitude and Latitude of Birth Place
def get_lat_long(location):
    geolocator = Nominatim(user_agent="Soul_Ties")

    try:
        location_info = geolocator.geocode(location)
        if location_info:
            latitude, longitude = location_info.latitude, location_info.longitude

            # Validate and parse birth date
            while True:
                months = [
                    'January', 
                    'February', 
                    'March', 
                    'April', 
                    'May', 
                    'June', 
                    'July', 
                    'August', 
                    'September', 
                    'October', 
                    'November', 
                    'December'
                ]
                try:
                    month = input("Birth Month: ")
                    if month in months:
                        month = months.index(month) + 1
                    else:
                        month = int(month)
                    if len(str(month)) != 2:
                        month = str(month).rjust(2, '0')
                    day = input("Birth Day: ")
                    if len(str(day)) != 2:
                        day = str(day).rjust(2, '0')
                    year = input("Birth Year: ")
                    if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                        date = f"{year}-{month}-{day}"
                        break
                    # date = input("Birth Date (Use two digit month, two digit day, and four digit year separated by '-'): ")
                    # date_parts = [int(part) for part in date.split('-')]
                    # if len(date_parts) == 3 and 1 <= date_parts[0] <= 12 and 1 <= date_parts[1] <= 31:
                    #     break
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
                            time = f'{split_time[0]:02d}:{split_time[1]:02d}'
                            return date, time, latitude, longitude
                            # Add an else block here to handle invalid periods
                        else:
                            print("Invalid period. Please enter 'am' or 'pm'.")
                    else:
                        print("Invalid time format. Please try again.")

                except ValueError:
                    print("Invalid time format. Please try again.")

            # Return default values or handle invalid date/time here

        else:
            print("Location not found.")
            return None  # Return a default value or handle this case accordingly

    except Exception as e:
        print(f"Error: {e}")
        return None  # Return a default value or handle this case accordingly