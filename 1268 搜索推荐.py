class Solution:
    def suggestedProducts(self, products, searchWord: str):
        result = []
        for index in range(len(searchWord)):
            key = searchWord[:index+1]
            temp_result = []
            for item in products:
                if item[:index+1] == key:
                    temp_result.append(item)
            t = sorted(temp_result)
            if len(temp_result) < 3:
                result.append(sorted(t))
            else:
                result.append(sorted(t[:3]))
        return result

s = Solution()
products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
print(s.suggestedProducts(products, searchWord))