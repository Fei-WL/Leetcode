from typing import List

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = [0] * 26
        for i, ch in enumerate(S):
            last[ord(ch) - ord("a")] = i    #记录下S中同一个字符最后出现的位置

        result = []
        start = end = 0
        for i, ch in enumerate(S):
            end = max(end, last[ord(ch) - ord("a")])
            if i == end:
                result.append(end-start+1)
                start = end + 1

        return result

