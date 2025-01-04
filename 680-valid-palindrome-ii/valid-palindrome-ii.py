'''
    a b c c b a x
    ^         ^
      

'''

class Solution:
    def isvalidate(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False

            i, j = i+1, j-1
        
        return True


    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1

        while i < j:
            if s[i] != s[j]:
                if self.isvalidate(s[i+1:j+1]):
                    return True
                elif self.isvalidate(s[i:j]):
                    return True
                else:
                    return False
            i, j = i+1, j-1
        
        return True