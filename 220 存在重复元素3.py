from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        for index in range(len(nums) - k):
            for index in range(1, k):
                