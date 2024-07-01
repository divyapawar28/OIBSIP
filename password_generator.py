import string 
import random

length = int(input("Enter password length : "))

print("Choose Character set for password from these :\n 1. Letters\n 2. Digits \n 3. Special Characters \n 4. Done")

character_set = ""

while True : 
     choice = int(input("Pick a number (1-4) : "))
     
     if choice == 1 :
          character_set += string.ascii_letters
     
     elif choice == 2 :
          character_set += string.digits
          
     elif choice == 3 :
          character_set += string.punctuation
          
     elif choice == 4 :
          break
     
     else :
          print("Please pick a valid option !")
          
          
password = ''.join(random.choice(character_set) for _ in range(length))

print("The random password is : " + password)