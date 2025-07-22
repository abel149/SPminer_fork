import networkx as nx
from networkx.algorithms import isomorphism
# Target graph (directed)
G = nx.DiGraph()
G.add_edges_from([(0, 1), (1, 2), (2, 0)])  # A cycle

# Query graph (directed)
Q = nx.DiGraph()
Q.add_edges_from([(0, 1), (1, 2)])

matcher = isomorphism.DiGraphMatcher(G, Q)
count = sum(1 for _ in matcher.subgraph_isomorphisms_iter())
print("Matches found:", count)
