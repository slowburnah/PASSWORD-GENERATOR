import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@']

print("Welcome to the PyPassword Generator!")
random_letters = int(input("How many letters would you like in your password?\n"))
random_numbers = int(input("How many numbers would you like?\n"))
random_symbols = int(input("How many symbols would you like?\n"))

#easy level(has a pattern)
#password = ""
# for char in range(1, random_letters, + 1):
#     password += random.choice(letters)
    
# for char in range(1, random_numbers, + 1):
#     password += random.choice(numbers)
    
# for char in range(1, random_symbols, + 1):
#     password += random.choice(symbols)
    
                 #OR

# for char in range(0, random_letters):
#     password += random.choice(letters)
    
# for char in range(0, random_numbers):
#     password += random.choice(numbers)
    
# for char in range(0, random_symbols):
#     password += random.choice(symbols)
    


# print(password)

#Hard level(no specific pattern)
password_combo = []
for char in range(0, random_letters):
    # password_combo += random.choice(letters)
    password_combo.append(random.choice(letters))
    
for char in range(0, random_numbers):
    # password_combo += random.choice(numbers)
    password_combo.append(random.choice(numbers))
    
for char in range(0, random_symbols):
    # password_combo += random.choice(symbols)
    password_combo.append(random.choice(symbols))

random.shuffle(password_combo)
print(password_combo)

password = ""
for char in password_combo:
    password += char
    
print(f"Your new password is: {password}")
