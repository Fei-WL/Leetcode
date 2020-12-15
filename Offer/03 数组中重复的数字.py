from typing import List

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        existed = [False] * max(nums)
        for num in nums:
            if existed[num]:
                return num
            existed[num] = True

nums = [2, 3, 1, 0, 2, 5, 3]

Solution().findRepeatNumber(nums)