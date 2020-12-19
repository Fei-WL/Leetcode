from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]):
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 如果用[[0]*len(matrix)]*len(matrix)，那么就会导致最后这几行的结果是一样的
        # 使用了辅助矩阵
        # 还有两种，分别是利用四个等式变换，构建旋转；还有个是先翻转，再转置
        temp_matrix = [[0]*len(matrix) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                temp_matrix[i][j] = matrix[len(matrix)-1-j][i]
        matrix[:] = temp_matrix

        """
        # 先翻转，再转置
        n = len(matrix)
        for i in range(int(n/2)):
            for j in range(n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-1-i][j]
                matrix[n-1-i][j] = temp

        for i in range(n):
            for j in range(i, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        """