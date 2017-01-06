# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 12:44:20 2017

@author: kiawo
"""

"""
Create an G{n,m} random graph with n nodes and m edges
and report some properties.

This graph is sometimes called the Erd##[m~Qs-Rényi graph
but is different from G{n,p} or binomial_graph which is also
sometimes called the Erd##[m~Qs-Rényi graph.
"""
__author__ = """Aric Hagberg (hagberg@lanl.gov)"""
__credits__ = """"""
#    Copyright (C) 2004-2006 by 
#    Aric Hagberg 
#    Dan Schult 
#    Pieter Swart 
#    Distributed under the terms of the GNU Lesser General Public License
#    http://www.gnu.org/copyleft/lesser.html

import networkx
import sys

n=10 # 10 nodes
m=20 # 20 edges

G=networkx.gnm_random_graph(n,m)

# some properties
print ("node degree clustering")
for v in networkx.nodes(G):
    print (v,networkx.degree(G,v),networkx.clustering(G,v))

# print the adjacency list to terminal 
networkx.write_adjlist(G,sys.stdout)