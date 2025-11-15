# temperature_converter.py
# Day 1: Temperature Converter CLI
# Author: Lawrence Alan Gomes
# Date: November 15, 2025
# A simple command-line tool to convert between Celsius and Fahrenheit

def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit"""
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius"""
    return (f - 32) * 5/9

def main():
    print("Temperature Converter CLI")
    print("Enter 'C' for C→F, 'F' for F→C, or 'Q' to quit\n")
    
    while True:
        # Get conversion type
        choice = input("Choose conversion (C/F/Q): ").strip().upper()
        
        if choice == 'Q':
            print("Goodbye!")
            break
        elif choice not in ['C', 'F']:
            print("Invalid choice. Please enter C, F, or Q.\n")
            continue
        
        # Get temperature input with error handling
        try:
            temp = float(input(f"Enter temperature in {'Celsius' if choice == 'C' else 'Fahrenheit'}: "))
        except ValueError:
            print("Error: Please enter a valid number.\n")
            continue
        
        # Perform conversion
        if choice == 'C':
            result = celsius_to_fahrenheit(temp)
            print(f"{temp}°C = {result:.2f}°F\n")
        else:  # choice == 'F'
            result = fahrenheit_to_celsius(temp)
            print(f"{temp}°F = {result:.2f}°C\n")

if __name__ == "__main__":
    main()