import unittest
import linked_list
import warnings


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.empty_list = linked_list.LinkedList()
        self.list = linked_list.LinkedList()
        self.list.head = linked_list.Node(5)
        self.list2 = linked_list.LinkedList()
        self.list2.head = linked_list.Node(100)
        self.list2.head.next = linked_list.Node(1000)

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

    def test_push_back(self):
        self.list.push_back(3)
        self.assertEqual(3, self.list.head.next.data)
        self.empty_list.push_back(10)
        self.assertEqual(10, self.empty_list.head.data)

    def test_return_back(self):
        self.assertIsNone(self.empty_list.return_back())
        self.assertEqual(5, self.list.return_back())
        self.list.push_back(14)
        self.assertEqual(14, self.list.return_back())

    def test_pop_back(self):
        self.list.pop_back()
        self.assertTrue(self.list.empty())
        self.list2.pop_back()
        self.assertEqual(100, self.list2.head.data)

    def test_find(self):
        self.assertTrue(self.list.find(5))
        self.assertFalse(self.list.find(3))
        self.assertTrue(self.list2.find(100))

    def test_erase(self):
        self.list2.erase(100)
        self.assertEqual(self.list2.head.data, 1000)
        self.list.erase(5)
        self.assertTrue(self.list.empty())

    def test_add_before(self):
        self.list2.add_before(13, 1000)
        self.assertEqual(13, self.list2.head.next.data)


if __name__ == '__main__':
    unittest.main()