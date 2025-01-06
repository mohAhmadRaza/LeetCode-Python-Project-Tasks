########################################################## Optimized Code #########################################################

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        st = list(s)
        n = len(s)

        TotalShifts = [0]*(n+1)

        for shift in shifts:
            start, end, direction = shift
            
            TotalShifts[start] += (1 if direction == 1 else -1)

            if end+1 < n:
                TotalShifts[end+1] -= (1 if direction == 1 else -1)
        
        current = 0
        for i in range(n):
            current += TotalShifts[i]

            netShift = (current % 26 + 26) % 26

            st[i] = chr((ord(st[i]) - ord('a') + netShift) % 26 + ord('a'))

        return ''.join(st)


###################################################### Brute Force Method #############################################################
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s = list(s)
        n = len(s)

        TotalShifts = []

        for shift in shifts:
            start, end, direction = shift
            

            if direction == 1 and start == 0:
                TotalShifts.append(n)
            elif direction == 0 and start == 0:
                TotalShifts.append(-n)
            elif direction == 0 and start != 0:
                TotalShifts.append(-start)
            elif direction == 1 and start != 0:
                TotalShifts.append(start)

            if start != end and direction == 1:
                TotalShifts.append(end)
            elif start != end and direction == 0:
                TotalShifts.append(-end)
            
            if end - start > 1 and direction == 1:
                TotalShifts.extend(list(range(start+1, end)))
            elif end - start > 1 and direction == 0:
                TotalShifts.extend(list(range(-(start+1), -end, -1)))
        

        RequiredShifts = Counter(TotalShifts)
        Required = [0]*(n)

        for a, b in RequiredShifts.items():
            c = abs(a)
            if c == n:
                if a<0:
                    Required[0] -= b
                elif a>0:
                    Required[0] += b
            
            else:
                if a<0:
                    Required[c] -= b
                elif a>0:
                    Required[c] += b
        
        for i in range(n):
            turns = Required[i]
            s[i] = char((ord(s[i]-ord('a')+turns))%26 + ord('a'))
        
        return ''.join(s)
