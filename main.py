from random import choice
from string import ascii_letters, digits, punctuation

print("Attention! The file passwords_PASGEN is rewritten every time you choose to save to file.")

length = int(input("Enter password length: "))
number_of_passwords = int(input("Enter the number of passwords: "))
special_symbols = input("Special characters required? (+/-): ")
mode = input("Display passwords on screen (+) or save to file (-)? (+/-): ") 

if mode == "-":
    print("Passwords saved to file passwords_PASGEN.txt")

    with open("passwords_PASGEN.txt", "w", encoding="utf-8") as file:
           file.write("Generated passwords:\n")

for _ in range(number_of_passwords):
    if special_symbols == "+":
        characters = ascii_letters + digits + punctuation
    else:
        characters = ascii_letters + digits
    password = ''.join(choice(characters) for _ in range(length))

    if mode == "-":
        with open("passwords_PASGEN.txt", "a", encoding="utf-8") as file:
            file.write(f"{password}\n")
    else:
         print(password)

input("Press Enter to exit...")