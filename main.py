import sys
import random

# get length
passLength = 0
while passLength < 8 or passLength > 24:
    passLength = input("How long do you want you password?(8-24): ")
    try:
        passLength = int(passLength)
    except ValueError:
        sys.exit(print("Needs to be integer"))

# get upper case letters
upper = False
upper = input("Do you want uppercase?(y/n): ").lower()
if upper == "y" or upper == "yes":
    upper = True


# get number
numbers = False
answer = input("Do you want numbers?(y/n): ").lower()
if answer == "y" or answer == "yes":
    numbers = True


# get special character
specialChar = False
answer = input("Do you want special characters?(y/n): ").lower()
if answer == "y" or answer == "yes":
    specialChar = True


alphabet = "abcdefghijklmnopqrstuvwxyz"
alphaList = []
for letter in alphabet:
    alphaList.append(letter)

special = "~`!@#$%^&*()_-+={[}]|\\:;\"'<,>.?/"
specialList = []
for symbol in special:
    specialList.append(symbol)

generatedPass = ""
for length in range(passLength):
    while length + 1 > len(generatedPass):
        char = random.randrange(1, 4)
        if char == 1:
            # gets alphabet
            alphaChar = alphaList[random.randrange(0, len(alphaList))]
            if upper is True:
                if random.randrange(1, 3) == 1:
                    generatedPass += alphaChar.upper()
                else:
                    generatedPass += alphaChar
            else:
                generatedPass += alphaChar

        elif char == 2:
            if numbers is True:
                # gets number
                generatedPass += str(random.randrange(0, 10))
            else:
                continue

        elif char == 3:
            if specialChar is True:
                # gets special
                max = len(specialList)
                generatedPass += specialList[random.randrange(0, max)]
            else:
                continue

print(generatedPass)
