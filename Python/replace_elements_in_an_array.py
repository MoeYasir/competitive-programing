class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        numsMap = {}
        for i in range(0,len(nums)):
            numsMap[nums[i]] = i
        for ops in operations:
            numsMap[ops[1]] = numsMap[ops[0]]
            numsMap[ops[0]] = None
        for value, index in numsMap.items():
            if index is not None:
                nums[index] = value
        return nums
