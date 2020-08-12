class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal=[]
        rowIndex +=1
        c =1
        for i in range(1,rowIndex+1):
            pascal.append(c)
            c = int(c*(rowIndex-i)/i)
        
        return pascal
        
