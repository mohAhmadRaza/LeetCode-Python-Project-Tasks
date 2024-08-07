class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.endOfWord = True
    
    def search(self, word):
        Word = ""
        node = self.root
        for i in word:
            if i not in node.children:
                return word
            node = node.children[i]
            Word += i
            if node.endOfWord == True:
                return Word
        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()

        for i in dictionary:
            trie.insert(i)
        
        words = sentence.split()
        for i in range(len(words)):
            words[i] = trie.search(words[i])
        
        return " ".join(words)
        
