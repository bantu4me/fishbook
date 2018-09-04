l = [('1', 1), ('2', 2), ('3', 3)]

for i in l:
    print(i)

m = {'1':1,'2':2}

print(m.get(3) if m.get(3) else 0)