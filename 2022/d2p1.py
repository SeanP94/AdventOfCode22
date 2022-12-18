outcome = 0
def winLose(you, opp) -> int:
    #1 rock
    #2 paper
    #3 scis
    if (opp == you - 1) or (you == 1 and opp == 3):
        return 6 + you
    if opp == you:
        return 3 + you
    return you

with open("d2in.txt", 'r') as file:
    for row in file.read().splitlines():
        arr = row.split(" ")
        opp = 1 + ord(arr[0]) - ord("A") 
        you = 1 + ord(arr[1]) - ord("X") 
        outcome += winLose(you, opp)
print(outcome)