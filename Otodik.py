for i in range(2, 101):
    prim = True
    for j in range(2, i):
        if i % j == 0:
            prim = False
            break
    if prim:
        print(i)
