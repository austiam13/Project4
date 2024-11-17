import random

ROW_OF_PICKS=6
MAXIMUM=45
MINIMUM=1
quick_picks=int(input("How many quick picks you want to generate: "))
all_picks=[]


for i in range(quick_picks):
    current_pick=[]
    while len(current_pick)<ROW_OF_PICKS:
        num=random.randint(MINIMUM,MAXIMUM)
        if num not in current_pick:
            current_pick.append(num)
    current_pick.sort()
    all_picks.append(current_pick)

for pick in all_picks:
    for num in pick:
     print(f"{num:>2}",end=" ")
    print()