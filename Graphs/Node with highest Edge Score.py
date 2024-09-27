class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        freq = defaultdict(int)

        for ind, i in enumerate(edges):
            freq[i] += ind
        
        sorted_list = dict(sorted(freq.items(), key=lambda x:x[1], reverse=True))
        keys = list(sorted_list.keys())
        values = list(sorted_list.values())
        count = values.count(values[0])
        keys = sorted(keys[:count])
        return keys[0]


######## Method 2 #########

class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        freq = defaultdict(int)

        for ind, i in enumerate(edges):
            freq[i] += ind

        max_score = -1
        min_node = -1
        for node, score in freq.items():
            if score > max_score or ( score == max_score and node < min_node):
                max_score = score
                min_node = node
        
        return min_node
