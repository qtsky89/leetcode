class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        s = "   hellow  world   "
        ret = "world hello"


        s = "the sky is blue"
        ret = "blue is sky the"
        '''
        
        tmp = s.split(" ")[::-1]

        ret = []
        for t in tmp:
            if t != "":
                ret.append(t)
        return " ".join(ret)

        
        