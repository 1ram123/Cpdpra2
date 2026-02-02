x = int(input())
y = input()
count = 0
for d in range(1,x):
    if y[d] == y [d-1]:
        count += 1
print(count)    