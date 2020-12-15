class Solution:
    def largestSumAfterKNegations(self, A, K: int) -> int:
        A.sort()
        min_index = 0
        for index in range(K):
            A[min_index] = -A[min_index]
            if A[min_index] > A[min_index+1]:
                min_index = min_index + 1
        return sum(A)

A = [3,-1,0,2]
K = 3
s = Solution()
print(s.largestSumAfterKNegations(A, K))