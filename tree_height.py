# read this: https://www.geeksforgeeks.org/generic-tree-level-order-traversal/
# recursion!!!


class Node:
    def __init__(self, num: int):
        self.key = num
        self.children = []
        self.root = False

    def add_child(self, child):
        self.children.append(child)

    def is_root(self):
        self.root = True

    def __eq__(self, other):
        return self.key == other


def build_tree(n, seq):
    nodes = [Node(i) for i in range(n)]
    for child, parent in enumerate(seq):
        if parent != -1:
            nodes[parent].add_child(nodes[child])
        else:
            nodes[child].is_root()
            root = child
    return nodes[root]


def height(node, h=0):
    if node is None:
        return h
    h += 1
    hs = []
    for child in node.children:
        hs.append(height(child, h))
    return max(hs) if hs else h


def compute_height(n, seq):
    root_node = build_tree(n, seq)
    return height(root_node)


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))

'''
seq = [8, 8, 5, 6, 7, 3, 1, 6, -1, 5]
n = len(seq)
print(compute_height(n, seq))
assert compute_height(n, seq) == 6
'''

seq = [-1, 0, 4, 0, 3]
n = len(seq)
print(compute_height(n, seq))
assert compute_height(n, seq) == 4

