outcome = 0
    #1 rock
    #2 paper
    #3 scis
def findMove(key, opp):
    if key == "WIN": #X
        if opp == 3:
            return 7
        return 6 + opp + 1
    elif key == "DRAW": 
        return opp + 3
    else: #Lose
        if opp == 1:
            return 3
        return opp - 1
ds = {
    "X" : "LOSE",
    "Y" : "DRAW",
    "Z" : "WIN"
}
with open("d2in.txt", 'r') as file:
    for row in file.read().splitlines():
        arr = row.split(" ")
        opp = 1 + ord(arr[0]) - ord("A") 
        key = arr[1] 
        outcome += findMove(ds[key], opp)
print(outcome)