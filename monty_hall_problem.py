import random

def compute_probability(limit) :
    proceed_wins = 0
    switch_wins = 0
    for i in range(limit) :
        car_door = random.randint(1,3) # door behind which car hides
        user_choice = random.randint(1,3) #user guess 1 door to open
        doors = [1,2,3] # there are 3 doors , universe
        doors.remove(user_choice)
        if user_choice != car_door :
            doors.remove(car_door)
        monty_opens = random.choice(doors)
        switch_options = [1,2,3]
        switch_options.remove(monty_opens)
        switch_options.remove(user_choice)
        switch_choice = switch_options[0]

        if switch_options == car_door :
            switch_wins += 1
        elif user_choice == car_door :
            proceed_wins += 1
    switch_probability = switch_wins / limit
    proceed_probability = proceed_wins / limit

    return switch_probability, proceed_probability

a = compute_probability(1000000)
print(a)