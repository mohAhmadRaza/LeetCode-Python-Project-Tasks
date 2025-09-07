class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams_looking = defaultdict(list)

        for a in strs:
            anagrams_looking["".join(sorted(a))] += [a]
        
        return list(anagrams_looking.values())
        


