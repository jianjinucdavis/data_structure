import unittest
import linked_list
import warnings


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.empty_list = linked_list.LinkedList()
        self.list = linked_list.LinkedList()
        self.list.head = linked_list.Node(5)

    def test_empty(self):
        self.assertEqual(self.empty_list.empty(), True)

    def test_push_front(self):
        self.empty_list.push_front(5)
        self.assertEqual(self.empty_list.head.data, 5)

    def test_top_front(self):
        self.assertEqual(self.list.top_front(), 5)

    def test_pop_front(self):
        self.list.pop_front()
        self.assertEqual(True, self.list.empty())
        # self.assertWarns(warnings.warn("Empty List"), self.empty_list.pop_front())


if __name__ == '__main__':
    unittest.main()