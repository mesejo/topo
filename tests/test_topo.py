from .context import topo

import unittest


class QueueTest(unittest.TestCase):
    def test_no_priority(self):
        q = topo.Queue([1, 2, 3], priority=False)
        self.assertEqual(1, q.pop())

    def test_priority(self):
        pq = topo.Queue([2, 3, 1, 5, 4], priority=True)
        self.assertEqual(1, pq.pop())


class TopoTest(unittest.TestCase):
    def test_queue(self):
        g = {1: [2], 2: []}
        self.assertEqual([1, 2], topo.topo(set(g.keys()), g.get))

    def test_heap(self):
        g = {1: [2], 2: [], 3: [2]}
        self.assertEqual([1, 3, 2], topo.topo(set(g.keys()), g.get, key=lambda x: x))