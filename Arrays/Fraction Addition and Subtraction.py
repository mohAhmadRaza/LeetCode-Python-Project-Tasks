class Solution:
    def fractionAddition(self, expression: str) -> str:
        s = []
        L = []
        left = 0
        denominator, numerator = "", ""

        while left < len(expression):
            while left < len(expression) and expression[left] != '/':
                numerator += expression[left]
                left += 1
            
            L.append(int(numerator))
            numerator = ""

            # To get integer after '/'
            left += 1

            denominator += expression[left]
            left += 1

            while left < len(expression) and expression[left] != '+' and expression[left] != '-':
                denominator += expression[left]
                left += 1

            s.append(int(denominator))
            denominator = ""

        sums = sum(L)
        if len(set(s)) == 1:
            if sums % s[0] == 0:
                return str(sums//s[0]) + "/" + "1"

            else:
                div = math.gcd(sums, s[0])
                return str(sums//div) + "/" + str(s[0]//div)
        
        else:
            div = 1
            for i in set(s):
                div = div*i//gcd(div, i)

            multiArr = [ (div//s[i])*L[i] for i in range(len(L))]
            print(multiArr)
            sums = sum(multiArr)
            d = math.gcd(sums, div)

            return str(sums//d) + "/" + str(div//d)
