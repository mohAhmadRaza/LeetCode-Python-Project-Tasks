class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0

        def CalculatePower(base, exponent):
            if exponent == 0:
                return 1.0
            
            elif exponent % 2 == 0:
                return CalculatePower(base * base, exponent // 2)
            
            else:
                return base * CalculatePower(base * base, (exponent - 1) // 2)
        
        result = CalculatePower(x, abs(n))

        return result if n > 0 else 1/result


##################################### Method : 2 #####################################
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        def CalculatePower(base, exponent):
            if exponent == 0:
                return 1.0
            
            value = value * x
            count = count + 1

            return CalculatePower(count, value)
        
        
        result = CalculatePower(1, 1)

        return result if n > 0 else 1/result
