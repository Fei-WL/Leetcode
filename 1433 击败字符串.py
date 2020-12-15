class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        def battle(ref, att):
            ref = sorted(ref)
            att = sorted(att)

            for index in range(len(ref)):
                if ref[index] > att[index]:
                    return False

            return True

        s1_num = sorted([ord(t) for t in s1])
        s2_num = sorted([ord(t) for t in s2])

        p = -1

        for index in range(len(s1_num)):
            if s1_num[index] != s2_num[index]:
                p = index
                break

        ref = s1_num[p:] if s1_num[p] < s2_num[p] else s2_num[p:]
        att = s2_num[p:] if s1_num[p] < s2_num[p] else s1_num[p:]

        return battle(ref, att)

s = Solution()
s1 = "leetcodee"
s2 = "interview"
print(s.checkIfCanBreak(s1, s2))