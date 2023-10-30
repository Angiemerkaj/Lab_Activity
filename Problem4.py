#!/usr/bin/env

#Enxhi Merkaj 10/29/2023

# Loop from 1 to 50
for number in range(1, 51):
    if number % 3 == 0 and number % 5 == 0:
        print(f"{number} Divisible by three and five")
    elif number % 3 == 0:
        print(f"{number} Divisible by three")
    elif number % 5 == 0:
        print(f"{number} Divisible by five")
    else:
        print(number)
