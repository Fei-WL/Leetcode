class Solution:
    def movesToMakeZigzag(self, nums: list) -> int:
        result_1 = 0
        result_2 = 0
        for index in range(len(nums)):
            if index % 2 == 0:
                d1 = nums[index] - nums[index-1] + 1 if index > 0 and nums[index] >= nums[index-1] else 0
                d2 = nums[index] - nums[index+1] + 1 if index < len(nums)-1 and nums[index] >= nums[index+1] else 0
                result_1 += max(d1, d2)
            else:
                d1 = nums[index] - nums[index-1] + 1 if nums[index] >= nums[index-1] else 0
                d2 = nums[index] - nums[index+1] + 1 if index < len(nums)-1 and nums[index] >= nums[index+1] else 0
                result_2 += max(d1, d2)
        return min(result_1, result_2)

s = Solution()
nums = [9,6,1,6,2]
print(s.movesToMakeZigzag(nums))