from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(s) == 0:
            return 0

        g.sort()
        s.sort()
        g_idx = 0
        s_idx = 0
        count = 0
        while g_idx != len(g):
            while s_idx < len(s) and g[g_idx] > s[s_idx]:
                s_idx += 1
            if s_idx >= len(s):
                break
            else:
                count += 1
                g_idx += 1
                s_idx += 1

        return count