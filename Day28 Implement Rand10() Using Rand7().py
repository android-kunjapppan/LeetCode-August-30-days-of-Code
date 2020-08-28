# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        
        c = (rand7() - 1)*7 + rand7() - 1
        return self.rand10() if c>=40 else (c%10) +1
        
        """
        :rtype: int
        """
        
