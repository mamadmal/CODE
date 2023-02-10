import sys

low = 1
high = 1400000 #just large random number

list = []

for num in range(low, high ):

   if num > 1:
       for i in range(2, num): #it will need so much time to compile
           if (num % i) == 0:
               break
       else:
           list.append(num)
           if len(list) == 10001: #if we find 10000th of prime number just stoped the running code.
               print(list)
               sys.exit()

print(len(list))

