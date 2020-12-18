class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # 计数，总计各个字符的ASCII码总和，再把t的ASCII码总和减去s的ASCII码总和
        return chr(sum([ord(item) for item in t]) - sum([ord(item) for item in s]))