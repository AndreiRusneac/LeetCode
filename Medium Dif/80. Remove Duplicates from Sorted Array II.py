from  typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i = 1
        ind = nums[0]
        counter = 1
        empty_pos = 1

        while i < len(nums):
            if nums[i] == ind:
                if counter < 2:
                    nums[empty_pos] = nums[i]
                    empty_pos += 1
                    counter += 1
                i += 1
            else:
                ind = nums[i]
                counter = 1
                nums[empty_pos] = nums[i]
                empty_pos += 1
                i += 1

        return empty_pos

nums = [0,0,1,1,1,1,2,3,3]
sol = Solution()
print(sol.removeDuplicates(nums))
print(nums)