from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
       i = 0
       while i < len(nums):
           if nums[i] == val:
               nums.pop(i)
           else:
               i += 1


nums = [0,1,2,2,3,0,4,2]
val = 2
sol = Solution()
sol.removeElement(nums, val)
print(nums)