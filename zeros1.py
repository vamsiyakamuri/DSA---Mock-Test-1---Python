def moveZeroes(nums_input):
    n = len(nums_input)
    zero_count = 0  # Counter for tracking the number of zeroes encountered
    
    # Iterate through the array using a fast pointer
    for i in range(n):
        if nums_input[i] == 0:
            zero_count += 1
        else:
            # Swap the non-zero element with the element at the slow pointer
            nums_input[i], nums_input[i - zero_count] = nums_input[i - zero_count], nums_input[i]
    
    # Move all the zeroes to the end of the array
    for i in range(zero_count):
        nums_input[n - 1 - i] = 0

# Example test cases
nums_input1 = [0, 1, 0, 3, 12]
moveZeroes(nums_input1)
print(nums_input1)  # Output: [1, 3, 12, 0, 0]

nums_input2 = [0]
moveZeroes(nums_input2)
print(nums_input2)  # Output: [0]
