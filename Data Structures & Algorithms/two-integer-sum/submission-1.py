class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index, diff_mapping = {}, {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in diff_mapping:
                return [num_index[diff], i]
            diff_mapping[num] = diff
            num_index[num] = i
        