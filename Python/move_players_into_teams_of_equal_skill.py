class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
      skill.sort()  
      n = len(skill)
      group_count = n//2
      s = sum(skill) // group_count
      chemistry = 0
      for i in range(n//2):
            a = skill[i]
            b = skill[n-i-1]
            if a + b != s:
                return -1
            chemistry += a*b       
      return chemistry      
        

     
        
