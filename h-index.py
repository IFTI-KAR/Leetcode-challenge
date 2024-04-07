# 
        

class Solution(object):
    def hIndex(self, citations):
        n=len(citations)
        tmp=[0]*(n + 1)  
        for i in range(n):
            if citations[i]>=n:
                tmp[n]+=1
            else:
                tmp[citations[i]]+=1  
        total=0
        for i in range(n,-1,-1):
            total+=tmp[i]
            if total>=i:
                return i
        return 0  


        
