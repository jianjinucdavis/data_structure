import warnings


''' todo:
- with tail
- doubly linked list
- algorithm practice
-- learn python function overload
'''


# node has data and next
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# a list of nodes
# head
'''API
x push_front(key)        add to front
x key top_front()        return front item
x pop_front()            remove front item
x push_back(key)         add to back
x top_back()             return back item
x pop_back()             remove back item
x boolean find(key)      is key in list
x Erase(key)             remove key from list
x boolean empty()        is list empty?
x add_before(node, key)  add key before node
'''


class LinkedList:
    def __init__(self):
        self.head = None

    def empty(self) -> bool:
        return self.head is None

    def push_front(self, node: Node) -> None:
        if not isinstance(node, Node):
            print(f"instantiating Node({node})")
            node = Node(node)
        if self.empty():
            self.head = node
        else:
            p = self.head
            self.head = node
            node.next = p

    def top_front(self):
        return self.head.data

    def pop_front(self):
        # move head to next next
        if not self.empty():
            p = self.head
            if p.next:
                self.head = p.next
            else:
                self.head = None
            # delete
            del p
        else:
            warnings.warn("Empty List")

    def push_back(self, node: Node):
        if not isinstance(node, Node):
            print(f"instantiating Node({node})")
            node = Node(node)
        if self.empty():
            self.push_front(node)
        else:
            # go to the last node end
            p = self.head
            while p.next:
                p = p.next
            p.next = node

    def return_back(self):
        if self.empty():
            return None
        else:
            p = self.head
            while p.next:
                p = p.next
            return p.data

    def pop_back(self):
        if not self.empty():
            p = self.head
            if not p.next:
                self.head = None
                del p
            else:
                lst = p.next
                while lst.next:
                    print(p.data)
                    p = p.next
                    lst = lst.next
                p.next = None
                del lst

    def find(self, key) -> bool:  # O(N)
        # if node in list, return True
        # else return False
        if not self.empty():
            p = self.head
            if p.data == key:
                return True
            while p.next:
                p = p.next
                if p.data == key:
                    return True
        return False

    def erase(self, key):
        if not self.empty():
            p = self.head
            # if erase first node
            if p.data == key:
                if p.next:
                    self.head = p.next
                    del p
                    return None
                else:
                    del p
                    self.head = None
                    return None
            # if erase second or later node: find node,
            while p.next:
                node1 = p
                node2 = p.next
                if node2.data == key:
                    # if node 2 is not the last node
                    # node1.next points to node2's next
                    # delete node2
                    if node2.next:
                        node1.next = node2.next
                        del node2
                        return None
                    # if node2 is the last node
                    else:
                        del node2
                        node1.next = None
                        return None

    def add_before(self, node, key):
        # add node before key
        if not isinstance(node, Node):
            print(f"instantiating Node({node})")
            node = Node(node)
        node1 = self.head
        if node1.data == key:
            self.head = node
            node.next = node1
        else:
            node2 = node1.next
            while node2.data != key:
                node1 = node1.next
                node2 = node2.next
            node1.next = node
            node.next = node2

    def print(self):
        if not self.empty():
            p = self.head  # first node
            nodes = [p.data]
            while p.next:  # while it's not the last node
                p = p.next
                nodes.append(p.data)
            print('-->'.join([str(i) for i in nodes]))
        else:
            print("List is empty")


class LinkedListTail(LinkedList):
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, node: Node) -> None:
        if not isinstance(node, Node):
            print(f"instantiating Node({node})")
            node = Node(node)
        if self.empty():
            self.head = node
            self.tail = node
        else:
            p = self.head
            self.head = node
            node.next = p

    def pop_front(self):
        # move head to next next
        if not self.empty():
            p = self.head
            if p.next:
                self.head = p.next
            else:
                self.head = None
                self.tail = None
            # delete
            del p
        else:
            warnings.warn("Empty List")

    def push_back(self, node: Node):
        if not isinstance(node, Node):
            print(f"instantiating Node({node})")
            node = Node(node)
        if self.empty():
            self.push_front(node)
        else:
            p = self.tail
            p.next = node
            self.tail = node

    def return_back(self):
        if self.empty():
            return None
        else:
            return self.tail

    def pop_back(self):
        if not self.empty():
            p = self.head
            if not p.next:
                self.head = None
                self.tail = None
                del p
            else:
                lst = p.next
                while lst.next:
                    print(p.data)
                    p = p.next
                    lst = lst.next
                p.next = None
                self.tail = p
                del lst

    def find(self, key) -> bool:  # O(N)
        # if node in list, return True
        # else return False
        if not self.empty():
            p = self.head
            if p.data == key:
                return True
            if self.tail.data == key:
                return True
            while p.next:
                p = p.next
                if p.data == key:
                    return True
        return False

    def erase(self, key):
        if not self.empty():
            p = self.head
            # if erase first node
            if p.data == key:
                if p.next:
                    self.head = p.next
                    del p
                    return None
                else:
                    del p
                    self.head = None
                    self.tail = None
                    return None
            # if erase second or later node: find node,
            while p.next:
                node1 = p
                node2 = p.next
                if node2.data == key:
                    # if node 2 is not the last node
                    # node1.next points to node2's next
                    # delete node2
                    if node2.next:
                        node1.next = node2.next
                        del node2
                        return None
                    # if node2 is the last node
                    else:
                        del node2
                        self.tail = node1
                        node1.next = None
                        return None
