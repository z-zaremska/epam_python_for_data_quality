from random import randint
from statistics import mean


# Create list of 100 random numbers from 0 to 1000
random_list = [randint(0, 1000) for num in range(100)]

# Sort list from min to max(without using sort())
sorted_random_list = []

for i in range(len(random_list)):
    min_num = min(random_list)
    sorted_random_list.append(min_num)
    random_list.remove(min_num)

# Calculate average for even and odd numbers.
even_avg = mean([num for num in sorted_random_list if num % 2 == 0])
odd_avg = mean([num for num in sorted_random_list if num % 2 != 0])

# Print both average result in console.
print('Even average: ', even_avg)
print('Odd average: ', odd_avg)
