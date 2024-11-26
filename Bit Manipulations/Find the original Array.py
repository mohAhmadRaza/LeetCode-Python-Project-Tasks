class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        
        resultingArray = [pref[0]]

        for i in range(1, len(pref)):
            bitA, bitB = 0, 0

            for bit in range(0, 32):
                mask = 1<<bit

                bitA |= (pref[i] & mask)
                bitB |= (pref[i-1] & mask)


            resultingArray.append(bitB ^ bitA)
        
        return resultingArray

######################################## SOLUTION : 2 #####################################
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        resultingArray = [pref[0]]  # Start with the first element
        
        for i in range(1, len(pref)):
            # Simply XOR the current prefix with the previous one to get the resulting element
            resultingArray.append(pref[i] ^ pref[i - 1])
        
        return resultingArray
