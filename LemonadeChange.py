class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_count = 0
        ten_count = 0

        for i in bills:
            if i == 5:
                five_count += 1
            elif i == 10:
                if five_count == 0:
                    return False
                ten_count += 1
                five_count -= 1
            elif i == 20:
                if ten_count > 0 and five_count > 0:
                    ten_count -= 1
                    five_count -= 1
                elif five_count >= 3:
                    five_count -= 3
                else:
                    return False
        
        return True
