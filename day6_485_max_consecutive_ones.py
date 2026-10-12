class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        streak = 0
        best = 0
        for x in nums:
            if x == 1:
                streak += 1
                best = max(best, streak)
            else:
                streak = 0
        return best

# Time Complexity: O(n)
# Space Complexity: O(1)

# 485. Max Consecutive Ones
# Solved
# Easy


# Hint
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2
 