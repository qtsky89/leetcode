class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        23
        ad, ae, af
        bd, be, bf
        cd, ce, cf

        key value
        2   [a, b, c]
        3   [d, e, f]


        1. make these map
        2. using queue
        3. get result until they use all digits
        '''

        if not digits:
            return []

        # 1. make these map
        phone_map = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }

        # 2. using queue
        q = deque()
        # digits[i] = 2
        for alphabet in phone_map[int(digits[0])]:
            # alphabet = a, b, c...
            q.append(alphabet)

        # 3. get result until they use all digits
        ret = []
        while q:
            # item = a
            alphabets = q.popleft()

            if len(alphabets) == len(digits):
                ret.append(alphabets)
                continue
                
            current_index = len(alphabets)-1
            for new_alphabet in phone_map[int(digits[current_index+1])]:
                q.append(alphabets + new_alphabet)
        
        return ret
            

            








        