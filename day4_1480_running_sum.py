class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        running_sum = []
        running_sum.append(nums[0])
        for i in range(1,len(nums)):
            running_sum.append(nums[i]+ running_sum[i-1])
        return running_sum

#  automatic 
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        total = 0
        result = []
        for x in nums:
            total += x
            result.append(total)
        return result

# Time Complexity: O(n)
# Space Complexity: O(n)
# 1480. Running Sum of 1d Array


# Hint
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
# Example 2:

# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
# Example 3:

# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]
 