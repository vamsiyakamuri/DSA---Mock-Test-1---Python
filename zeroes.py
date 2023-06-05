def moveZeroes(nums):
    n = len(nums)
    zero_count = 0  # Counter for the number of zeroes encountered
    
    # Iterate through the array with the fast pointer
    for i in range(n):
        if nums[i] == 0:
            zero_count += 1
        else:
            # Swap the non-zero element with the element at the slow pointer
            nums[i], nums[i - zero_count] = nums[i - zero_count], nums[i]
    
    # Move all the zeroes to the end of the array
    for i in range(zero_count):
        nums[n - 1 - i] = 0

# Example test cases
nums1 = [0, 1, 0, 3, 12]
moveZeroes(nums1)
print(nums1)  # Output: [1, 3, 12, 0, 0]

nums2 = [0]
moveZeroes(nums2)
print(nums2)  # Output: [0]
