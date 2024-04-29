

from collections import defaultdict


# directed graph

class Graph:
    def __init__(self, size):
        self.adj_matrix = [[None] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size
    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight
    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data
    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(' '.join(map(lambda x: str(x) if x is not None else '0', row)))
        print("\nVertex Data:")
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")
g = Graph(4)
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_edge(0, 1, 3)
g.add_edge(0, 2, 2)
g.add_edge(3, 0, 4)
g.add_edge(2, 1, 1)
g.print_graph()


# indirected graph

def build_graph():
    edges = [
        ["A", "B"], ["A", "E"],
        ["A", "C"], ["B", "D"],
        ["B", "E"], ["C", "F"],
        ["C", "G"], ["D", "E"]
    ]
    graph = defaultdict(list)
    for edge in edges:
        a, b = edge[0], edge[1]
        graph[a].append(b)
        graph[b].append(a)
    return graph
if __name__ == "__main__":
    graph = build_graph()
    print(graph)


# Acyclic graph

class Graph:
    def __init__(self, size):
     self.adj_matrix = [[0] * size for _ in range(size)]
     self.size = size
     self.vertex_data = [''] * size
    def add_edge(self, u, v):
     if 0 <= u < self.size and 0 <= v < self.size:
      self.adj_matrix[u][v] = 1
    def add_vertex_data(self, vertex, data):
     if 0 <= vertex < self.size:
      self.vertex_data[vertex] = data
    def print_graph(self):
     print("Adjacency Matrix:")
     for row in self.adj_matrix:
      print(' '.join(map(str, row)))
     print("\nVertex Data:")
     for vertex, data in enumerate(self.vertex_data):
      print(f"Vertex {vertex}: {data}")
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.print_graph()


# a CYCLIC graph
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size
    def add_edge(self, u, v):
         if 0 <= u < self.size and 0 <= v < self.size:
          self.adj_matrix[u][v] = 1
          self.adj_matrix[v][u] = 1
    def add_vertex_data(self, vertex, data):
         if 0 <= vertex < self.size:
          self.vertex_data[vertex] = data
    def print_graph(self):
         print("Adjacency Matrix:")
         for row in self.adj_matrix:
            print(' '.join(map(str, row)))
         print("\nVertex Data:")
         for vertex, data in enumerate(self.vertex_data):
          print(f"Vertex {vertex}: {data}")
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 0)
g.print_graph()


# weighted graph

class graphWeighted:
     def __init__(self, size):
       self.adj_matrix = [[0] * size for _ in range(size)]
       self.size = size
       self.vertex_data = [''] * size
     def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
          self.adj_matrix[u][v] = weight
          self.adj_matrix[v][u] = weight
     def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
         self.vertex_data[vertex] = data
     def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
           print(' '.join(map(str, row)))
           print("\nVertex Data:")
        for vertex, data in enumerate(self.vertex_data):
         print(f"Vertex {vertex}: {data}")
g = graphWeighted(4)
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 3)
g.add_edge(0, 3, 7)
g.add_edge(1, 2, 2)
g.print_graph()