class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = ""
        for i, char in enumerate(strs[0]):
            for j in range(len(strs)):
                if len(strs[j]) - 1 < i:
                    return longest_prefix
                if char != strs[j][i]:
                    return longest_prefix
            longest_prefix += char
        return longest_prefix