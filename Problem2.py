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
        for i in range(0,self.V):
            self.graph[i].append(None)
        self.globalSum = 0
        self.globalList = []

    def addEdge(self, u, v, w):
        self.graph[u].append((v,w))

    def isCyclicUtil(self, v, visited, recStack, sum):

        visited[v] = True
        recStack[v] = True


        for neighbour in self.graph[v]:
            if neighbour is not None:
                if visited[neighbour[0]] == False:
                    if self.isCyclicUtil(neighbour[0], visited, recStack, sum+neighbour[1]) == True:
                        if self.globalSum < sum+neighbour[1]:
                            self.globalSum = sum+neighbour[1]
                            self.addVertextoList(visited, self.globalList)
                    return True
                elif recStack[neighbour[0]] == True:
                    if self.globalSum < sum+neighbour[1]:
                        self.globalSum = sum+neighbour[1]
                        self.addVertextoList(visited, self.globalList)
                    return True

            # The node needs to be poped from
            # recursion stack before function ends
            recStack[v] = False
            #TODO - remove
            #visited[v] = False
        return False

    # Returns true if graph is cyclic else false
    def isCyclic(self):
        visited = [False] * (self.V+1)
        recStack = [False] * (self.V+1)
        res = False
        for node in range(self.V):
            #if visited[node] == False:
            visited = [False] * (self.V+1)
            if self.isCyclicUtil(node, visited, recStack,0 ) == True:
                res = True
        return res

    def addVertextoList(self, stack, list):
        list.clear()
        for i in range(self.V+1):
            if stack[i] == True:
                list.append(i)

df = pd.read_csv("data_Problem2.csv", index_col=False)
df.dropna(inplace=True)
vertices = max(int(max(df['TO_NODE'])), int(max(df['FROM_NODE'])))
g = Graph(vertices)

for i in range (0, len(df['FROM_NODE'])):
    if df['FROM_NODE'][i] is not "nan" and df['FROM_NODE'][i] is not "nan" and df['FROM_NODE'][i] is not "nan":
        g.addEdge(int(df['FROM_NODE'][i]), int(df['TO_NODE'][i]), df['VALUE'][i])

if g.isCyclic() == 1:
    print("Graph has a cycle with maximum sum: ", g.globalSum, " and the cycle ", g.globalList)
else:
    print("Graph has no cycle")
 
