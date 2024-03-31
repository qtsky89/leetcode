class Solution:
    def wordBreak(self, s: str, word_dict: List[str]) -> bool:
        '''
        s = 'leetcode' word_dict = ['leet', 'code']
        '''

        ret = False

        visited = set()
        def dfs(current_word: str) -> None:
            nonlocal ret

            if current_word in visited:
                return
            else:
                visited.add(current_word)

            if current_word == '':
                ret = True
            
            for word in word_dict:
                if current_word [:len(word)] == word:
                    dfs(current_word[len(word):])
        dfs(s)

        return ret