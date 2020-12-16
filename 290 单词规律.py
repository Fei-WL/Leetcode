class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        inputs = s.split(" ")
        keys = list(pattern)

        if len(inputs) != len(keys):
            return False

        pattern_dict = {}

        for idx in range(len(keys)):
            key = keys[idx]
            value = inputs[idx]
            if key in pattern_dict.keys():
                if value != pattern_dict[key]:
                    return False
            else:
                if value in pattern_dict.values():
                    return False
                pattern_dict[key] = value

        return True