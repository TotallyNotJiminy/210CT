class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.totaldistances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, totaldistance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.totaldistances[(from_node, to_node)] = totaldistance

def dijsktra(graph, start):
  past = {start: 0}
  route = {}
  nodes = set(graph.nodes)
  while nodes: 
    smallest = None
    for node in nodes:
      if node in past:
        if smallest is None:
          smallest = node
        elif past[node]<past[smallest]:
          smallest = node
    if smallest==None:
      break
    nodes.remove(smallest)
    current_value = past[smallest]
    for edge in graph.edges[smallest]:
      value = current_value + graph.totaldistance[(smallest, edge)]
      if edge not in past or value < past[edge]:
        past[edge] = value
        route[edge] = smallest
  return past, route
