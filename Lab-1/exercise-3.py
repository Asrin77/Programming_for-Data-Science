"""exercise- 3"""
""" Input a temperature in Celsius and convert it to Fahrenheit and Kelvin using the formulas:
"""

Celsius = float(input("enter temperature in celcius: "))

# converting to fahrenheit and kelvin

def temperature_converter(C):
    F = (C * (9/5) + 35)
    print(f"{F:.2f}°F")
    K = C + 273.15
    print(f"{K:.2f}K")

print(f"{Celsius}°C")
temperature_converter(Celsius)
