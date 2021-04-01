# Generate random numbers with a given range
# Store them in a list
import random
import time

# Initializing hashmap (number: itemsInArray) dictionary
numbersCount = {}

# Getting input from user
quantityInput = int(input("How many numbers do you wish to generate in the list? "))
startInput = int(input("What is the starting range? "))
endInput = int(input("What is the ending range? "))

# Colors for console print
# green
colorGreen = '\033[32m'
# orange
colorOrange = '\033[33m'
# blue
colorBlue = '\033[34m'

# Algorithm start time
start_time = time.time()

# Generating list with random integer numbers according to user input 
randomNumList = []
for i in range(quantityInput):
    temp = random.randint(startInput, endInput)
    # Set number volume to 0 if it does not exist
    if temp not in numbersCount:
        numbersCount[temp] = 0
    # Increase generated number volume
    numbersCount[temp] += 1
    # Adding generated number to an array
    randomNumList.append(temp)

print('\n')
print(colorBlue + 'Unsorted generated list: ')
print(randomNumList)
print('\n')

# Sorting an array by each item's count (itemsInArray) and item itself (number)
sortedRandomNumList = sorted(randomNumList, reverse=True, key=lambda k: (numbersCount.get(k), k))
# Removing items from array by most frequent occurrences
while len(sortedRandomNumList):
    keyOfMostFrequentNum = max(numbersCount, key=numbersCount.get)
    noun = 'are' if numbersCount[keyOfMostFrequentNum] > 1 else 'is'
    # Formatted string with correct noun and values for printing
    formatted_string = 'There %s %i of %i' % (noun, numbersCount[keyOfMostFrequentNum], keyOfMostFrequentNum)
    print(colorGreen + formatted_string)
    print(sortedRandomNumList)
    # Removal procedure
    while keyOfMostFrequentNum in sortedRandomNumList:
        sortedRandomNumList.remove(keyOfMostFrequentNum)
    # Removing item from numbersCount hashmap
    numbersCount.pop(keyOfMostFrequentNum)
    print(colorOrange + 'With removed numbers: ')
    print(sortedRandomNumList)
    print('\n')

# Calculating and printing algorithm execution time in seconds
print(colorGreen + "Algorithm took total of %s seconds." % (time.time() - start_time))