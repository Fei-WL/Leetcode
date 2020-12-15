from typing import List
from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, two, curr = 0, len(nums)-1, 0
        while curr <= two:
            if nums[curr] == 0:
                nums[zero], nums[curr] = nums[curr], nums[zero]
                zero += 1
                curr += 1
            elif nums[curr] == 2:
                nums[two], nums[curr] = nums[curr], nums[two]
                # curr += 1
                two -= 1
            else:
                curr += 1
        print(nums)


nums = [2, 0, 2, 1, 0, 1, 0]
Solution().sortColors(nums)