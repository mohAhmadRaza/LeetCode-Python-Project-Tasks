class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def symmetric(root):
    def isMirror(left, right):
        if not left and not right:
            return True
        if not right or not left:
            return False
        
        return left.val == right.val and isMirror(left.left, right.right) and isMirror(left.right, right.left)
    
    return isMirror(root.left, root.right) if root else True
