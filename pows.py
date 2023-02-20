
list = []
for i in range(101):
    list.append(i)
print(list)

sum = 0
for i in range(len(list)):
    sum = sum + list[i]
    i = i + 1

print(sum)
sumOfPow = pow(sum, 2)
print("poewer sum: ", sumOfPow)


single_pow = []
for i in range(len(list)):
    x = pow(list[i], 2)
    single_pow.append(x)
print(single_pow)

sin_sum = 0
for i in range(len(single_pow)):
    sin_sum = sin_sum + single_pow[i]
    i += i
print("total sum: ", sin_sum)

finalAns = sumOfPow - sin_sum
print("final answer is: ", finalAns)
