from typing import List

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        result = []
        for n in range(2, target):
            temp = int(target - n * (n-1) / 2)
            a_1 = int(temp // n)
            if a_1 <= 0:
                break
            t = int((2 * a_1 + n -1) * n / 2)
            if t == target:
                result.append([i for i in range(a_1, a_1 + n)])
        result = sorted(result, key=lambda item:item[0])
        return result

target = 15
s = Solution()
print(s.findContinuousSequence(target))