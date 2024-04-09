#WAF to convert USD to INR .
INR = 83.21
USD = float(input("Enter the USD : "))

def convertUsdToInr(USD):
    return USD * INR

print(USD,"USD = ",convertUsdToInr(USD),"INR")