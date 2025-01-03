class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        f l o w e r
        f l o w
        f l i g h t
        ^

        '''

        n = min([len(s) for s in strs])
        
        for j in range(n):
            tmp = []
            for i in range(len(strs)):
                if strs[0][j] == strs[i][j]:
                    tmp.append(strs[i][j])

            if len(tmp) != len(strs):
                return strs[i][:j]
        
        return strs[0][:n]
                
