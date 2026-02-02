x = int(input())
for _ in range (x):
    a , b , c = map(int,input().split())
    if c == a + b:
        print("+")
    else:
        print ("-")   