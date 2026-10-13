class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        n= len(nums)
        for i in range(n):
            if  nums[i] in nums[i+1:n]:
                return True
        return False
# the above method has time complexity of O(n^2) and space complexity of O(1) and so it gives time exceed for large inputs
# the fastest way is O(n) time and O(n) space complexity using set data structure

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for x in nums:
            if x in seen:
                return True
            else:
                seen.add(x)
        return False

        

# 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Explanation:

# The element 1 occurs at the indices 0 and 3.

# Example 2:

# Input: nums = [1,2,3,4]

# Output: false

# Explanation:

# All elements are distinct.

# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]

# Output: true