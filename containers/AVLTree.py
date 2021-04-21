'''
This file implements the AVL Tree data structure.
'''

from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in the class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        self.root = None
        if xs:
            self.insert_list(xs)

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        '''
        Returns True if the avl tree satisfies that all nodes
        have a balance factor in [-1,0,1].
        '''
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        Implement this function.
        '''
        if node is None:
            return True
        left = AVLTree._is_avl_satisfied(node.left)
        right = AVLTree._is_avl_satisfied(node.right)
        return AVLTree._balanced_factor(node) in [-1, 0, 1] and left and right

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        '''
        if node.right is None or node is None:
            return node

        newnode = Node(node.right.value)
        newnode.right = node.right.right

        newleft = Node(node.value)
        newleft.left = node.left
        newleft.right = node.right.left

        newnode.left = newleft

        return newnode

    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.
        '''
        if node.left is None or node is None:
            return node

        newnode = Node(node.left.value)
        newnode.left = node.left.left

        newright = Node(node.value)
        newright.right = node.right
        newnode.left = node.left.right

        newnode.right = newright

        return newnode

    def insert(self, value):
        '''
        FIXME:
        Implement this function.

        HINT:
        It is okay to add @staticmethod helper functions for this code.
        The code should look very similar to the code for your insert
        function for the BST,
        but it will also call the left and right rebalancing functions.
        '''
        if not self.root:
            self.root = Node(value)
            return
        if value == self.root.value:
            return
        else:
            self._insert(value, self.root)
            if not self.is_avl_satisfied():
                self.root = self.rebalance(self.root)
                if not self.is_avl_satisfied():
                    self.root = self.rebalance(self.root)
            return

    @staticmethod
    def _insert(value, node):
        if node.value == value:
            return
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
                return
            else:
                return AVLTree._insert(value, node.left)
        else:
            if node.right is None:
                node.right = Node(value)
                return
            else:
                return AVLTree._insert(value, node.right)

    def rebalanced(self, start):
        if start is None:
            return
        if self._balance_factor(start) in [-2, 2]:
            start = self._rebalance(start)
        else:
            start.left = self.rebalance(start.left)
            start.right = self.rebalance(start.right)
        return start

    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''
        if node is None:
            return
        balance = AVLTree._balance_factor(node)
        if balance < 0:
            if AVLTree._balance_factor(node.right) > 0:
                node.right = AVLTree._right_rotate(node.right)
                node = AVLTree._left_rotate(node)
            else:
                node = AVLTree._left_rotate(node)
            return node
        elif balance > 0:
            if AVLTree._balance_factor(node.left) < 0:
                node.left = AVLTree._left_rotate(node.left)
                node = AVLTree._right_rotate(node)
            else:
                node = AVLTree._right_rotate(node)
            return node
