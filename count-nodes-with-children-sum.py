from logging import root
from tkinter.messagebox import NO


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def ChildrenSum(root):
    left = 0
    right = 0
    if(root == None):
        return 0
    else:
        if(root.left != None):
            left = root.left.data
        if(root.right != None):
            right = root.right.data

        if(root.data == left+right):
            return 1+ChildrenSum(root.left)+ChildrenSum(root.right)
        else:
            return 0


root = TreeNode(100)
root.left = TreeNode(51)
root.right = TreeNode(49)
root.left.left = TreeNode(20)
root.left.right = TreeNode(31)
root.right.left = TreeNode(23)
root.right.right = TreeNode(26)

print(ChildrenSum(root))
