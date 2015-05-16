__author__ = 'sriganesh'

import networkx as nx
import random

def extract(filename):
    f = open(filename,'r')
    G = nx.Graph()
    nodes = {}
    num = 1
    for line in f:
        line = line.split()
        u, v = line[0], line[1]
        if u not in nodes:
            nodes[u] = num
            num += 1
        if v not in nodes:
            nodes[v] = num
            num += 1
        G.add_edge(nodes[u], nodes[v])
    f.close()
    print nx.number_of_edges(G), nx.number_of_nodes(G)
    return G

nodeInfo = {}

def produce_final_plot(filename):
    f = open(filename,'r')
    x = 0
    for line in f:
        if line[0] == '<':
            x += 1
            continue
        if line[0] == 'B':
            break
        if len(line.strip()) > 0 and x == 1:
            line = line.strip().split(' ')
            if line[1] not in nodeInfo:
                nodeInfo[line[1]] = [float(line[0])]
            else:
                nodeInfo[line[1]].append(float(line[0]))
    f.close()
    normalize()
    f = open('finalplot.txt','r')
    time_taken = []
    randomness = []
    print>>f , "Time:", time_taken
    print>>f , "Randomness:", randomness
    for x in nodeInfo.keys():
        print>>f, x, nodeInfo[x]
    f.close()

def normalize():
    total = [0.0 for _ in range(len(nodeInfo[0]))]
    for x in nodeInfo.keys():
        for y in range(len(nodeInfo[x])):
            total[y] += nodeInfo[x][y]
    for x in nodeInfo.keys():
        for y in range(len(nodeInfo[x])):
            nodeInfo[x][y] /= total[y]



def approximate(G):
    D = nx.diameter(G)-3
    paths = nx.all_pairs_shortest_path(G,cutoff=D)
    centralityScore= {}
    total = 0.0
    for path in paths.keys():
        for p in paths[path].keys():
            for nodes in paths[path][p]:
                if nodes not in centralityScore:
                    centralityScore[nodes] = 1.0
                    total += 1.0
                else:
                    centralityScore[nodes] += 1.0
                    total += 1.0
    for x in centralityScore.keys():
        centralityScore[x] /= total
    return centralityScore

def writeFile(G, filename):
    nf = open(filename,'w')
    print>>nf, 'p sp', nx.number_of_nodes(G)+1, nx.number_of_edges(G)
    for u, v in G.edges():
        print>>nf, 'e', u, v, '1'
    nf.close()

if __name__ == "__main__":
    filename = 'Fresh/facebook_combined.txt'
    G = extract(filename)
    writeFile(G,"facebook.txt")