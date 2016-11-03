# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 15:57:11 2016

@author: kiawo
"""

graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }

def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges
print(generate_edges(graph))


def find_isolated_nodes(graph):
    """ returns a list of isolated nodes. """
    isolated = []
    for node in graph:
        if not graph[node] :
            isolated += node
    return isolated

find_isolated_nodes(graph)