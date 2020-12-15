from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        tp_res = []
        import copy
        def deep(tp_res: list, next_set: list):
            for index in range(len(next_set)):
                tp_res.append(next_set[index])
                temp_set = copy.deepcopy(next_set)
                temp_set.pop(index)
                if len(temp_set) == 0:
                    if tp_res not in result:
                        cop = copy.deepcopy(tp_res)
                        result.append(cop)
                    tp_res.pop(-1)
                    return
                deep(tp_res, temp_set)
                if len(tp_res) != 0:
                    tp_res.pop(-1)
            # tp_res.pop(-1)

        deep(tp_res, nums)


        return result



nums = [1,2,1,2]
s = Solution()
print(s.permuteUnique(nums))