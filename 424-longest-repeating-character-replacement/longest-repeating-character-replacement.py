class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        s: str, k: int

        example1.
            s = "ABAB" k = 2
                 AAAA
                 BBBB   => 4
        
        example2.
            s= "AABABBA"  k = 1
                AAAA => 4


        s = "A A A B A B B A C C A A B"
            i,j
        longest = 6
        
        k = 2 -> 1
            1 -> 0
        '''

        i, j = 0, 0
        longest_count = 0
        '''
        {
            A : 1
        }
        '''
        c = Counter(s[0])
        while j <= len(s)-1:
            # valid check
            most_char_count = max(c.values())
            # not valid
            if (j-i+1) - most_char_count > k:
                c[s[i]] -= 1
                i += 1
                continue

            longest_count = max(longest_count, j - i + 1)

            # moving forward
            if j+1 <= len(s) -1:
                c[s[j+1]] += 1
            j += 1
        return longest_count
        
                
            
            




            
            


