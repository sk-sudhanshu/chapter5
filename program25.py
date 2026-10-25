#pass condition
# that is used for place holder for feture.

for i in range(5):
    pass

print("some work ..")

#practic qustions

n = int(input("Enter number:"))

sum = 0
for i in range(1, n+1):
    sum += i
    
print("total sum =",sum)
 
 
 
#factorial of n number
n = int(input("Enter number:"))

fact = 1
i=1
while i <= n:
    fact *= i
    i += 1
    
print("total fact =",fact)
 