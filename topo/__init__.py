import heapq
from collections import deque
from functools import partial


class Queue:
    def __init__(self, data, priority=False):

        if priority:
            self._structure = data[:]
            heapq.heapify(self._structure)
            self.pop = partial(heapq.heappop, self._structure)
            self.push = partial(heapq.heappush, self._structure)
        else:
            self._structure = deque(data)
            self.pop = self._structure.popleft
            self.push = self._structure.append

    def __bool__(self):
        return bool(self._structure)


def topo(nodes: set, neighbors, key=None, reverse=False):
    """
    Return a list of nodes in topological sort order.

    A topological sort is a non-unique permutation of the nodes such that an edge from u to v implies that u appears
    before v in the topological sort order.

    :param nodes: set, labels of nodes
    :param neighbors: function, a function of one argument that is used to get the neighbors o a node
    :param key: function, optional specifies a function of one argument that is used to extract a comparison key
    :param reverse: bool, optional
    :return:
    """

    in_degree = {node: 0 for node in nodes}

    for node in nodes:
        for neighbor in neighbors(node):
            in_degree[neighbor] += 1

    priority = key is not None
    if not priority:
        key = lambda x: 1

    seeds = (node for node, degree in in_degree.items() if degree == 0)
    queue = Queue([(key(seed), seed) for seed in seeds], priority=priority)

    order = []
    while queue:
        _, node = queue.pop()
        order.append(node)
        for neighbor in neighbors(node):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.push((key(neighbor), neighbor))

    if reverse:
        return list(reversed(order))

    return order
