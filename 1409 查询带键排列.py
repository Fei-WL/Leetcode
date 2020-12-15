import collections

class Solution:
    def processQueries(self, queries, m: int):
        result = []
        P = [i+1 for i in range(m)]
        for index in range(len(queries)):
            p = P.index(queries[index])
            result.append(p)
            P.pop(p)
            P.insert(0, queries[index])
        return result

s = Solution()
queries = [7,5,5,8,3]
m = 8
print(s.processQueries(queries, m))
