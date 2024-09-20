class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        c = [colors[-1]]
        c.extend(colors)
        c.append(colors[0])
        count = 0

        for i in range(1, len(c) - 1):
            if c[i] != c[i-1] and c[i] != c[i+1]:
                count += 1
            
        return count


############## Method 2 ###########

class Solution:
  def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        count = 0
        if colors[-1] != colors[0] and colors[1] != colors[0]:
            count += 1
        
        if colors[-1] != colors[0] and colors[-1] != colors[-2]:
            count += 1
        
        for i in range(1, len(colors) - 1):
            if colors[i] != colors[i-1] and colors[i] != colors[i+1]:
                count += 1
        
        return count
        

            
