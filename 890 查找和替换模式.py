from typing import List

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def encode(pattern):
            dict = {}
            num = 0
            for index in range(len(pattern)):
                if pattern[index] not in dict.keys():
                    dict[pattern[index]] = num
                    num += 1
            enc_out = [dict[pattern[i]] for i in range(len(pattern))]
            return enc_out

        pattern_enc = encode(pattern)
        result = []
        for word in words:
            if len(word) == len(pattern):
                word_enc = encode(word)
                if word_enc == pattern_enc:
                    result.append(word)
        return result

s = Solution()
words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
print(s.findAndReplacePattern(words, pattern))