class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lessThanPivot = [num for num in nums if num<pivot]
        greaterThanPivot = [num for num in nums if num>pivot]
        equalsPivot = [num for num in nums if num==pivot]
        result = lessThanPivot + equalsPivot+greaterThanPivot 
        return result

        
