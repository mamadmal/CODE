# sum of pows

num = pow(2, 1000)
lis = list(str(num))
print(lis)

sum = 0 
for i in range(len(lis)):
    sum = sum + int(lis[i])
print(sum)
