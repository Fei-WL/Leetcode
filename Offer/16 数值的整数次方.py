class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = x
        if n < 0:
            limit = -n
        elif n > 0:
            limit = n
        else:
            return 1
        
        count = 1
        while True:
            if count * 2 > limit:
                break
            result *= result
            count *= 2
        
        for idx in range(count, limit):
            result *= x
        if n < 0:
            result = 1/result

        return result

Solution().myPow(0.00001, 2147483647)