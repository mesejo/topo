from topo import Queue, topo

q = Queue([1, 2, 3], priority=False)

assert q.pop() == 1
assert q.pop() == 2

pq = Queue([2, 3, 1, 5, 4], priority=True)

assert pq.pop() == 1
assert pq.pop() == 2
assert pq.pop() == 3

g = {1: [2], 2: []}

assert [1, 2] == topo(g.keys(), g.get)
