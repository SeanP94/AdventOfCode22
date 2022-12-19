def crane9000(crateCount, fromPile, toPile):
    for _ in range(crateCount):
        toPile.append(fromPile.pop())

def crane9001(crateCount, fromPile, toPile):
    #for _ in range(crateCount):
    toPile += fromPile[-crateCount:]
    del fromPile[-crateCount:]

with open("d5in.txt", "r") as file:
    data = file.read().splitlines()
    
# Create Crate Pile
crate_stacks = [[],[],[],[],[],[],[],[],[]]
for crate in data[:8]:
    i = 0
    # First 8 lines are the crate piles.
    for j in range(9):
        if crate[i:i+3] != "   ": # If not empty space
            crate_stacks[j].insert(0,crate[i+1])
        i+=4
c=0    
for statement in data[10:]:
    data = statement.split(" ")
    count = int(data[1])
    i = int(data[3]) - 1
    j = int(data[5]) - 1
    # Used on Part1
    #crane9001(count, fromPile=crate_stacks[i], toPile=crate_stacks[j])
    # Used on Part2
    crane9001(count, fromPile=crate_stacks[i], toPile=crate_stacks[j])

for crate in crate_stacks:
    print(f"{crate[-1]}", end="")
print()