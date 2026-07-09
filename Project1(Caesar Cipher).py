import sys

a = input("Enter the text: ")
option = input("Brute Force(Y/N): ")
option = option.lower()
if option == "y":
    for i in range(1,27):
        decrypted = ""
        for letters in a:
            if letters == " ":
                decrypted += " "
            elif letters.islower():
                decrypted += chr((ord(letters)-97-i)%26+97)
            elif letters.isupper():
                decrypted += chr((ord(letters)-65-i)%26+65)
            else:
                decrypted += letters
    
        print(f"Decrypted Message #{i}: {decrypted}")
    
    sys.exit()
elif option == "n":
    key = int(input("Enter a key number: "))

    encrypted = ""
    decrypted = ""

    choice = int(input("1. Encrypt\n2. Decrypt\nEnter the choice number:"))
    if choice == 1:
        for letters in a:
            if letters == " ":
                encrypted += " "
            elif letters.islower():
                encrypted += chr((ord(letters)-97+key)%26+97)
            elif letters.isupper():
                encrypted += chr((ord(letters)-65+key)%26+65)
            else:
                encrypted += letters
        
        print(f"Your encrypted message is:\n{encrypted}")

    elif choice == 2:
        for letters in a:
            if letters == " ":
                decrypted += " "
            elif letters.islower():
                decrypted += chr((ord(letters)-97-key)%26+97)
            elif letters.isupper():
                decrypted += chr((ord(letters)-65-key)%26+65)
            else:
                decrypted += letters
        
        print(f"Your decrypted message is:\n{decrypted}")


    else:
        print("Invalid Choice")



