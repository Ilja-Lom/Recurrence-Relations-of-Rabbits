
immature_rabbits = int(input("Enter how many immature pairs of rabbits you wish to start with:\n"))
n = int(input("Enter the number of generations you wish to run:\n")) #number_of_generations
k = int(input("Enter the number of pairs per litter (k-number):\n")) #number_of_pairs_per_litter
newly_born_rabbits = 0
mature_rabbits = 0
generation_number = 1 #the generation number is 1 from the onset because Python counts from 0. This would make loop counting confusing

while generation_number <= n-1: #n-1 because otherwise the loop runs once too many times
    
    mature_rabbits += immature_rabbits
    immature_rabbits = 0 #All the immature rabbits have matured, none left
    immature_rabbits += newly_born_rabbits #This is to make the newly_born_rabbits take one generation to mature before they are able to breed
    newly_born_rabbits = mature_rabbits * k #This calculates the number of new rabbits that are born
    generation_number += 1

print(f"This is generation {generation_number}, total number of rabbits {mature_rabbits+immature_rabbits}")











