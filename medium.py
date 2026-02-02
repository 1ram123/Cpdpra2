x = int(input())
for _ in range (x):
    ls = list(map(int,input().split()))
    ls.sort()
    print(ls[1])    