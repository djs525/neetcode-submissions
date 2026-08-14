# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = collections.deque()
        q.append(root)
        count = 1
        while q:
            lvl = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    lvl.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if lvl:
                if count % 2 == 0:
                    lvl.reverse()
                    res.append(lvl)
                else:
                    res.append(lvl)
            count += 1
        return res