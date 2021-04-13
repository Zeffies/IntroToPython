def add_pers(n):
    cur_num = 0
    runs = 0
    numlist = list(str(n))
    while len(numlist) > 1:
        for num in numlist:
            cur_num += int(num)
        else:
            numlist = list(str(cur_num))
            runs += 1
            cur_num = 0
    print(runs)
            
add_pers(13)
add_pers(199)
add_pers(9876)
test = bin(5)
print(test)
