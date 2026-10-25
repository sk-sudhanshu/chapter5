#practice qustions

#print for any number of table
n = int(input("Enter the number: "))
i = 1
while i <= 10 :
    print(n*i)
    i+=1


#print the list with the help of while loop

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1
    
    
#search for a number x in this tuple using loop
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

x=81
i = 0
while i < len(list):
    if(list[i]==x):
        print("Found at index:", i)
        break
    else:
        print("Finded..")
    i += 1