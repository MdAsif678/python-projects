import random
import string

try:
    length = int(input("Enter the length of the password you want: "))
except ValueError:
    print("Thats not a Valid Number.")
    exit()
    

num = input("Do you want numbers in your password(y/n): ")
if num != "y" and num != "n":
    print("Thats not a valid choice")
    exit()
sp_char = input("Do you want to have special characters in your password(y/n): ")
if sp_char != "y" and sp_char != "n":
    print("Thats not a valid choice")
    exit()

pool = string.ascii_letters
dig= string.digits
punc = string.punctuation

if num == "y":
    pool += dig

if sp_char == "y":
    pool += punc

password = ""

for passw in range(length):
    password += random.choice(pool)

print(password)