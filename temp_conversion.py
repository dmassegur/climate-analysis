"""
A module for converting temperature from Imperial to Metric units.
Will throw ValueErrors for temperatures < absolute zero.

Functions:
    convert_fahr_to_celsius: Converts Fahrenheit to Celsius
    convert_fahr_to_kelvin: Converts Fahrenheit to Kelvin
"""

def convert_fahr_to_celsius(fahr, precision):
    """
    Given a temperature in Fahrenheit, converts it to Celsius

    :param fahr: The temperature in Fahrenheit
    :param precision: number of significant digits of precision.
    :raises ValueError: If the temperature is below absolute zero
    :return: The temperature in Celsius
    """

    assert isinstance(precision, int)
    
    temp_celsius = (fahr - 32) * (5 / 9)
    
    if temp_celsius < -273.15:
        # If temperature is below absolute zero, throw an error.
        raise ValueError(f"Trying to convert impossible temperature: {fahr}F")
    return temp_celsius

def convert_fahr_to_kelvin(x):
    temp_kelvin = convert_fahr_to_celsius(x)
    temp_kelvin += 273.15
    assert temp_kelvin > 0.0
    return temp_kelvin
