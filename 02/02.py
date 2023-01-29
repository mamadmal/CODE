#fibonacci numbers
x = 1
y = x + 1

ls = [1,2]

for x in range(13):
    x = 1
    z = x + y
    ls.append(z)
    print(z)
    x = z + y
    ls.append(x)
    print(x)
    y = x + z
    ls.append(y)
    print(y)

print(ls)
ls.remove(4782968)
print(ls)

total = len(ls)
print("len is: ", total)

sum = 0
for i in range(total):
    sum = sum + ls[i]
    ++i
print(sum)
# thath the tortal sum of ep2 

evls = []  # get the odd numbers in List
for i in ls:
    if (i % 2) == 0:
        evls.append(i) 
print(evls)

t = len(evls)
su = 0
for i in range(t):
    su = su + evls[i]
    ++i
print(su)
