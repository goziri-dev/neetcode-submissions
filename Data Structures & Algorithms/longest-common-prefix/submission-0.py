class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sub_strings = {'': len(strs)}
        for string in strs:
            sub_str = ''
            for char in string:
                sub_str += char
                sub_strings[sub_str] = sub_strings.get(sub_str, 0) + 1
        return max(sub_strings, key=lambda x: (sub_strings[x], len(x)))

        