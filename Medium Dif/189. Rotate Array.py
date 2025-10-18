from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if len(nums) <= 1:
            return
        extras = []
        if k > len(nums):
            k = k % len(nums)
        for i in range(len(nums)-k,len(nums)):
            extras.append(nums[i])
        size = len(nums) - k - 1
        while size >= 0:
            nums[size+k] = nums[size]
            size -= 1
        for i in range(len(extras)):
            nums[i] = extras[i]

nums = [1,2]
k = 7
sol = Solution()
sol.rotate(nums,k)
print(nums)