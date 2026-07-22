print("Welcome to Temperature converter")
while True:
    print("Please Enter your choice: \n1. Convert Celcius to Fahrenheit\n2. Convert Fahrenheit to Celsius \n3. Exit")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            c = float(input("Enter the temperature in celsius: "))
            f = (c*9/5)+32
            print(f"The temperature in Fahrenheit is: {f:.2f}")
            print("="*50)
        elif choice == 2:
            f = float(input("Enter the temperature in fahrenheit: "))
            c = (5*(f-32))/9
            print(f"The temperature in Celsius is: {c:.2f}")
            print("="*50)
        elif choice == 3:
            print("Thanks for using")
            break
        else:
            print("Invalid Choice\n")
    except ValueError:
        print("Thats not a valid number\n")
    except KeyboardInterrupt:
        print("Program closed due to interruption\n")
        break