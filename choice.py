import random

word_list = ["apple","banana","cherry","Mango","pear"]
print(random.choice(word_list))
usrInput = ''
 
while True:
    usrInput = input("Enter a single character as input: ")
    if len(usrInput) == 1:
        print(f'Your single character input was: {usrInput}')
        break
    print("Please enter a single character to continue\n")
