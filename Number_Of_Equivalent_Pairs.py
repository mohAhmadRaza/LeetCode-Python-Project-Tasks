Methode 1:

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = 0

        for i in range(len(dominoes)):
            for j in range(i+1, len(dominoes)):
                if dominoes[i][0] == dominoes[j][0] and dominoes[i][1] == dominoes[j][1]:
                    count += 1
                elif dominoes[i][0] == dominoes[j][1] and dominoes[i][1] == dominoes[j][0]:
                    count += 1
        
        return count


Methode 2:
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count_dominos = {}
        count = 0

        for dominoe in dominoes:
            key = tuple(sorted(dominoe))

            if key in count_dominos:
                count += count_dominos[key]
                count_dominos[key] += 1
            else:
                count_dominos[key] = 1
        
        return count
                
