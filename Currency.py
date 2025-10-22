total_amount = int(input())
starting_denomination = int(input()) 
denominations = [100, 50, 20, 10, 5, 2, 1]
remaining_amount = total_amount

for note in denominations:
    if note == 100:
        count = remaining_amount // 100
        remaining_amount = remaining_amount % 100
        print(f"{note} rupees note: {count}")
    
    elif note == 50:
        count = remaining_amount // 50
        remaining_amount = remaining_amount % 50
        print(f"{note} rupees note: {count}")
        
    elif note == 20:
        count = remaining_amount // 20
        remaining_amount = remaining_amount % 20
        print(f"{note} rupees note: {count}")
        
    elif note == 10:
        count = remaining_amount // 10
        remaining_amount = remaining_amount % 10
        print(f"{note} rupees note: {count}")

    elif note == 5:
        count = remaining_amount // 5
        remaining_amount = remaining_amount % 5
        print(f"{note} rupees note: {count}")

    elif note == 2:
        count = remaining_amount // 2
        remaining_amount = remaining_amount % 2
        print(f"{note} rupees note: {count}")

    elif note == 1:
        count = remaining_amount // 1
        remaining_amount = remaining_amount % 1 
        print(f"{note} rupee note: {count}")   