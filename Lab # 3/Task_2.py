# Write a Python program to convert temperatures to and from Celsius, Fahrenheit.
# [ Formula: c/5 = f-32/9 [ where c = temperature in Celsius and f = temperature in Fahrenheit ]

fahrenheit = float(input("Enter temperature in fahrenheit"))
celsius = (fahrenheit - 32)/1.8
print(str(fahrenheit )+ " degree Fahrenheit is equal to " + str(celsius ) + " degree Celsius." )

celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 1.8) + 32
print(str(celsius )+ " degree Celsius is equal to " + str(fahrenheit )+ " degree Fahrenheit.")

