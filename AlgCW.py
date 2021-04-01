import random
import time

# Input from User
amount = int(input('Enter numbers for list: '))
start = int(input('Enter the starting range? '))
end = int(input('Enter the ending range? '))

# Start Time
start_time = time.time()
print()

# Generating Random Integer from Input
generated = [random.randint(start, end) for x in range(amount)]

print('Unsorted generated list:')
print(generated)
print()

# Sorting the arrays
numbers = {}
for x in generated:
    try:
        numbers[x] += 1
    except:
        numbers[x] = 1

generated.sort(reverse=True)
generated.sort(reverse=True, key=lambda x: numbers[x])

while numbers:
    best = None
    for x in numbers:
        if best == None:
            best = x
        elif numbers[x] > numbers[best]:
            best = x
        elif numbers[x] == numbers[best] and x > best:
            best = x
        # Removing the numbers
    print(f'There are {numbers[best]} of {best}')
    print(generated)
    print('With removed numbers:')
    index = generated.index(best)
    for x in range(numbers[best]):
        del generated[index]
    del numbers[best]
    print(generated)
    print()

# End Time
print("The program took %s seconds." % (time.time() - start_time))



