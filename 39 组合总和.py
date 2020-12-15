import copy
class Solution:
    def combinationSum(self, candidates, target: int):
        self.result = []
        candidates.sort()

        sum_list = []
        self.deep(sum_list, target, candidates)

        return self.result

    def deep(self, sum_list, target, candidates):
        for index in range(len(candidates)):
            sum_list.append(candidates[index])
            if sum(sum_list) == target:
                temp = sorted(copy.deepcopy(sum_list))
                if temp not in self.result:
                    self.result.append(temp)
                sum_list.pop(-1)
                return
            elif sum(sum_list) < target:
                self.deep(sum_list, target, candidates)
                sum_list.pop(-1)
            else:
                sum_list.pop(-1)
                return

s = Solution()
candidates = [2,3,5]
target = 8
print(s.combinationSum(candidates, target))
