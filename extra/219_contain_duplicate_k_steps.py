class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = {}       
        for i,x in enumerate(nums):
            if x in seen:
                if abs(i - seen[x]) <=k:
                    return True   
            seen[x] = i
        return False
        