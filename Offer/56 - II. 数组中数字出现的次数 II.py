from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        for index in range(0, len(nums), 3):
            if index + 1 == len(nums):
                return nums[index]
            if nums[index] != nums[index+1]:
                return nums[index]

nums = [9,1,7,9,7,9,7]
print(Solution().singleNumber(nums))