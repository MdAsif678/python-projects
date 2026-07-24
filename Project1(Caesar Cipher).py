def caesar_cipher(text,key):
    result = ""
    for char in text:
        if char.isspace():
            result += " "
        elif char.islower():
            result += chr((ord(char)-97+key)%26+97)
        elif char.isupper():
            result += chr((ord(char)-65+key)%26+65)
        else:
            result += char

    return result

common_words = {
    "the","and","is","are","you","i","to","of",
    "in","that","it","for","on","with","this",
    "have","be","not","was","he","she","they",
    "we","hello","world"
}

print("WELCOME TO CAESAR CIPHER V2!!!")
while True:
    print("What would you like to do\n1. Encrypt a text message \n2. Decrypt a text message \n3. Brute force a message \n4. Exit")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            text = input("Enter the text to be encrypted: ")
            if not text:
                print("YOu need to enter some text to encrypt\n")
                continue
            key = int(input("Enter the Shift Value: "))
            key = key%26
            encrypted = caesar_cipher(text,key)
            print(f"\nYour encrypted message is:\n\"{encrypted}\"\n")

        elif choice == 2:
            text = input("Enter the text to be decrypted: ")
            if not text:
                print("YOu need to enter some text to encrypt\n")
                continue
            key = int(input("Enter the shift value: "))
            key = key%26
            decrypted = caesar_cipher(text,-key)
            print(f"\nYour decrypted message is:\n\"{decrypted}\"\n")

        elif choice == 3:
            text = input("Enter the text to be decrypted via brute force: ")
            if not text:
                print("You need to enter some text.\n")
                continue
            print("1. Show all guesses \n2. Show best guess only")
            try:
                choice2 = int(input("Enter your choice: "))
                if choice2 == 1:
                    print("Trying all Possible Keys: ")
                    scores = {}
                    for key in range(1,27):
                        score = 0
                        
                        decrypted = caesar_cipher(text,-key)
                        print(f"Key : {key}\n\n{decrypted}\n")
                        for words in decrypted.lower().split():
                            if words in common_words:
                                score += 1
                        scores[key] = score

                        print("-"*100)
                    best_key = max(scores, key=scores.get)
                    print(f"The Best key is: {best_key}\n")
                    print(f"text: \"{caesar_cipher(text,-best_key)}\"\n")
                    print("="*100+"\n")

                elif choice2 == 2:
                    scores = {}
                    for key in range(1,27):
                        score = 0
                        
                        decrypted = caesar_cipher(text,-key)
                        # print(f"Key : {key}\n\n{decrypted}\n")
                        for words in decrypted.lower().split():
                            if words in common_words:
                                score += 1
                        scores[key] = score

                    print("-"*100)
                    best_key = max(scores, key=scores.get)
                    print(f"The Best key is: {best_key}\n")
                    print(f"text: \"{caesar_cipher(text,-best_key)}\"\n")
                    print("="*100+"\n")

                else:
                    print("Choose form the choices above\n")
                    continue
            except ValueError:
                print("Not a valid choice")

        elif choice == 4:
            print("Thanks for using Caesar Cipher!\n")
            break

        else:
            print("Please choose an option from above\n")
            continue

    except ValueError:
        print("Please enter a valid choice\n")
        print("="*100)
        continue
    except KeyboardInterrupt:
        print("\nClosing Program")
        print("="*100)
        break



