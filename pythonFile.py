import random as rd


num_range = int(input("How many numbers do you want to print?: "))
random_numbers = [rd.randint(1,100) for i in range(num_range)]

print(f"{num_range} random numbers: ")
print(random_numbers)