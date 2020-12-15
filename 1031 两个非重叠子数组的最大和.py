from typing import List

class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        first = M if L <= M else M
        second = L if L <= M else L
        max = -float("inf")

        for index_i in range(len(A)):
            first_stage = A[index_i: index_i + first]
            for index_j in range(len(A), second-1, -1):
                if index_j - second < index_i + first and index_j - second >= index_i or index_j <= index_i + first and index_j > index_i\
                        or index_i >= index_j - second and index_i < index_j or index_i + first <= index_j and index_i + first > index_j - second:
                    continue
                else:
                    second_stage = A[index_j - second: index_j]
                    result = sum(first_stage) + sum(second_stage)
                    if result > max:
                        print(first_stage, second_stage, result)
                        max = result
        return max

s = Solution()
A = [11,13,12,17,17,19,1,14,4,7,4,8,4]
L = 10
M = 2
print(s.maxSumTwoNoOverlap(A, L, M))