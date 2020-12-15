import copy

class Solution:
    def combinationSum4(self, nums, target: int):
        nums.sort()
        self.result = []
        self.target = target
        sum_list = []

        self.deep(sum_list, nums)

        return len(self.result)

    def deep(self, sum_list, candidates):
        for index in range(len(candidates)):
            sum_list.append(candidates[index])
            if sum(sum_list) > self.target:
                sum_list.pop(-1)
                return
            elif sum(sum_list) == self.target:
                temp = copy.deepcopy(sum_list)
                self.result.append(temp)
                sum_list.pop(-1)
                # self.deep(sum_list, candidates[index:])
            else:
                self.deep(sum_list, candidates)
                sum_list.pop(-1)

s = Solution()
nums = [4, 2, 1]
target = 32
print(s.combinationSum4(nums, target))