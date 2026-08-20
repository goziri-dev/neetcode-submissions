class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map, t_map = self.get_mapping(s), self.get_mapping(t)
        if set(s_map.keys()) != set(t_map.keys()):
            return False
        for key in s_map.keys():
            if s_map[key] != t_map[key]:
                return False
        return True

    def get_mapping(self, s: str) -> dict:
        mapping = {}
        for char in s:
            mapping[char] = mapping.get(char, 0) + 1
        return mapping