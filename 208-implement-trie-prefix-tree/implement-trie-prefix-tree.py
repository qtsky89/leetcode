class TrieNode:
    def __init__(self, character: str, is_word: bool):
        self._character = character
        self._is_word = is_word
        self._next: dict[str, TrieNode] = {}

class Trie:
    def __init__(self):
        self._root = TrieNode(None, False)
        

    def insert(self, word: str) -> None:
        p = self._root

        for w in word:
            if w not in p._next:
                p._next[w] = TrieNode(w, False)
            p = p._next[w]
        
        p._is_word = True
    
    def search(self, word: str) -> bool:
        p = self._root

        for w in word:
            if w not in p._next:
                return False
            p = p._next[w]
        
        return p._is_word

    def startsWith(self, prefix: str) -> bool:
        p = self._root

        for r in prefix:
            if r not in p._next:
                return False
            p = p._next[r]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)