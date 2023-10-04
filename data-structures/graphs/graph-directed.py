class Node():
    def __init__(self, value, neighbors=None):
        self.value = value
        if neighbors:
            self.neighbors = neighbors
        else:
            self.neighbors = []

    def add_neighbor(self, value):
        self.neighbors.append(value)

    def neighbor_count(self):
        return len(self.neighbors)

    def has_neighbors(self):
        return self.neighbors > 0

class GraphDirected():
    def __init__(self, nodes=None):
        if nodes:
            self.nodes = nodes
        else:
            self.nodes = []

    def add_node(self, value):
        new_node = Node(value)

        self.nodes.append(new_node)

    def find_node(self, value):
        for node in self.nodes:
            if node.value == value:
                return node

        return None

    def add_edge(self, value1, value2, weight=1):
        node1 = self.find_node(value1)
        node2 = self.find_node(value2)

        if node1 and node2:
            node1.add_neighbor((value2, weight))

    def is_neighbor(self, value1, value2):
        node1 = self.find_node(value1)
        node2 = self.find_node(value2)

        if node1 and node2:
            for (value, weight) in node1.neighbors:
                if value == value2:
                    return True

        return False


    def get_node_count(self):
        return len(self.nodes)

    def get_edge_count(self):
        edge_count = 0

        for node in self.nodes:
            edge_count += len(node.neighbors)

        return edge_count

    def __repr__(self):
        return f'{[(node.value, node.neighbors) for node in self.nodes]}'


sample_directed_graph = GraphDirected()
print(sample_directed_graph)

sample_directed_graph.add_node(11)
sample_directed_graph.add_node(21)
sample_directed_graph.add_node(31)
sample_directed_graph.add_node(41)
sample_directed_graph.add_node(51)
sample_directed_graph.add_node(61)
sample_directed_graph.add_node(71)
sample_directed_graph.add_node(81)

print(sample_directed_graph.find_node(1))

sample_directed_graph.add_edge(31, 81, 5)
sample_directed_graph.add_edge(31, 61, 3)
sample_directed_graph.add_edge(11, 31, 6)
sample_directed_graph.add_edge(11, 21, 2)

print(sample_directed_graph.is_neighbor(11, 21))
print(sample_directed_graph.is_neighbor(11, 71))

print(sample_directed_graph)

print(sample_directed_graph.get_edge_count())
