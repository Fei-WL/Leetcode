"""
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false
"""

class Solution:
    def __init__(self):
        self.direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    def exist(self, board, word: str) -> bool:
        starts = []
        self.board = board
        self.word = word
        self.x_limit = len(board[0])
        self.y_limit = len(board)

        for row in range(len(board)):
            for index in range(len(board[row])):
                if word[0] == board[row][index]:
                    starts.append([row, index])

        for index in range(len(starts)):
            points = [starts[index]]
            temp_word = board[starts[index][0]][starts[index][1]]
            for direct in self.direction:
                if self.deep(points, direct, temp_word):
                    return True

        return False

    def deep(self, points, direction, temp_word):
        if temp_word == self.word:
            return True

        row = points[-1][0] + direction[0]
        line = points[-1][1] + direction[1]

        if [row, line] in points:
            return False
        if row < 0 or row >= self.y_limit or line < 0 or line >= self.x_limit:
            return False

        temp_word += self.board[row][line]
        points.append([row, line])
        if temp_word == self.word[:len(temp_word)]:
            if len(temp_word) == len(self.word):
                return True
            for direct in self.direction:
                if self.deep(points, direct, temp_word):
                    return True

        points.pop(-1)
        temp_word = temp_word[:-1]
        return False

s = Solution()
board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCB"
print(s.exist(board, word))