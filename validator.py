special_characters = ['&', '#', '$', '!', '?', '"', '(', ')', '.']

alphabetic_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
                                                                                                                          'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

digit= ['0','1','2','3','4','5','6','7','8','9']
import sys 

# Define fixed values here
min_length = 9
max_length = 12

special_characters_number = 0
alphabetic_characters_number = 0
digit_number= 0

# Write your code here
print('Enter your password for validation.')
print('The passsword should meet the fiollowing rules:')
print('1. Length is between(9, 12)') 
print('2. Value has at least 5 regular characters')
print('3. Value has at least 3 special characters')
password = input('Your Password: ')

if len(password) < min_length:
    print(f"Invalid password! Length of password less than {min_length}")


elif len(password) >= min_length and len(password) <= max_length:
    for character in password:
        if character in special_characters:
            special_characters_number += 1
        elif character in alphabetic_characters:
            alphabetic_characters_number += 1
        elif character in digit:
            digit_number += 1
      
    if special_characters_number < 3:
        print("Validation failed: You have to have a minimum of 3 special characters")
        sys.exit()  
    elif alphabetic_characters_number < 5:
        print("Validation failed: You have to have a minimum of 5 alphabets in your password")
        sys.exit()
    elif digit_number < 3:
        print("Validation failed: You have to have a minimum of 3 numbers in your password")
        sys.exit()
    else:
        print("Validation succeeded!")

else:
    print("Invalid password! Length of password has exceeded 12")

