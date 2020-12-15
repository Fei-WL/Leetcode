import collections

class Solution:
    def firstUniqChar(self, s: str) -> str:
        s = collections.Counter(s)
        if 1 not in s.values():
            return " "
        for key, value in s.items():
            if value == 1:
                return key



s = Solution()
input = "leetcode"
print(s.firstUniqChar(input))