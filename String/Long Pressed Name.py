class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        if len(name) > len(typed):
            return False
        
        other = 0
        string = ""

        for i in range(len(typed)):
            if other >= len(name) and name[other-1] != typed[i]:
                return False

            elif ( other < len(name) ) and ( name[other] == typed[i] ):
                string += name[other]
                other += 1
            
            elif ( other < len(name) ) and ( name[other] != typed[i] ):
                if i == 0:
                    return False

                elif typed[i] == typed[i-1]:
                    continue
            
                else:
                    return False
        
        if (other == len(name) - 1 ) or (name != string):
            return False

        return True


        
