class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def clean(s: str):
            s = list(s)
            while '#' in s:
                index = s.index('#')
                if index == 0:
                    s.pop(index)
                else:
                    s.pop(index)
                    s.pop(index-1)

            return s

        S = clean(S)
        T = clean(T)

        return S == T

S = "a##c"
T = "#a#c"

Solution().backspaceCompare(S, T)