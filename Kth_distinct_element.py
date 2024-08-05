class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hashmap = Counter(arr)

        for key, value in hashmap.items():
            if hashmap[key] == 1:
                k -= 1
            if k == 0:
                return key
        return ""
