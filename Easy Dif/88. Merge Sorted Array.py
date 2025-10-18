from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        inda, indb = 0, 0
        nums3 = []
        while inda < m and indb < n:
            if nums1[inda]<nums2[indb]:
                nums3.append(nums1[inda])
                inda += 1
            else:
                nums3.append(nums2[indb])
                indb += 1
        while inda < m:
            nums3.append(nums1[inda])
            inda += 1
        while indb < n:
            nums3.append(nums2[indb])
            indb += 1
        for i in range(0, len(nums3)):
            nums1[i] = nums3[i]
        """
        Do not return anything, modify nums1 in-place instead.
        """

sol = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
sol.merge(nums1, m, nums2, n)
print(nums1)