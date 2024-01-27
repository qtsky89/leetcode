class TrieNode:
    def __init__(self, char: str):
        self._char = char
        self._next = {}
        self._is_word = False

class Trie:
    def __init__(self):
        self._root = TrieNode(None)

    def add_word(self, word: str):
        p = self._root

        for w in word:
            if w not in p._next:
                p._next[w] = TrieNode(w)
            p = p._next[w]
        p._is_word = True
    
    def get_suggestion(self, word: str) -> list[str]:
        p = self._root

        ret: list[str] = []
        for w in word:
            if w not in p._next:
                return None
            p = p._next[w]
        
        q = deque([[p, word]])

        ret: list[str] = []
        while q:
            item, current_word = q.popleft()
                        
            if item._is_word:
                ret.append(current_word)

            for key in item._next:
                q.append([item._next[key], current_word + key])
        
        ret.sort()
        return ret[:3]
                
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        trie = Trie()

        for product in products:
            trie.add_word(product)
        
        ret: list[list[str]] = []

        for i in range(len(searchWord)):
            ret.append(trie.get_suggestion(searchWord[:i+1]))
        return ret
