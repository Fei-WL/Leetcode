from collections import Counter

class Solution:
    def longestPalindrome(self, s) -> int:
        dic = Counter(s)
        values = list(dic.values())
        double = []
        odd = []
        values.sort()
        for value in values:
            if value % 2 == 0:
                double.append(value)
            else:
                odd.append(value-1)
        if len(odd) != 0:
            return sum(double) + sum(odd) + 1
        else:
            return sum(double)


str = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicate" \
      "dcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedi" \
      "cpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirl" \
      "ivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddot" \
      "hisButinalargersensewecannotdedicatewecannotconsecratewecannothallowt" \
      "hisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfa" \
      "raboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongr" \
      "ememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforustheliv" \
      "ingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughthereh" \
      "avethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattd" \
      "afskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiont" \
      "othatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehigh" \
      "lyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodsh" \
      "allhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforth" \
      "epeopleshallnotperishfromtheearth"
print(len(list(set(str))))
s = Solution()
print(s.longestPalindrome(str))