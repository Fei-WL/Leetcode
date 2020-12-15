import math
class Solution:
    def rangeSum(self, nums, n: int, left: int, right: int) -> int:
        sum_list = []
        for skip in range(1, n+1):
            for start in range(n-skip+1):
                sum_list.append(sum(nums[start:start+skip]))
        sum_list.sort()
        return sum(sum_list[left-1:right]) % int(math.pow(10, 9) + 7)
        # print(sum_list.sort())

s = Solution()
nums = [1,2,3,4]
n = 4
left = 3
right = 4
print(s.rangeSum(nums, n, left, right))