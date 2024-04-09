#Write a function to check the number is even or odd .
num= int(input("Enter a number : "))
def checkEvenOdd(n):
    if (num % 2 == 0):
        print("EVEN")
    else:
        print("ODD")

checkEvenOdd(num)