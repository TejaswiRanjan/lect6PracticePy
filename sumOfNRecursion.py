#Write a recursive function to calculate the sum of first n natural numbers.

n = int(input("Enter the number : "))

def sumOfN(n):
    if(n==1):
        return 1
    return sumOfN(n-1)+n

print("The sum of first ",n,"Natural number is : ",sumOfN(n))