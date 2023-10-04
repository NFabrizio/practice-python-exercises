class Node():
    def __init__(self, value, neighbors=None):
        self.value = value
        if not neighbors:
            self.neighbors = []
        else:
            self.neighbors = neighbors

    # Method that returns whether the Node has neighbors
    def has_neighbors(self):
        return len(self.neighbors) > 0

    # Method that returns the number of neighbors for the Node
    def neighbor_count(self):
        return len(self.neighbors)

    # Method that adds a neighbor to the Node
    def add_neighbor(self, neighbor_node):
        self.neighbors.append(neighbor_node)

class GraphUndirected():
    # Initialization method
    def __init__(self, nodes=None):
        if not nodes:
            self.nodes = []
        else:
            self.nodes = nodes

    # Method to add a node
    def add_node(self, value):
        new_node = Node(value)
        self.nodes.append(new_node)

    # Method to find a node
    def find_node(self, value):
        for node in self.nodes:
            if node.value == value:
                return node

        return None

    # Method to add an edge
    def add_edge(self, value1, value2, weight=1):
        node1 = self.find_node(value1)
        node2 = self.find_node(value2)

        if node1 and node2:
            node1.add_neighbor((value2, weight))
            node2.add_neighbor((value1, weight))
        else:
            return 'Edges can only be added between nodes that exist in the graph'

    # Method that returns the number of nodes
    def get_node_count(self):
        return len(self.nodes)

    # Method that returns the number of edges
    def get_edge_count(self):
        edge_count = 0

        for node in self.nodes:
            edge_count += len(node.neighbors)

        return int(edge_count / 2)

    # Method that returns whether two nodes are connected
    def are_connected(self, value1, value2):
        node1 = self.find_node(value1)
        node2 = self.find_node(value2)

        if node1 and node2:
            for (value, weight) in node1.neighbors:
                if value2 == value:
                    return True

        return False

    # Print graph representation
    def __repr__(self):
        return f"{[(node.value, node.neighbors) for node in self.nodes]}"


sample_graph = GraphUndirected()
print(f'Initial node count: {sample_graph.get_node_count()}')
print(f'Initial edge count: {sample_graph.get_edge_count()}')

sample_graph.add_node(1)
sample_graph.add_node(3)
sample_graph.add_node(5)
sample_graph.add_node(7)
sample_graph.add_node(2)
sample_graph.add_node(4)
sample_graph.add_node(6)

print(sample_graph)
print(f'Node 7: {sample_graph.find_node(7)}')
print(f'Node 9: {sample_graph.find_node(9)}')

sample_graph.add_edge(1, 7)
sample_graph.add_edge(1, 5)
sample_graph.add_edge(1, 9)
print(sample_graph)

print(sample_graph.are_connected(1, 2))
print(sample_graph.are_connected(1, 5))
print(sample_graph.are_connected(1, 9))

print(f'Final node count: {sample_graph.get_node_count()}')
print(f'Final edge count: {sample_graph.get_edge_count()}')
