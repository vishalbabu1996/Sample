def temperature_converter():
    print("Temperature Converter")
    print("1. Convert from Celsius to Fahrenheit")
    print("2. Convert from Fahrenheit to Celsius")
    
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        try:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C is equal to {fahrenheit}°F")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    elif choice == '2':
        try:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit}°F is equal to {celsius}°C")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        print("Invalid choice. Please choose 1 or 2.")

def length_converter():
    print("Length Converter")
    print("1. Convert from meters to feet")
    print("2. Convert from feet to meters")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        try:
            meters = float(input("Enter length in meters: "))
            feet = meters * 3.28084
            print(f"{meters} meters is equal to {feet} feet")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    elif choice == '2':
        try:
            feet = float(input("Enter length in feet: "))
            meters = feet / 3.28084
            print(f"{feet} feet is equal to {meters} meters")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        print("Invalid choice. Please choose 1 or 2.")

def weight_converter():
    print("Weight Converter")
    print("1. Convert from kilograms to pounds")
    print("2. Convert from pounds to kilograms")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        try:
            kilograms = float(input("Enter weight in kilograms: "))
            pounds = kilograms * 2.20462
            print(f"{kilograms} kilograms is equal to {pounds} pounds")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    elif choice == '2':
        try:
            pounds = float(input("Enter weight in pounds: "))
            kilograms = pounds / 2.20462
            print(f"{pounds} pounds is equal to {kilograms} kilograms")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        print("Invalid choice. Please choose 1 or 2.")

def main():
    while True:
        print("Unit Converter Menu")
        print("1. Temperature Converter")
        print("2. Length Converter")
        print("3. Weight Converter")
        print("4. Quit")
        
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            temperature_converter()
        elif choice == '2':
            length_converter()
        elif choice == '3':
            weight_converter()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")

if name == "main":
    main()
