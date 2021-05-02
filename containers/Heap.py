from containers.BinaryTree import BinaryTree, Node


class Heap(BinaryTree):
    def __init__(self, xs=None):
        super().__init__()
        if xs:
            self.insert_list(xs)

    def __repr__(self):
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def is_heap_satisfied(self):
        if self.root:
            return Heap._is_heap_satisfied(self.root)
        return True

    @staticmethod
    def _is_heap_satisfied(node):
        left = True
        right = True
        if node is None:
            return True

        x_left = Heap._is_heap_satisfied(node.left)
        y_right = Heap._is_heap_satisfied(node.right)

        if node.left:
            left = node.value <= node.left.value and x_left
        if node.right:
            right = node.value <= node.right.value and y_right

        return left and right

    def insert(self, value):
        '''
        Inserts value into the heap.
        '''
        if self.root is None:
            self.root = Node(value)
            self.root.descendents = 1
        else:
            self.root = Heap._insert(self.root, value)

    @staticmethod
    def _insert(node, value):
        if node is None:
            return

        if node.left and node.right:
            node.left = Heap._insert(node.left, value)
            if node.value > node.left.value:
                return Heap._move_up(node, value)

        if node.left is None:
            node.left = Node(value)
            if node.value > node.left.value:
                return Heap._move_up(node, value)

        elif node.right is None:
            node.right = Node(value)
            if node.value > node.right.value:
                return Heap._move_up(node, value)

        return node

    @staticmethod
    def _move_up(node, value):
        if Heap._is_heap_satisfied(node) is True:
            return node
        if node.left and node.left.value > node.value:
            node.left = Heap._move_up(node.left, value)
        if node.right and node.right.value > node.value:
            node.right = Heap._move_up(node.right, value)

        if node.right:
            if node.right.value == value:
                parent_new = node.right.value
                right_new = node.value
                node.value = parent_new
                node.right.value = right_new

        if node.left:
            if node.left.value == value:
                parent_new = node.left.value
                left_new = node.value
                node.value = parent_new
                node.left.value = left_new

        return node

    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.
        '''
        for x in xs:
            self.insert(x)

    def find_smallest(self):
        if self.root:
            return Heap._find_smallest(self.root)

    @staticmethod
    def _find_smallest(node):
        return node.value

    def remove_min(self):
        if self.root is None:
            return None
        elif self.root.left is None and self.root.right is None:
            self.root = None
        else:
            right_replace = Heap._find_right(self.root)
            self.root = Heap._remove(self.root)
            if right_replace == self.root.value:
                return
            else:
                self.root.value = right_replace
            if Heap._is_heap_satisfied(self.root) is False:
                return Heap._move_down(self.root)

    @staticmethod
    def _find_right(node):
        if node.left is None and node.right is None:
            return node.value
        elif node.right:
            return Heap._find_right(node.right)
        elif node.left:
            return Heap._find_right(node.left)

    @staticmethod
    def _remove(node):
        if node is None:
            return
        elif node.right:
            node.right = Heap._remove(node.right)
        elif node.left:
            node.left = Heap._remove(node.left)
        else:
            if node.right is None and node.left is None:
                return None
        return node

    @staticmethod
    def _move_down(node):
        if node.left is None and node.right is None:
            return node

        a = node.right is None
        y = node.left is None

        if node.left and (a or node.left.value <= node.right.value):
            if node.left.value < node.value:
                parent_new = node.left.value
                left_new = node.value

                node.value = parent_new
                node.left.value = left_new

            node.left = Heap._move_down(node.left)

        elif node.right and (y or node.right.value <= node.left.value):
            if node.right.value < node.value:
                parent_new = node.right.value
                right_new = node.value

                node.value = parent_new
                node.right.value = right_new

            node.right = Heap._move_down(node.right)

        return node
