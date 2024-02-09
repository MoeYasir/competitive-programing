class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        num = 0
        for i in range(0,len(operations)):
            if "--" in operations[i]:
                num = num-1
            elif "++" in operations[i]:
                num = num+1
        return num
        
        
