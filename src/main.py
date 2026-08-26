from utils import celsius_to_fahrenheit, is_even, square


number = float(input("Enter a number: "))

print("Square:", square(number))
print("The number is even." if is_even(number) else "The number is odd.")
print("Fahrenheit:", celsius_to_fahrenheit(number))
