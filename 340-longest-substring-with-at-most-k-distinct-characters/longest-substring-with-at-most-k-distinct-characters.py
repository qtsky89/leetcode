from collections import deque

class Solution:
    '''
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # s = e c e b a,  k = 2
            

        # e => 1, ec => 2, ece => 3
        # c => 1, ce => 2
        # e => 1, eb => 2
        # b => 1, ba => 2
        # a => 1

        result = 3

        max_length = 0
        q = deque()

        for i in range(len(s)):
            q.append((i, i))

        # q = (0, 0) (1, 1) (2, 2) (3, 3) (4, 4)
        while q:
            # start_i=0, end_i=0
            start_i, end_i = q.popleft()

            # c = {e: 1}
            c = Counter(s[start_i:end_i+1])
            if len(c) > k:
                continue
            
            max_length = max(max_length, end_i-start_i+1)

            if end_i+1 <=len(s)-1:
                q.append((start_i, end_i+1))
            
        return max_length
    '''

    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        '''
        s = ' a  b e e' k = 1
                   ^ ^
        '''

        if k == 0:
            return 0

        i, j = 0, 0
        max_length = 0
        counter = defaultdict(int)
        '''
        counter = {
            e : 1
        }
        '''
        while j <= len(s)-1:
            counter[s[j]] += 1

            while i <= len(s)-1 and len(counter) > k:
                counter[s[i]] -= 1
                if counter[s[i]] == 0:
                    del counter[s[i]]

                i += 1
            
            max_length = max(max_length, j-i+1)
            j += 1
        
        return max_length