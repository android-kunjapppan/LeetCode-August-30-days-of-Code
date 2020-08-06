class Solution:
    
    def sum_of_squares(self,n):
        sum = 0
        while n>0:
            x= n%10
            sum+=x*x
            n = n//10
        return sum
    

    def isHappy(self, n: int) -> bool:
        a1 = b1 = n
        
        a1 = self.sum_of_squares(a1)
        b1 = self.sum_of_squares(a1)
        
        while (a1!=b1):
            a1 = self.sum_of_squares(a1)
            b1 = self.sum_of_squares(self.sum_of_squares(b1))

            
            if b1 ==1:
                return True
        return a1 ==1
