from typing import List
from collections import Counter

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count_list = Counter(arr)
        count_list = dict(sorted(count_list.items(), key=lambda kv:(kv[1], kv[0])))
        one_quater = len(arr) / 4
        for (keys, values) in count_list.items():
            if values > one_quater:
                return keys

arr = [1,2,2,6,6,6,6,7,10]
print(Solution().findSpecialInteger(arr))