from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        nums.sort()
        import copy
        def deep(tmp, subset):
            for index in range(len(subset)):
                tmp.append(subset[index])
                tmp.sort()
                if tmp not in self.result:
                    tp = copy.deepcopy(tmp)
                    self.result.append(tp)
                if index < len(subset):
                    deep(tmp, subset[index+1:])
                if len(tmp) != 0:
                    tmp.pop(-1)

        self.result.append([])
        tmp = []
        deep(tmp, nums)
        return self.result

s = Solution()
nums = [4, 1, 0]
print(s.subsets(nums))