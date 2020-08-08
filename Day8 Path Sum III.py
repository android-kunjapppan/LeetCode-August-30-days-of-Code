# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
            # set {0: 1} as default so it will be valid for leaf node
            self.acc_map={0:1}
    def pathsumrecursive(self,root,acc,sum):
        if not root:
            return 0
    
        current_acc= acc+root.val
        self.acc_map.setdefault(current_acc,0)
        self.acc_map[current_acc]+=1
        left_sum = self.pathsumrecursive(root.left,current_acc,sum)
        right_sum = self.pathsumrecursive(root.right,current_acc,sum)
        self.acc_map[current_acc] -=1
        
        return self.acc_map.get(current_acc-sum,0) + left_sum + right_sum
    
    def pathSum(self, root: TreeNode, sum: int) -> int:
        # approach: use a hash map to save accumulative sum of root to 
        #           current node and check if there is a match when return

        return self.pathsumrecursive(root, 0, sum)
        
      
