class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def tree(nums : List[int]):
    if not nums:
        return None
    
    mid = len(nums) // 2
    root = Node(nums[mid])
    
    root.left = tree(nums[:mid])
    root.right = tree([nums[mid+1:]])
    
    return root
    
