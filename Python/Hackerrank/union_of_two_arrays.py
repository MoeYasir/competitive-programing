class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        union_ab=set(a)|set(b)
        return len(union_ab)
