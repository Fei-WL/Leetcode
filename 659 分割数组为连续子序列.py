from collections import Counter
from typing import List

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        nums_dict = Counter(nums)
        nums_dict = dict(sorted(nums_dict.items(), key=lambda kv: kv[0] < kv[1]))
        tail = [key for key in list(nums_dict.keys())]
        for (key, value) in nums_dict.items():
            

Solution().isPossible([1,2,3,3,4,5])