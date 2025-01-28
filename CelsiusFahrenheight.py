def toFahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Enter the temperature in Celsius: "))
print(f"{celsius}°C is equal to {toFahrenheit(celsius)}°F")
