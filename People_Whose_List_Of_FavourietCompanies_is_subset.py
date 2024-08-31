class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        # Convert lists of favorite companies to sets
        favoriteSets = [set(companies) for companies in favoriteCompanies]
        
        result = []
        
        # Check each person's list
        for i in range(len(favoriteSets)):
            is_subset = False
            for j in range(len(favoriteSets)):
                if i != j and favoriteSets[i].issubset(favoriteSets[j]):
                    is_subset = True
                    break
            if not is_subset:
                result.append(i)
        
        return result
