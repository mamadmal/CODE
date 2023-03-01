import sys
min_num = 1
max_num = 2000000

list = []

for num in range(min_num, max_num):
    if num > 1:
        for i in range(2, num): #it will need so much time to compile
            if (num % i) == 0:
               break
            else:
                list.append(num)

    if len(list) == 2000000:
        print(list)
        sys.exit()

x = 0
for i in range(len(list)):
    x = x + list[i]
print(x)