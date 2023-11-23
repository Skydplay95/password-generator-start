#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
""""
#declare and initialize var, no space in "" if there is one, it will count as a caractere
password_letters = ""
password_symbols = ""
password_numbers = ""

#choose random letter in the list
for letter in letters:
    if len(password_letters) < nr_letters:
        password_letters += random.choice(letters)
print(password_letters)

#choose random symbol in the list
for symbol in symbols:
    if len(password_symbols) < nr_symbols:
        password_symbols += random.choice(symbols)
print(password_symbols)

#choose random number in the list
for number in numbers:
    if len(password_numbers) < nr_numbers:
        password_numbers += random.choice(numbers)
print(password_numbers)

password = password_letters + password_numbers + password_symbols

#print the password
print(password)
"""
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#declare and initialize var, no space in "" if there is one, it will count as a caractere
password_letters = ""
password_symbols = ""
password_numbers = ""

#choose random letter in the list
for letter in letters:
    if len(password_letters) < nr_letters:
        password_letters += random.choice(letters)
print(password_letters)

#choose random symbol in the list
for symbol in symbols:
    if len(password_symbols) < nr_symbols:
        password_symbols += random.choice(symbols)
print(password_symbols)

#choose random number in the list
for number in numbers:
    if len(password_numbers) < nr_numbers:
        password_numbers += random.choice(numbers)
print(password_numbers)

#creater a new list which contains all the char already chosen before
password_char = []
password_char.extend(password_numbers)
password_char.extend(password_symbols)
password_char.extend(password_letters)

print(password_char)

#create a new list which is a copy of the one create above
password_shuffle = password_char.copy()

#shuffle the new list to give random char order == safer password
random.shuffle(password_shuffle)

#declare and initialize password
password = ""
#add all char in the shuffle list to password
for char in password_shuffle:
    password += char

#print password
print(password_shuffle)
print(password)
