class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, number):
        node = self.root
        for char in str(number):
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def findPrefixLength(self, number):
        node = self.root
        prefixLength = 0

        for char in str(number):
            if char in node.children:
                prefixLength += 1
                node = node.children[char]
            else:
                break
        return prefixLength

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        for i in arr1:
            self.insert(i)
        
        max_length = 0
        for i in arr2:
            max_length = max(max_length, self.findPrefixLength(i))
        
        return max_length
