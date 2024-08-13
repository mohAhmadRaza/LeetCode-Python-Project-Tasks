class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        # Applying hashmap to count frequency
        frequency = Counter(words)
        
        # Sorting the hashmap according to keys in lexicographical order
        sorted_frequent_words = sorted(frequency.items(), key=lambda x:x[0])

        # Now again converting the sorted list into dictionary
        sorted_dict = collections.OrderedDict(sorted_frequent_words)

        # now sorting lexicographical dictionary into sorted by value list
        sorted_frequent_words = sorted(sorted_dict.items(), key=lambda x:x[1], reverse=True)

        # Now again converting the sorted list into dictionary
        sorted_dict = collections.OrderedDict(sorted_frequent_words)

        # Extracting keys and builting a list
        top_k = list(sorted_dict.keys())[:k]
        
        # returning listed sorted frequent strings
        return top_k
