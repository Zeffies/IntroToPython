a, b = 0, 1
for x in range(20):
    a, b = b, a+b
    print(a, end=", ")
