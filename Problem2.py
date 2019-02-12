#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 16:51:11 2019

@author: skondaveeti
"""

from collections import defaultdict
import pandas as pd


class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
        self.globalSum = 0

    def addEdge(self, u, v, w):
        self.graph[u].append((v,w))

    def isCyclicUtil(self, v, visited, recStack, sum):

        # Mark current node as visited and
        # adds to recursion stack
        visited[v] = True
        recStack[v] = True

        # Recur for all neighbours
        # if any neighbour is visited and in
        # recStack then graph is cyclic
        for neighbour in self.graph[v]:
            if visited[neighbour[0]] == False:
                if self.isCyclicUtil(neighbour[0], visited, recStack, sum+neighbour[1]) == True:
                    if self.globalSum < sum+neighbour[1]:
                        self.globalSum = sum++neighbour[1]
                return True
            elif recStack[neighbour[0]] == True:
                if self.globalSum < sum+neighbour[1]:
                    self.globalSum = sum+neighbour[1]
                return True

        # The node needs to be poped from
        # recursion stack before function ends
        recStack[v] = False
        #TODO - remove
        #visited[v] = False
        return False

    # Returns true if graph is cyclic else false
    def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        res = False
        for node in range(self.V):
            #if visited[node] == False:
            visited = [False] * self.V
            if self.isCyclicUtil(node, visited, recStack,0 ) == True:
                res = True
        return res

df = pd.read_csv("data_Problem2.csv", index_col=False)
df.dropna(inplace=True)
vertices = int(max(df['TO_NODE']))
g = Graph(len(df['FROM_NODE'].unique()))

for i in range (0, len(df['FROM_NODE'])):
    g.addEdge(df['FROM_NODE'][i], df['TO_NODE'][i], df['VALUE'][i])