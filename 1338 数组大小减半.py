import collections
class Solution:
    def minSetSize(self, arr:list) -> int:
        dic = collections.Counter(arr)

        keys = []
        count = 0
        for key, value in dic.most_common():
            keys.append(key)
            count += value
            if count >= len(arr)/2:
                return len(keys)

s = Solution()
arr = [3,3,3,3,5,5,5,2,2,7]
print(s.minSetSize(arr))