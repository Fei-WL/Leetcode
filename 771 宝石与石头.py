class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        result = 0
        for index in range(len(S)):
            if S[index] in J:
                result += 1
        return result