class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0
        for x in nums:
            if len(str(abs(x)))%2 ==0:
                count +=1
        return count

class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0
        for x in nums:
            digit = 0
            while x>0:
                x//=10
                digit+=1
            if digit%2 ==0:
                count+=1
        return count
        

# Time Complexity: O(n)
# Space Complexity: O(1)

# 1295. Find Numbers with Even Number of Digits
# Solved
# Easy


# Hint
# Given an array nums of integers, return how many of them contain an even number of digits.

 

# Example 1:

# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation: 
# 12 contains 2 digits (even number of digits). 
# 345 contains 3 digits (odd number of digits). 
# 2 contains 1 digit (odd number of digits). 
# 6 contains 1 digit (odd number of digits). 
# 7896 contains 4 digits (even number of digits). 
# Therefore only 12 and 7896 contain an even number of digits.
# Example 2:

# Input: nums = [555,901,482,1771]
# Output: 1 
# Explanation: 
# Only 1771 contains an even number of digits.
 