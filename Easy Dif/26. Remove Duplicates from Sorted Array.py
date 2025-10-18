from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[res] = nums[i]
                res += 1
        return res


sol = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
sol.removeDuplicates(nums)
print(nums)