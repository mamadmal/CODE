list = []
for i in range(1000):
    if (i % 3 ) == 0 or (i % 5) == 0:
        list.append(i)
print(list)

total = len(list)
print("len", total)
sum = 0
for i in range(total):
    sum = sum + list[i]
print(sum)
