class Solution:
    def singleNumbers(self, nums: list):
        index = 0
        nums.sort()
        tag = nums[0] - 1
        while index < len(nums):
            if index+1 < len(nums):
                if tag == nums[index] or nums[index] == nums[index+1]:
                    tag = nums[index]
                    nums.pop(index)
                else:
                    index += 1
            else:
                if tag == nums[index]:
                    tag = nums[index]
                    nums.pop(index)
                else:
                    index += 1
        return nums


s = Solution()
nums = [4,1,4,6]
print(s.singleNumbers(nums))