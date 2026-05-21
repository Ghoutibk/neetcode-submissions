class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_element = {} # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_element:
                return [prev_element[diff], i]
            prev_element[n] = i
        return
    

