fullyCountainedCount = 0
overlapCount = 0
# I only care, if one elf is within the
# Full range of the other..
# PART 1 FUNCTION
def ifInRange(elf1, elf2):
    if int(elf1[0]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1]):
        return 1
    elif int(elf2[0]) >= int(elf1[0]) and int(elf2[1]) <= int(elf1[1]):
        return 1
    return 0

def ifOverlap(elf1, elf2):
    # Check if the values are within the range of the 2nd elf.
    for elves in [(elf1, elf2), (elf2, elf1)]:
        if int(elves[0][0]) >= int(elves[1][0]) and int(elves[0][0]) <= int(elves[1][1]):
            return 1
        elif int(elves[0][1]) >= int(elves[1][0]) and int(elves[0][1]) <= int(elves[1][1]):
            return 1
    return 0

c = 1
with open("d4in.txt", "r") as file:
    for line in file.read().splitlines():
        i = line.find(',')
        elf1 = line[:i].split('-')
        elf2 = line[i+1:].split('-')
        # Part1
        fullyCountainedCount += ifInRange(elf1, elf2)
        # Part2
        overlapCount += ifOverlap(elf1, elf2)

print(f"Fully Contained: {fullyCountainedCount}\nOverlapping: {overlapCount}")