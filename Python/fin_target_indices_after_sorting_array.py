class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        myList=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                myList.append(i)
        return myList
       
        

        
