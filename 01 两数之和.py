from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx in range(len(nums) - 1):
            start = nums[idx]
            for jdx in range(idx + 1, len(nums)):
                result = start + nums[jdx]
                if result == target:
                    return [idx, jdx]

        return []