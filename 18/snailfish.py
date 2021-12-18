import ast, os, copy
from functools import reduce
from itertools import permutations


class Node:
    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None
        self.value = None

    def add(self, tree):
        new_root = Node()
        new_root.left = self
        new_root.right = tree
        self.parent = new_root
        tree.parent = new_root
        self = new_root
        return self

    # def reduce_number(self):
    #     while True:

    def is_node(self):
        return self.value is None

    def is_value(self):
        return self.value is not None

    def __str__(self):
        if self.is_value():
            return str(self.value)
        return "[" + self.left.__str__() + "," + self.right.__str__() + "]"

    def magnitude(self):
        if self.is_value():
            return self.value
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()


def get_leftmost_value(node):
    if node is not None and node.is_value():
        return node
    return get_leftmost_value(node.left)


def get_rightmost_value(node):
    if node is not None and node.is_value():
        return node
    return get_rightmost_value(node.right)


def propagate_left(node, value):
    # print(f"Propagating {value} left from {node}")
    parent = node.parent
    if parent is None:
        return
    if parent.left == node:
        #TODO verify this
        propagate_left(parent, value)
    if parent.right == node:
        value_node = get_rightmost_value(parent.left)
        value_node.value += value


def propagate_right(node, value):
    # print(f"Propagating {value} right from {node}")
    parent = node.parent
    if parent is None:
        return
    if parent.right == node:
        #TODO verify this
        propagate_right(parent, value)
    if parent.left == node:
        value_node = get_leftmost_value(parent.right)
        value_node.value += value


def explode(node, depth=0):
    l, r = node.left, node.right
    parent = node.parent
    exploded = False
    if depth >= 4 and l.is_value() and r.is_value():
        new_node = Node()
        exploded = True
        new_node.value = 0
        if parent is not None:
            new_node.parent = parent
            if parent.left == node:
                parent.left = new_node
            elif parent.right == node:
                parent.right = new_node
            propagate_left(new_node, l.value)
            # in txt example last 7 is nott propagated to rightmost elem [1,1]
            propagate_right(new_node, r.value)
        node = new_node
    if l.is_node():
        exploded, _ = explode(l, depth + 1)
        if exploded:
            return True, node
    if r.is_node():
        exploded, _ = explode(r, depth + 1)
    return exploded, node


def split(node):
    if node.is_value():
        if node.value >= 10:
            left_node = Node()
            left_node.parent = node
            right_node = Node()
            right_node.parent = node
            left_node.value = node.value // 2
            right_node.value = node.value // 2 + node.value % 2
            node.value = None
            node.left = left_node
            node.right = right_node
            return True
        return False
    l, r = node.left, node.right
    l_split = split(l)
    if l_split:
        return True
    r_split = split(r)
    return r_split


def reduce_tree(node):
    while True:
        exploded, _ = explode(node, 0)
        if exploded:
            # print("After explode", node)
            continue
        did_split = split(node)
        # if did_split:
        # print("After split", node)
        if not did_split and not exploded:
            return node


def build_tree(number, parent):
    if isinstance(number, list):
        root = Node()
        root.parent = parent
        root.left = build_tree(number[0], root)
        root.right = build_tree(number[1], root)
        return root
    leaf = Node()
    leaf.parent = parent
    leaf.value = number
    return leaf


def add_and_reduce(n1, n2):
    n1_copy = copy.deepcopy(n1)
    n2_copy = copy.deepcopy(n2)
    added = n1_copy.add(n2_copy)
    return reduce_tree(added)


with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input:
    numbers = [
        build_tree(ast.literal_eval(line.strip()), None)
        for line in input.readlines()
    ]
    res = reduce(lambda x, y: add_and_reduce(x, y), numbers)
    print(res.magnitude())

    magnitudes = [
        add_and_reduce(x, y).magnitude() for x, y in permutations(numbers, 2)
    ]
    print(max(magnitudes))
    # print(magnitudes)
