class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        p1, p2 = 0, k-1

        '''
        a b c i i i d e f
        ^   ^
        '''

        max_count = 0

        tmp_count = 0
        for i in range(0, k):
            if s[i] in {'a', 'e', 'i', 'o', 'u'}:
                tmp_count += 1
        
        while p2 <= len(s)-1:
            max_count = max(max_count, tmp_count)

            if p2 + 1 <= len(s)-1 and s[p2+1] in {'a', 'e', 'i', 'o', 'u'}:
                tmp_count += 1
            if s[p1] in {'a', 'e', 'i', 'o', 'u'}:
                tmp_count -=1

            p1, p2 = p1+1, p2+1
        return max(max_count, tmp_count)


        