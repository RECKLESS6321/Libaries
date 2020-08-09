#Uses a dictionary as an adjacency list to store connected vertices.
#Connected vertex names are keys and the edge weights are values.
#Has methods to add edges and return a list of connected vertices.
#djndnd


class Vertex:
  def __init__(self, value):
    self.value = value
    self.edges = {}

  def add_edge(self, vertex, weight = 0):
    self.edges[vertex] = weight

  def get_edges(self):
    return self.edges.keys()

