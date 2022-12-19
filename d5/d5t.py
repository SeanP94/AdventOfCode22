def move(crateCount, fromPile, toPile):
    for _ in range(crateCount):
        toPile.append(fromPile.pop())


with open("d5int.txt", "r") as file:
    data = file.read().splitlines()
    
# Create Crate Pile
crate_stacks = [[],[],[],[],[],[],[],[],[]]
for crate in data[:3]:
    i = 0
    # First 8 lines are the crate piles.
    for j in range(3):
        if crate[i:i+3] != "   ": # If not empty space
            crate_stacks[j].insert(0,crate[i+1])
        i+=4

c = 0
for statement in data[5:]:
    data = statement.split(" ")
    count = int(data[1])
    i = int(data[3]) - 1
    j = int(data[5]) - 1
    move(count, fromPile=crate_stacks[i], toPile=crate_stacks[j])
    c+=1
print(crate_stacks)