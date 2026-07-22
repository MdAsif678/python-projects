

print("Welcome to professional calculator!!")
while True:
    print("What operation do you want to perform: \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Exit")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("Enter numbers one by one.\nType 'done' when finished.")
            try:
                addition = float(input("Enter the first number: "))
                while True:
                
                    a = input("+ ")
                    if a.lower() == "done":
                        print(f"Total Sum: {addition}")
                        print("="*50)
                        break
                    addition += float(a)
            except ValueError:
                print("Not a valid Number")
        
        elif choice == 2:
            print("Enter numbers one by one.\nType 'done' when finished.")
            try:
                result = float(input("Enter first number: "))
                while True:
                
                    b = input("- ")
                    if b.lower() == "done":
                        print(f"Total Difference: {result}")
                        print("="*50)
                        break
                    result -= float(b)
            except ValueError:
                print("Not a valid Number")
                
        elif choice == 3:
            print("Enter numbers one by one.\nType 'done' when finished.")
            try:
                multi = float(input("Enter first number: "))
                while True:
                
                    b = input("x ")
                    if b.lower() == "done":
                        print(f"Total multiplication: {multi}")
                        print("="*50)
                        break
                    multi *= float(b)
            except ValueError:
                print("Not a valid Number")
        
        elif choice == 4:
            print("Enter numbers one by one.\nType 'done' when finished.")
            try:
                result = float(input("Enter first number: "))
                while True:
                    
                    b = input("/ ")
                    if b.lower() == "done":
                        print(f"Answer after division: {result}")
                        print("="*50)
                        break

                    b = float(b)
                    if b == 0:
                        print("Division by 0 not possible")
                        continue
                    result /= b
            except ValueError:
                print("Invalid Value")

        
        elif choice == 5:
            print("Thanks for using")
            break

        else:
            print("Choose a number between 1-5")
            print("="*100)
            continue
    except ValueError:
        print("Invalid Choice")
        print("="*50)
    except KeyboardInterrupt:
        print("\nProgram closed.")
        break
