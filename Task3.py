# PASSWORD GENERATOR USING PYTHON #

import random
import string

# Function to generate a random password
def generate_password(length, complexity):
    # Defining the character sets to use in the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation 
    
    # Defining the list of character sets to use in the password
    if complexity == '1':
        character_sets = [lowercase_letters, uppercase_letters, digits]
    elif complexity == '2':
        character_sets = [lowercase_letters, uppercase_letters, digits, special_characters]
    else:
        print("Please Enter a valid choice.") 
    
    # Initializing an empty password string
    password = ''

    # Generate the password by randomly selecting characters from the character sets
    for i in range(length):
        character_set = random.choice(character_sets)
        password += random.choice(character_set)
    return password


# Main program
length = int(input("Enter password length: "))
complexity = input("Enter password complexity (1/2): ")
password = generate_password(length, complexity)
print("Your password is:", password)
