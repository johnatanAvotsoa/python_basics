# probability o fn people having the same birthday
import random


def birthday_paradox_simulation(num_people) :
    birthdays = [random.randint(1,365) for _ in range(num_people)]
    repeated= 0 # number of duplicate birthday
    print(birthdays)
    for i in range(len(birthdays)-1) :
        for j in range(i,len(birthdays)-1) :
            if birthdays[i] == birthdays[j] :
                repeated += 1
    return repeated/ len( birthdays)

print(birthday_paradox_simulation(23))