import math

class Solution:
    def find_index_(self, index):
        temp = self.order[index-1]
        self.order.remove(temp)
        return temp

    def getPermutation(self, n: int, k: int) -> str:
        result = []
        self.order = [i for i in range(1, n+1)]
        for i in range(n):
            t = i + 1
            each_change = math.factorial(n-t)
            if k > each_change:
                if k % each_change != 0:
                    first = k // each_change + 1
                    k %= each_change
                else:
                    first = k // each_change
                    k -= each_change * (first - 1)
            else:
                first = 1
            temp = self.find_index_(first)
            result.append(str(temp))
        return ''.join(result)

s = Solution()

print(s.getPermutation(1, 1))