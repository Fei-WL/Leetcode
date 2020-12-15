class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        height = len(matrix)
        weight = len(matrix[0])
        x = []
        y = []
        for index in range(len(matrix)):
            if 0 in matrix[index]:
                x.append(index)
                temp_y = self.get_res(matrix[index])
                y += temp_y

        list(set(x)).sort()
        list(set(y)).sort()

        for _x in x:
            matrix[_x] = [0] * weight

        for h in range(height):
            if matrix[h][0] == 0:
                continue
            for w in y:
                matrix[h][w] = 0


    def get_res(self, nums):
        res = []
        for index in range(len(nums)):
            if nums[index] == 0:
                res.append(index)
        return res

s = Solution()
matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
s.setZeroes(matrix)
print(matrix)