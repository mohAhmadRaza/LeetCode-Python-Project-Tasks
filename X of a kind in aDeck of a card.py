class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        hashmap = Counter(deck)
        count = list(hashmap.values())
        return reduce(gcd, count) > 1
        
