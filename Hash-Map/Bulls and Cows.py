class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        count = 0

        CowDict = Counter(secret)
        Cows = 0
        Indexes = ""

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                count += 1
                CowDict[secret[i]] -= 1
        
        for i in range(len(guess)):
            if guess[i] != secret[i] and CowDict[guess[i]] > 0:
                CowDict[guess[i]] -= 1
                Cows += 1

        return str(count) + "A" + str(Cows) + "B"

        
