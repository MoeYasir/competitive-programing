class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        
        #return: True or False
        dict_A = {}
        dict_B = {}
        
        for val in A:
            if val in dict_A :
                dict_A [val] += 1
            else:
                dict_A [val] = 1
                
        for val in B:
            if val in dict_B :
                dict_B [val] += 1
            else:
                dict_B [val] = 1
                
        return int(dict_B==dict_A)
                
