max_tuple = (-1, -1)
li = 1
with open("d1in.txt", "r") as inp:
    elfSum = 0
    for line in inp.readlines():
        if line != '\n':
            elfSum += int(line)
        else:
            if max_tuple[0] < elfSum:
                max_tuple = (elfSum, li)
            li+=1
            elfSum = 0
print(max_tuple)