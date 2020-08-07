import collections

class Solution:
    def __init__(self,val=0,left=None,right= None):
        self.val = val
        self.left =left
        self.right = right
        
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        dict1 = collections.defaultdict(list)
        queue = [(root,0)]
        while queue:
            new = []
            dict2 = collections.defaultdict(list)
            for node,s in queue:
                dict2[s].append(node.val)
                if node.left: new += (node.left,s-1),
                if node.right: new += (node.right,s+1),
            for i in dict2: dict1[i].extend(sorted(dict2[i]))
            queue = new
        
        return [dict1[i] for i in sorted(dict1)]
