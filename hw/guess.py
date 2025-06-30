import random

numTrys = 0

while True:
    nums = random.randint(1,100)

    userGuess = int(input("Enter a number from 1 - 100: "))

    if str(nums) in str(userGuess):
        print("YOU GOT IT RIGHT! "+"num was "+str(nums))
        break
    else:
        print("WRONG try again.")
        numTrys += 1
    if numTrys == 10:
        print("num was "+str(nums))
        break