********************************************Solution : 1****************************************(TestCases : 81/100)
  class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort()

        HashMap = Counter(arr)
        for i in arr:
            
            if i > 0:
                if i*2 in HashMap:
                    HashMap[i] -= 1
                    HashMap[i*2] -= 1
            
            elif i < 0:
                if i//2 in HashMap:
                    HashMap[i] -= 1
                    HashMap[i//2] -= 1
        Value = list(HashMap.values())
        return len(set(Value)) == 1

******************************************Solution : 3***************************************(BEST)
        for i in sorted(arr, key=abs):

            if HashMap[i] > 0 and HashMap[2*i] > 0:
                HashMap[i] -= 1
                HashMap[i*2] -= 1
            
            elif HashMap[i] > 0:
                return False
        
        return True

