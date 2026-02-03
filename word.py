x = input()
y = 0
z = 0
for r in x:
    if r.isupper():
        y += 1
    else:
        z += 1
if  z >= y:
    print(x.lower())
else:
    print(x.upper())
                   
    
