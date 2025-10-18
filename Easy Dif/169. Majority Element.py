from typing import List
import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        return counter.most_common(1)[0][0]


nums= [3,2,3]
sol = Solution()
print(sol.majorityElement(nums))