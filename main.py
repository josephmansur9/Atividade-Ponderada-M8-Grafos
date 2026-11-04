import networkx as nx

ORIGEM = "S0"
DESTINO = "S7"

G = nx.Graph()
G.add_nodes_from(["S0", "S1", "S2", "S3", "S4", "S5", "S6", "S7"])
G.add_weighted_edges_from([
    ("S0", "S1", 14), ("S0", "S2", 19), ("S1", "S2", 9),  ("S1", "S3", 12),
    ("S2", "S4", 15), ("S2", "S5", 14), ("S3", "S4", 10), ("S3", "S6", 16),
    ("S4", "S5", 7),  ("S4", "S7", 17), ("S5", "S7", 24), ("S6", "S7", 13),
    ("S1", "S4", 20),
])

custo, rota = nx.single_source_dijkstra(G, ORIGEM, DESTINO, weight="weight")
dist = nx.single_source_dijkstra_path_length(G, ORIGEM, weight="weight")