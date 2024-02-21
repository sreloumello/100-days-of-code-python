import string
import random

print("PyPassword Generator")

letters = list(string.ascii_letters)
numbers = list(range(0,9+1))
symbols = list(string.punctuation)

hm_letters = int(input("How many letters would you like in your password: "))
hm_symbols = int(input("How many symbols would you like in your password: "))
hm_numbers = int(input("How many numbers would you like in your password: "))

password_letters = random.choices(letters, k=hm_letters)
password_symbols = random.choices(symbols, k=hm_symbols)
password_numbers = random.choices(numbers, k=hm_numbers)

password_list = password_letters + password_symbols + password_numbers
random.shuffle(password_list)

password = ""
for char in password_list:
    password += str(char)
print(f"Password Generated: {password}")