Method 1:

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0

        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if len(words[i]) <= len(words[j]):
                    toCompare = words[j]
                    negativeLength = ( len(words[i])*-1 )-1
                    suffix = toCompare[-1:negativeLength:-1]
                    if words[i] == toCompare[:len(words[i])] and words[i] == suffix[::-1]:
                        count += 1
        return count

Method 2:
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0

        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if len(words[i]) <= len(words[j]):
                    if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                        count += 1
        return count
        
