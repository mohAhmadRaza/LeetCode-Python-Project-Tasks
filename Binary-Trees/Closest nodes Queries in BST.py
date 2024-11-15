# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
       
        def DFS(node, data):
            if not node:
                return None

            DFS(node.left, data)
            data.append(node.val)
            DFS(node.right, data)
        
        data = []
        DFS(root, data)
        n = len(data)

        def calc(val):
            index = bisect.bisect_left(data, val)
            if index == n:
                return data[-1], -1
            if data[index] == val:
                return [val, val]
            if index == 0:
                return [-1, data[0]]
            
            return [data[index-1], data[index]]

        
        return [calc(val) for val in queries]


################################################# Solution : 02 ################################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
       res = []
       for i in range(len(queries)):
            maximum_val, minimum_val, val, node = -1, -1, queries[i], root

            while node:
                if node.val == val:
                    minimum_val, maximum_val = val, val
                    return

                if val > node.val:
                    if maximum_val == -1:
                        maximum_val = node.val
                    else:
                        maximum_val = max(maximum_val, node.val)
                    node = node.right
                
                if val < node.val:
                    if minimum_val == -1:
                        minimum_val = node.val
                        minFound = True
                    else:
                        minimum_val = min(minimum_val, node.val)
                    node = node.left
            
            res.append([maximum_val, minimum_val])
        
       return res


###################################################### Solution : 03 ########################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
       res = []
       for i in range(len(queries)):
            maximum_val, minimum_val, val, node = -1, -1, queries[i], root

            def DFS(node):
                if node.val == val:
                    minimum_val, maximum_val = val, val
                    return

                if val > node.val:
                    if maximum_val == -1:
                        maximum_val = node.val
                    else:
                        maximum_val = max(maximum_val, node.val)
                    DFS(node.right)
                
                if val < node.val:
                    if minimum_val == -1:
                        minimum_val = node.val
                        minFound = True
                    else:
                        minimum_val = min(minimum_val, node.val)
                    DFS(node.left)

            DFS(root)
            res.append([maximum_val, minimum_val])
        
       return res
