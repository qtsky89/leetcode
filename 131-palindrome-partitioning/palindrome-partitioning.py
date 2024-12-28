def is_palindrome(s: str) -> bool:
    l, r = 0, len(s)-1

    while l <= r:
        if s[l] != s[r]:
            return False
        
        l, r = l+1, r-1
    return True
    


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        s = a a b
            c   j

        [a a b]
        [aa b]


        '''

        ret: list[list[str]] = []

        def dfs(current_work: list[str], current_index: int) -> None:
            if current_index == len(s):
                ret.append(current_work)
                return

            for j in range(current_index, len(s)):
                new_char = s[current_index:j+1]
                if is_palindrome(new_char):
                    dfs(current_work[:] + [new_char], j+1)

        dfs([], 0)

        return ret

