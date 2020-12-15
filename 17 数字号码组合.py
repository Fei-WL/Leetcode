from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2': 'abc',
               '3': 'def',
               '4': 'ghi',
               '5': 'jkl',
               '6': 'mno',
               '7': 'pqrs',
               '8': 'tuv',
               '9': 'wxyz'}

        def find_result(code: str, temp_result):
            for index in range(len(code)):
                temp_result += code[index]
                find_result()