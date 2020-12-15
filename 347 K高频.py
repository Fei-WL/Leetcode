class Solution:
    def topKFrequent(self, nums, k: int):
        nums = sorted(nums)
        dic = {}
        for num in nums:
            if num in dic.keys():
                dic[num] += 1
            else:
                dic[num] = 0

        dic = dict(sorted(dic.items(), key=lambda kv:(kv[1], kv[0]), reverse=True))

        keys = [key for key, item in dic.items()][:k]

        return keys


s = Solution()
nums = [1,1,1,2,2,2,2,3]
k = 2
print(s.topKFrequent(nums, k))