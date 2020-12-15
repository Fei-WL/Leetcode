from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        while len(pushed) != 0:
            stack.append(pushed[0])
            pushed.pop(0)

            while len(stack) != 0 and popped[0] == stack[-1]:
                stack.pop(-1)
                popped.pop(0)

        popped.reverse()

        if popped == stack:
            return True
        return False

pushed = [2,1,0]

popped = [1,2,0]

Solution().validateStackSequences(pushed, popped)