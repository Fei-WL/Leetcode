import re

class Solution:
    def minimumOperations(self, leaves: str) -> int:
        reds = re.split(r'[y]*', leaves)
        yellows = re.split(r'[r]*', leaves)

        if len(reds) == 0:
            return 0

        reds_min = min(reds[1:-1], key=len)
        yellows_min =

        return 0

leaves = "rrryyyrryyyrr"

Solution().minimumOperations(leaves)