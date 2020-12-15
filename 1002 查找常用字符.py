from typing import List
from collections import Counter

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        result = A[0]
        for index in range(len(A)):
            result = [i for i in A[index] if i in result]

        return result

A = ["cool","lock","cook"]

print(Solution().commonChars(A))