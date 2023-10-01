"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = sorted([float(value) for value in input().split(",")])
        length = len(numbers)
        if (length % 2 == 0):
            median = (numbers[length//2]+numbers[(length//2)-1])/2
        else:
            median = numbers[(length//2)]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(median)
