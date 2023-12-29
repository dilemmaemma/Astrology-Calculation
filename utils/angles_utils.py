import ephem
from astrology_utils import get_zodiac_sign

# Calculate Ascendant Sign
def calculate_ascendant(observer):
    sun = ephem.Sun(observer)

    # Calculate the Ascendant (rising sign)
    ascendant = ephem.constellation(sun)[1]
    return ascendant

# Calculate Descendant Sign
def calculate_descendant(observer):
    sun = ephem.Sun(observer)

    # Calculate the Descendant
    # Add 180 degrees to the Ascendant
    descendant_deg = (ephem.constellation(sun)[1] + 6) % 12
    descendant = get_zodiac_sign(descendant_deg)
    return descendant

# Calculate Midheaven Sign
def calculate_midheaven(observer):
    sun = ephem.Sun(observer)

    # Calculate the Midheaven (MC)
    # Add 90 degrees to the Ascendant
    mc_deg = (ephem.constellation(sun)[1] + 3) % 12
    mc = get_zodiac_sign(mc_deg)
    return mc

# Calculate Imum Coeli Sign
def calculate_imum_coeli(observer):
    sun = ephem.Sun(observer)

    # Calculate the Imum Coeli (IC)
    # Add 270 degrees to the Ascendant
    ic_deg = (ephem.constellation(sun)[1] + 9) % 12
    ic = get_zodiac_sign(ic_deg)
    return ic