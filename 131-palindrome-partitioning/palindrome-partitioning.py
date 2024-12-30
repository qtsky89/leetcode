def is_palindrom(s: str) -> bool:
    p1, p2 = 0, len(s)-1

    while p1 <= p2:
        if s[p1] != s[p2]:
            return False
        p1, p2 = p1+1, p2-1
    
    return True
    

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        ret: list[list[str]] = []

        def dfs(current_work: list[str], current_i: int) -> None:
            if current_i == len(s):
                ret.append(current_work)
                return
            
            for j in range(current_i, len(s)):
                if is_palindrom(s[current_i:j+1]):
                    dfs(current_work[:] + [s[current_i:j+1]], j+1)
        
        dfs([], 0)

        return ret
        

        