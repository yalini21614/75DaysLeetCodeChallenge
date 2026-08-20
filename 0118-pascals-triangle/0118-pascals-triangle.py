class Solution(object):
    def generate(self, numRow):
        result=[]
        for i in range(numRow):
            row=[1]*(i+1)
            for j in range(1,i):          
                 row[j]=result[i-1][j-1]+result[i-1][j]
            result.append(row)
        return result
