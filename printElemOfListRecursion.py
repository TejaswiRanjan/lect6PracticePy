# Write a recursive function to print all elements in a list 
#Hint : use list & index as parameters. 


def printElemOfList(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    printElemOfList(list,idx+1)

print(printElemOfList([1,2,3,4,5,3,4,10]))