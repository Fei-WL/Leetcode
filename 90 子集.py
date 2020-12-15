class Solution:
    def subsetsWithDup(self, nums: list):
        import copy
        nums.sort()

        result = []
        result.append([])

        def deep(sub: list, nums):
            if sub not in result:
                result.append(copy.deepcopy(sub))
            for index in range(len(nums)):
                sub.append(nums[index])
                if index < len(nums):
                    deep(sub, nums[index+1:])
                if len(sub) != 0:
                    sub.pop(-1)

        sub = []
        deep(sub, nums)

        return result

s = Solution()
nums = [1, 2, 1, 2]
print(s.subsetsWithDup(nums))