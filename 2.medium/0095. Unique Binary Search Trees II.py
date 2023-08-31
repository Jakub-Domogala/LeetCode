from utilities.TreeNode import TreeNode


class Solution(object):
    def generateTrees(self, n):
        def insert_elem(root, elem):
            if root is None:
                return TreeNode(elem)
            if root.val < elem:
                root.right = insert_elem(root.right, elem)
                return root
            else:
                root.left = insert_elem(root.left, elem)
                return root
        root = None
        # for i in range(n):
        #     root = insert_elem(root, i)
        # return root
        def get_trees_from(nums = nums):
            result = []
            if len(nums) == 0:
                return []
            for i in nums:
                
            
        # result = []
        # nums = [i for i in range(1, n+1)]
        # for i in nums:
        #     result += 

print(Solution().generateTrees(3))