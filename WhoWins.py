N = int(input())
total_removed = 0
round_number = 1
winner = ""

while total_removed < N:
    ramesh_stones = round_number
    if total_removed + ramesh_stones >= N:
        winner = "Ramesh"
        break
    total_removed = total_removed + ramesh_stones
    suresh_stones = round_number * 2
    if total_removed + suresh_stones >= N:
        winner = "Suresh"
        break
    total_removed = total_removed + suresh_stones
    round_number = round_number + 1
print(winner)