from  typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        initial_len = len(nums)
        i = 0
        counter = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                j = i + 1
                while j < len(nums) - 1 and nums[j] == nums[j + 1]:
                    nums.pop(j + 1)
                    counter += 1
                i = j
            else:
                i += 1
        return initial_len - counter


nums = [1,1,1]
sol = Solution()
print(sol.removeDuplicates(nums))
print(nums)