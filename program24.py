#For loops

#it is used for stinngs, tuples, lists.
list = [1, 2, 3, 4, 5,]

for num in list:
    print(num)
else:
    print("End")
    
    
#example
    
    nums = (1, 4, 54, 76, 46, 76, 56, 46)
    x=46
    
    idx = 0
    for el in nums:
        if(el == x):
            print("Num found at idx", idx)
            break
        idx += 1
        
        
#range function.
#3 conditions(start?, stop, step)

for el in range(5): #range(start?)
    print(el)          
    
for el in range(2, 10):#range(start?, stop, )
    print(el)
    
for el in range(1, 20, 2):#range(start, stop, step)
    print(el)
    
    
#practic qustions

#print revers order
for i in range(100, 0, -1):
    print(i)
 
    
#peint the table of any number with the help of range
n = int(input("Enter the number:"))

for i in range(1, 11):
    print(n*i)