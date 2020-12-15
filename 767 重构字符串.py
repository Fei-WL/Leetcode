from collections import Counter

class Solution:
    def judge(self, total, count):
        left = total - count
        if count - left >= 2:
            return False
        else:
            return True

    def reorganizeString(self, S: str) -> str:
        if len(S) <= 2:
            if len(S) == 1:
                return S
            else:
                if S[0] == S[1]:
                    return ""
                else:
                    return S
        if len(S) == 0:
            return ""

        str_count = Counter(S)
        str_count = dict(sorted(str_count.items(), key=lambda kv:(kv[1], kv[0]), reverse=True))
        result = [None] * len(S)
        while len(str_count) != 0:
            keys = list(str_count.keys())
            values = list(str_count.values())
            if len(keys) >= 2:
                start = result.index(None)
                result[start] = keys[0]
                result[start+1] = keys[1]
                str_count[keys[0]] -= 1
                str_count[keys[1]] -= 1
                if str_count[keys[0]] == 0:
                    str_count.pop(keys[0])
                if str_count[keys[1]] == 0:
                    str_count.pop(keys[1])
            else:
                if values[0] > 1:
                    return ""
                else:
                    start = result.index(None)
                    result[start] = keys[0]
                    str_count[keys[0]] -= 1
                    if str_count[keys[0]] == 0:
                        str_count.pop(keys[0])
            str_count = dict(sorted(str_count.items(), key=lambda kv:(kv[1], kv[0]), reverse=True))

        return "".join(result)

print(Solution().reorganizeString("aaabbbcc"))