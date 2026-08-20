class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_mapping = {}
        for i, num in enumerate(nums):
            if num in diff_mapping:
                return [diff_mapping[num], i]
            diff_mapping[target-num] = i
        