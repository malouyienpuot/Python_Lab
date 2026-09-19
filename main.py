"""Command-line entry point for the Python lab."""

from utils import celsius_to_fahrenheit, greet, is_even, square


def main():
    number = float(input("Enter a number: "))

    print(greet("Python learner"))
    print("Square:", square(number))
    print("The number is even." if is_even(number) else "The number is odd.")
    print("Fahrenheit:", celsius_to_fahrenheit(number))


if __name__ == "__main__":
    main()
