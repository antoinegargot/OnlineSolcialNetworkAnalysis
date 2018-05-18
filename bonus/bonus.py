import networkx as nx

def jaccard_wt(graph, node):
    """
    The weighted jaccard score, defined in bonus.md.
    Args:
      graph....a networkx graph
      node.....a node to score potential new edges for.
    Returns:
      A list of ((node, ni), score) tuples, representing the 
                score assigned to edge (node, ni)
                (note the edge order)
    """
    candidates = list()
    for candidate in graph.nodes():
        if candidate not in graph.neighbors(node) and candidate != node:
            num = 0
            den1 = 0
            den2 = 0
            for n in graph.neighbors(candidate):
                den1 += 1 / graph.degree(n)
                if n in graph.neighbors(node):
                    num += 1 / graph.degree(n)
            for n in graph.neighbors(node):
                den1 += 1 / graph.degree(n)
            candidates.append(((node, candidate), num / (den1 + den2)))
    return candidates