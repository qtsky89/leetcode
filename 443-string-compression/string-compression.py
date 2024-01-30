class Solution:
    def compress(self, chars: List[str]) -> int:
        '''
        chars = [a,  a,  a, a, a, b,   b,   c,   c,   c]
                 ^   5   b  2  c  3                   ^        
        '''

        # p1 is for writing, p2 is for counting
        p1, p2 = 0, 0

        char_group = chars[0]
        while p2 <= len(chars)-1:
            count = 0
            count_str = ''
            while p2 <= len(chars)-1 and char_group == chars[p2]:
                count += 1
                p2 += 1
            
            chars[p1] = char_group
            if count == 1:
                p1 += 1
                char_group = chars[p2] if p2 <= len(chars)-1 else ''
                continue

            count_str = str(count)
            for i in range(len(count_str)):
                p1+=1
                chars[p1] = count_str[i]
            p1 += 1
            
            char_group = chars[p2] if p2 <= len(chars)-1 else ''
        return p1
        

