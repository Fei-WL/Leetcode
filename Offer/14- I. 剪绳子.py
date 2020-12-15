import math

class Solution:
    def cuttingRope(self, n: int) -> int:
        result = [idx for idx in range(0, n + 1)]

        result[0] = 1
        result[-1] -= 1

        for out_idx in range(2, n + 1):
            if out_idx == n:
                start = 1
            else:
                start = 0
            temp = 1
            for in_idx in range(start, out_idx):
                temp = max(temp, result[out_idx - in_idx] * result[in_idx])
            result[out_idx] = temp

        return result[-1]


print(Solution().cuttingRope(10))