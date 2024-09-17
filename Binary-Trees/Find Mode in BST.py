# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        q, freq = deque([root]), defaultdict(int)

        while q:
            length = len(q)

            for i in range(length):
                curr = q.popleft()
                freq[curr.val] += 1

                if curr.left:
                    q.append(curr.left)
                
                if curr.right:
                    q.append(curr.right)
        
        sorted_list = sorted(freq.values(), reverse=True)
        index = sorted_list.count(sorted_list[0])
        sorted_keys = dict(sorted(freq.items(), key=lambda x:x[1],  reverse=True))
        return list(sorted_keys.keys())[:index]


