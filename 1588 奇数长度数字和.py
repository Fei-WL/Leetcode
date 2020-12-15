class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0

        if len(arr) == 0:
            return result

        for length in range(1, len(arr) + 1, 2):
            for jdx in range(len(arr) - length + 1):
                result += sum(arr[jdx:jdx + length])

        return result