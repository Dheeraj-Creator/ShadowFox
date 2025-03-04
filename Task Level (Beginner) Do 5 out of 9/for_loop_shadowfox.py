import random
#simulating rolling a six-sided die
rolls=20  
count_six=0
count_one=0
consecutive_sixes=0
previous_roll=None  

for _ in range(rolls):
    roll = random.randint(1, 6)
    if roll==6:
        count_six +=1
        if previous_roll==6:
            consecutive_sixes +=1
    elif roll==1:
        count_one +=1
    previous_roll=roll

print(f"you rolled a 6:{count_six} times")
print(f"you rolled a 1:{count_one} times")
print(f"you rolled two 6s in a row:{consecutive_sixes} times")

#jumping jacks workout tracker
total_jumping_jacks=100
jump_per_set=10
completed_jumping_jacks=0

while completed_jumping_jacks < total_jumping_jacks:
    completed_jumping_jacks +=jump_per_set
    print(f"you completed {completed_jumping_jacks} jumping jacks")

    if completed_jumping_jacks >=total_jumping_jacks:
        print("congratulations! you completed the workout")
        break

    tired=input("are you tired? (yes/no): ").strip().lower()
    
    if tired in ["yes", "y"]:
        skip=input("do you want to skip the remaining sets? (yes/no): ").strip().lower()
        if skip in ["yes", "y"]:
            print(f"you completed a total of {completed_jumping_jacks} jumping jacks")
            break
    else:
        remaining=total_jumping_jacks - completed_jumping_jacks
        print(f"{remaining} jumping jacks remaining")
