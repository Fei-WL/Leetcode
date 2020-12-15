class Solution:
    def findLongestChain(self, pairs) -> int:
        pairs.sort()
        dp = [1] * len(pairs)

        for j in range(len(pairs)):
            for i in range(j):
                if pairs[i][1] < pairs[j][0]:
                    dp[j] = max(dp[j], dp[i] + 1)

        return max(dp)

s = Solution()
pairs = [[5,9],[-1,8],[-6,-2],[8,9],[4,8],[3,6],[2,6],[5,9],[-1,6],[-8,-7]]
print(s.findLongestChain(pairs))