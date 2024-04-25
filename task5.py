#Task 5
"""
Iterate through the list of numbers.
If the number is positive, determine the square root of the number.
State the number and the square root value
"""
nums = (5,-2,12,-8,14,16)

for i in nums:
    if i < 0:
        print(f"The number is {i} and has no square root because it is negative.")
    else:
        s = i**0.5
        print(f"The number is {i} and the square root value is {s}.")