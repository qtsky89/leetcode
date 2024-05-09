class TrieNode:
    def __init__(self, char: str|None, is_word: bool|None) -> None:
        self.char = char
        self.is_word = is_word
        self.next: dict[str, TrieNode] = {}

class WordDictionary:
    def __init__(self):
        # make dummy trie node
        self.trie = TrieNode(None, None)


    def addWord(self, word: str) -> None:
        p = self.trie

        for w in word:
            if w not in p.next:
                p.next[w] = TrieNode(w, False)
            
            p = p.next[w]

        p.is_word = True    
    
    def search(self, word: str) -> bool:
        ret = False
        def dfs(p: TrieNode, i: str) -> None:
            if i == len(word)and p.is_word:
                nonlocal ret
                ret = True
                return

            if i == len(word):
                return

            if word[i] == '.':
                for key in p.next:
                    dfs(p.next[key], i+1)
            elif word[i] in p.next:
                dfs(p.next[word[i]], i+1)
                
        dfs(self.trie, 0)

        return ret
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)