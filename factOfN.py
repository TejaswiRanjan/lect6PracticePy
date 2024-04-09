#WAF to find the factorial of n (n is the parameter)
n = int(input("Enter the number : "))
def factOfN(n):
    fact=1
    i=1
    while i<=n:
        
        fact = fact * i
        i+=1
    return fact
        
print("The Factorial of N is : ",factOfN(5))