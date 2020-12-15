class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name == typed:
            return True
        if len(name) > len(typed):
            return False
        set_name = set(name)
        set_type = set(typed)
        if set_name != set_type:
            return False
        name_p = 0
        type_p = 0
        while name_p < len(name):
            span_name = []
            span_type = []
            value = name[name_p]
            while name[name_p] == value:
                span_name += value
                name_p += 1
                if name_p >= len(name):
                    break
            if type_p < len(typed):
                while typed[type_p] == value:
                    span_type += value
                    type_p += 1
                    if type_p >= len(typed):
                        break
            if len(span_type) < len(span_name):
                return False
        return True

name = "alex"
typed = "aaleex"
Solution().isLongPressedName(name, typed)