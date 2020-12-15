import copy
class Solution:
    def combinationSum3(self, k: int, n: int):
        t = n if n <= 9 else 9
        candidates = [i + 1 for i in range(t)]
        self.len = k
        self.target = n
        self.result = []
        sumlist = []
        self.deep(sumlist, candidates)
        return self.result

    def deep(self, sum_list, candidates):
        for index in range(len(candidates)):
            sum_list.append(candidates[index])
            if sum(sum_list) > self.target:
                sum_list.pop(-1)
                return
            elif sum(sum_list) == self.target:
                temp = sorted(copy.deepcopy(sum_list))
                if temp not in self.result and len(sum_list) == self.len:
                    self.result.append(temp)
                sum_list.pop(-1)
                self.deep(sum_list, candidates[index + 1:])
            else:
                self.deep(sum_list, candidates[index + 1:])
                sum_list.pop(-1)

s = Solution()
k = 3
n = 9
print(s.combinationSum3(k, n))