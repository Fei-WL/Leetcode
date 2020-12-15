import math
from collections import Counter

class Solution:
    def isPrime(self, x):
        if x == 2:
            return True
        for idx in range(2, int(math.sqrt(x)+1)):
            if x % idx == 0:
                return False
        return True

    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        self.result = [False] * n

        self.result[0], self.result[1] = True, True

        for idx in range(2, n):
            if self.result[idx]:
                continue
            if not self.isPrime(idx):
                self.result[idx] = True
            else:
                temp = idx
                for t in range(2, n):
                    if t * temp >= n:
                        break
                    if not self.result[t * temp]:
                        self.result[t * temp] = True
        result = Counter(self.result)
        return result[False]

print(Solution().countPrimes(10))