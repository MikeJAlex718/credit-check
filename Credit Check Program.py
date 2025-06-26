#JAM
#6/19/2025
#Checks for inputted Credit Card numbers

import sys

cardNum = input("Enter a number: ")
cardLen = len(cardNum)
print(f"Current card length: {cardLen}")

#Determines if the card number length is valid
if(cardLen not in [13,15,16]):
    sys.exit("The card number entered is an invalid length")

#Traverses through the card number in reverse and adds the total
total = 0;
reverseDigits = cardNum[::-1]
for num in range(cardLen):
    digit = int(reverseDigits[num])
    if(num%2==1):
        digit*=2
        if(digit>9):
            digit-=9
    total+=digit

#Determines what type of card it is or whether it is invalid
firstDigit = int(cardNum[0])
secDigit = int(cardNum[1])
if(total%10==0):
    if((cardLen==13 or cardLen==16) and firstDigit == 4):
        print("VISA")
    elif(cardLen==16 and (firstDigit == 5 and secDigit<6)):
        print("MasterCard")
    elif(cardLen==15 and firstDigit==3 and (secDigit==4 or secDigit==7)):
        print("AMEX")
    else:
        print("unidentifiable Card Number")
else:
    print("Unidentifiable Card Number")