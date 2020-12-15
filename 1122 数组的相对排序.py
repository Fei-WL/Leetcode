from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        code = {}
        for index in range(len(arr2)):
            code[arr2[index]] = index
        for_code = []
        oov = []
        for index in range(len(arr1)):
            if arr1[index] in code.keys():
                temp = [arr1[index], code[arr1[index]]]
                for_code.append(temp)
            else:
                oov.append(arr1[index])

        temp_result = sorted(for_code, key=lambda k:k[1])
        result = [item[0] for item in temp_result] + sorted(oov)

        return result

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
s = Solution()
print(s.relativeSortArray(arr1, arr2))