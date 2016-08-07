import pydot
import copy
import string

from collections import Counter
from random import sample, randint
from pprint import pprint


LETTERS = string.ascii_lowercase
PREDS_COUNT = 20
VARS_RANGE = 3, 7


def generate_predicates(count):
    for i in range(1, count + 1):
        yield sample(LETTERS, randint(*VARS_RANGE))

# predicates_list = list(generate_predicates(PREDS_COUNT))
predicates_list = [
    ['e', 'm', 'q', 'd'],
    ['y', 'x', 'l', 'e'],
    ['m', 'o', 'n', 'k', 'r', 'x'],
    ['h', 'j', 'k', 't', 's'],
    ['k', 'v', 'p', 'x', 'z'],
    ['b', 'n', 'z'],
    ['n', 'u', 'y'],
    ['y', 'n', 'f', 'e'],
    ['e', 't', 'n', 'v', 'i', 's', 'k'],
    ['u', 'e', 't', 'h', 'n', 'i', 'd']
]

# predicates_list = [
#     ['a', 'b', 'c', 'd', 'e'],
#     ['a', 'b', 'c', 'd'],
#     ['a', 'b', 'c'],
#     ['a', 'b'],
#     ['a'],
# ]


pprint(predicates_list)


class Node(object):
    def __init__(self, predicates, group='', cost=0, parent=None):
        self.predicates = predicates

        self.group = group
        self.cost = cost

        self.down = None  # link to down node
        self.right = None  # link to right node
        self.parent = parent  # link to parent node
        self.decision_list = []  # link to decisions node

        self.groups = self.get_groups()

        if not group:
            for freq, group in self.head_groups():
                self.make_decision(group)

    def get_groups(self):
        c = Counter(sum(self.predicates, []))
        return sorted([(f, p) for p, f in c.items() if f > 1], reverse=True)

    def groups_title(self):
        return ' '.join('%s:%s' % (f, p) for f, p in self.get_groups())

    def get_path(self):
        node = self
        path = []

        while node:
            if node.group:
                path.append(node.group)
            node = node.parent

        return path

    def head_groups(self):
        result = []

        if self.groups:
            head_freq, _ = self.groups[0]

            for freq, group in self.groups:
                if freq == head_freq:
                    result.append((freq, group))

        return result

    def make_decision(self, group):
        down = []
        right = []
        decision = []
        add = 0

        for pred in self.predicates:
            pred_copy = copy.copy(pred)

            try:
                pred_copy.remove(group)
                right.insert(0, pred_copy)
                decision.insert(0, [group] + pred_copy)

                add += 1
            except ValueError:
                down.append(pred_copy)
                decision.append(pred_copy)

        if add > 1:
            node = Node(decision, group, self.cost + add, parent=self)
            node.right = Node(right, '', self.cost + add, parent=node)
            node.down = Node(down, '', self.cost + add, parent=node)

            self.decision_list.append(node)

    def format_predicates(self):
        return '\n'.join(''.join(p) for p in self.predicates)

    def graph_node(self):
        name = '%s %s\n%s' % (
            self.cost,
            '.'.join(reversed(self.get_path())),
            self.format_predicates(),
        )

        if not self.group:
            return pydot.Node(name, fillcolor='gray')

        return pydot.Node(name)

    def build_graph(self, graph):
        if self.parent:
            parent = self.graph_node()
        else:
            parent = pydot.Node('root')

        for decision in self.decision_list:
            graph.add_edge(pydot.Edge(parent, decision.graph_node(), label='decision: %s' % decision.group))
            decision.build_graph(graph)

        if self.down:
            graph.add_edge(pydot.Edge(parent, self.down.graph_node(), label='down'))
            self.down.build_graph(graph)

        if self.right:
            graph.add_edge(pydot.Edge(parent, self.right.graph_node(), label='right'))
            self.right.build_graph(graph)


root = Node(predicates_list)
graph = pydot.Dot(graph_type='digraph', label=str(root.groups_title()))

root.build_graph(graph)
graph.write_png('graph.png')
print(root)



