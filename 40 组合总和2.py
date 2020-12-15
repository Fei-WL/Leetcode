import copy

class Solution:
    def combinationSum2(self, candidates, target: int):
        candidates.sort()
        self.result = []
        self.target = target
        sum_list = []

        self.deep(sum_list, candidates)

        return self.result

    def deep(self, sum_list, candidates):
        for index in range(len(candidates)):
            sum_list.append(candidates[index])
            if sum(sum_list) > self.target:
                sum_list.pop(-1)
                return
            elif sum(sum_list) == self.target:
                temp = sorted(copy.deepcopy(sum_list))
                if temp not in self.result:
                    self.result.append(temp)
                sum_list.pop(-1)
                self.deep(sum_list, candidates[index+1:])
            else:
                self.deep(sum_list, candidates[index+1:])
                sum_list.pop(-1)


s = Solution()
candidates = [2,5,2,1,2]
target = 5
print(s.combinationSum2(candidates, target))