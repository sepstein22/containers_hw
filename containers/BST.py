'''
This file implements the Binary Search Tree data structure.
'''

from containers.BinaryTree import BinaryTree, Node


class BST(BinaryTree):
    '''
    The BST is a superclass of BinaryTree.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        If xs is a list (i.e. xs is not None),
        then each element of xs needs to be inserted into the BST.
        '''
        super().__init__()
        if xs is not None:
            for x in xs:
                self.insert(x)

    def __repr__(self):
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def __eq__(self, t2):
        '''
        This method checks to see if the contents of self and t2 are equal.
        The expression `a == b` desugars to `a.__eq__(b)`.
        NOTE:
        We only care about "semantic" equality,
        and not "syntactic" equality.
        That is, we do not care about the tree structure itself,
        and only care about the contents of what the tree contains.
        HINT:
        Convert the contents of both trees into a sorted list,
        then compare those sorted lists for equality.
        '''
        list_1 = self.to_list('inorder')
        list_2 = t2.to_list('inorder')
        for x in list_1:
            if x not in list_2:
                return False
        for x in list_2:
            if x not in list_1:
                return False
        return True

    def is_bst_satisfied(self):
        '''
        Whenever you implement a data structure,
        the first thing to do is to implement a function that checks whether
        the structure obeys all of its laws.
        '''
        if self.root:
            return BST._is_bst_satisfied(self.root)
        return True

    @staticmethod
    def _is_bst_satisfied(node):
        ret = True
        if node.left:
            if node.value >= BST._find_largest(node.left):
                ret &= BST._is_bst_satisfied(node.left)
            else:
                ret = False
        if node.right:
            if node.value <= BST._find_smallest(node.right):
                ret &= BST._is_bst_satisfied(node.right)
            else:
                ret = False
        return ret

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    @staticmethod
    def _insert(value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                BST._insert(value, node.left)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                BST._insert(value, node.right)
        else:
            print("value is already present in tree")

    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.
        '''
        for i in xs:
            self.insert(i)

    def __contains__(self, value):
        '''
        Recall that `x in tree` desugars to `tree.__contains__(x)`.
        '''
        return self.find(value)

    def find(self, value):
        '''
        Returns whether value is contained in the BST.
        FIXME:
        Implement this function.
        '''
        if self.root:
            if BST._find(value, self.root):
                return True
        else:
            return False

    @staticmethod
    def _find(value, node):
        '''
        FIXME:
        Implement this function.
        '''
        if value > node.value and node.right:
            return BST._find(value, node.right)
        elif value < node.value and node.left:
            return BST._find(value, node.left)
        if value == node.value:
            return True

    def find_smallest(self):
        '''
        Returns the smallest value in the tree.
        '''
        if self.root is None:
            raise ValueError('DNE in the Tree')
        else:
            return BST._find_smallest(self.root)

    @staticmethod
    def _find_smallest(node):
        assert node is not None
        if node.left is None:
            return node.value
        else:
            return BST._find_smallest(node.left)

    def find_largest(self):
        '''
        Returns the largest value in the tree.
        '''
        if self.root is None:
            raise ValueError('Nothing in the tree')
        else:
            return BST._find_largest(self.root)

    @staticmethod
    def _find_largest(node):
        assert node is not None
        if node.right is None:
            return node.value
        else:
            return BST._find_largest(node.right)

    def remove(self, value):
        '''
        Removes value from the BST.
        If value is not in the BST, it does nothing.
        '''
        if not self.root:
            return self.root
        else:
            self.root = BST._remove(self.root, value)

    @staticmethod
    def _remove(node, value):
        if not node:
            return node

        if node.value > value:
            node.left = BST._remove(node.left, value)

        elif node.value < value:
            node.right = BST._remove(node.right, value)

        else:
            if not node.right:
                return node.left

            if not node.left:
                return node.right

            temp_code = node.right

            while temp_code.left:
                temp_code = temp_code.left

            node.value = temp_code.value
            node.right = BST._remove(node.right, node.value)

        return node

    def remove_list(self, xs):
        '''
        Given a list xs, remove each element of xs from self.
        '''
        for elements in xs:
            self.remove(elements)
