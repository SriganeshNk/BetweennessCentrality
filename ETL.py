__author__ = 'root'

import networkx as nx
import random
import matplotlib.pyplot as plt

def get_number(node):
    if node in nodeMap:
        return nodeMap[node]
    else:
        nodeMap['max'] += 1
        nodeMap[node] = nodeMap['max']
        reverseMap[nodeMap['max']] = node
        return nodeMap[node]


def get_nodes(nodes):
    if type(nodes) != list:
        return get_number(nodes)
    else:
        for i in range(len(nodes)):
            nodes[i] = get_number(int(nodes[i]))
        return nodes


def readGraph(files):
    global nodeMap, reverseMap
    nodeMap = {'max': 0}
    reverseMap = {}
    G = nx.Graph()
    for x in files:
        f = open(x)
        for line in f:
            line = line.split(":")
            me = int(line[0].strip())
            friends = line[1].strip().split(',')
            if len(friends) > 1:
                if friends[0] != 'private' and friends[0] != 'notfound':
                    me = get_nodes(me)
                    friends = get_nodes(friends)
                    for x in friends:
                        G.add_edge(me, x)
        f.close()
    return G


def writeOriginal(G, filename):
    nf = open(filename, 'w')
    for u in G.nodes():
        connect = G.adj[u]
        line = str(u)+":"
        for v in connect:
            line += str(v)+","
        line = line[:len(line)-1]
        print>>nf, line
    nf.close()


def writeFile(G, filename):
    nf = open(filename,'w')
    print>>nf, 'p sp', nodeMap['max'], len(G.edges())
    for u, v in G.edges():
        print>>nf, 'e', u, v, '1'
    nf.close()


def getAdjList(node, Adj):
    connect = Adj[node].keys()
    L = connect
    return L


def drawApproximate(G, x):
    connect = getAdjList(x, G.adj)
    for each in connect:
        adj = G.adj[each].keys()
        for y in adj:
            if y == x:
                continue
            G.add_edge(x,y)
    for each in connect:
        if each == x:
            continue
        G.remove_node(each)
    return x, G


def writeNodeMap(filename):
    f = open(filename,"w")
    for i in nodeMap.keys():
        print>>f, i,":",nodeMap[i]
    f.close()


def normalizeOut(filename, index):
    f = open(filename,'r')
    x = 0
    BC = []
    for line in f:
        if line[0] == '<':
            x += 1
        if len(line.strip()) > 0 and x == 1:
            line = line.strip().split(' ')
            BC.append(float(line[0]))
    f.close()
    print BC[index]/sum(BC)

def plot():
    f = open('Fresh/finalplot15.txt','r')
    num = 0
    sampleSize = []
    timeTaken = []
    bcScores = []
    for line in f:
        if num == 0:
            timeTaken = [float(x.strip().strip(']')) for x in line.split('[')[1].split(',')]
        elif num == 1:
            sampleSize = [float(x.strip().strip(']')) for x in line.split('[')[1].split(',')]
        else:
            isSame = {}
            L = [float(x.strip().strip(']'))*10000000000.0 for x in line.split('[')[1].split(',')]
            for x in L:
                if x not in isSame:
                    isSame[x] = 1
                else:
                    isSame[x] += 1
            notZero = True if any(L) else False
            notSame = True if len(isSame.keys()) > 1 else False
            goodSample = True if L[0] > 100.0 else False
            if notZero and notSame and goodSample:
                bcScores.append(L)
        num += 1
    plt.plot(sampleSize, timeTaken)
    plt.xlabel('Sample %')
    plt.ylabel('Time Taken in minutes')
    plt.show()
    #num = 0
    plt.xlabel('Sample %')
    plt.ylabel('Betweenness Scores')
    for line in bcScores:
        if line[0] > 10000.0:
            continue
        plt.plot(sampleSize, line)
    plt.show()

if __name__ == "__main__":
    plot()
    """global nodeMap
    G = readGraph(["segmentofaaa"])
    x = random.randrange(1, nodeMap['max'])
    for i in range(10):
        if i == 2:
            writeOriginal(G, "3_dimacs.txt")
            MaxG = readGraph(["3_dimacs.txt"])
            print x, nodeMap[x]
            writeFile(MaxG, "3_Directed_Dimacs.txt")
        if i == 3:
            writeOriginal(G, "4_dimacs.txt")
            MaxG = readGraph(["4_dimacs.txt"])
            print x, nodeMap[x]
            writeFile(MaxG, "4_Directed_Dimacs.txt")
        if i == 4:
            writeOriginal(G, "5_dimacs.txt")
            MaxG = readGraph(["5_dimacs.txt"])
            print x, nodeMap[x]
            writeFile(MaxG, "5_Directed_Dimacs.txt")
        if i == 5:
            writeOriginal(G, "6_dimacs.txt")
            MaxG = readGraph(["6_dimacs.txt"])
            print x, nodeMap[x]
            writeFile(MaxG, "6_Directed_Dimacs.txt")
        if i == 6:
            writeOriginal(G, "7_dimacs.txt")
            MaxG = readGraph(["7_dimacs.txt"])
            print x, nodeMap[x]
            writeFile(MaxG, "7_Directed_Dimacs.txt")
        if i == 7:
            writeOriginal(G, "8_dimacs.txt")
            MaxG = readGraph(["8_dimacs.txt"])
            print x, nodeMap[x]
            writeFile(MaxG, "8_Directed_Dimacs.txt")
        if i == 8:
            writeOriginal(G, "9_dimacs.txt")
            MaxG = readGraph(["9_dimacs.txt"])
            print x, nodeMap[x]
            writeFile(MaxG, "9_Directed_Dimacs.txt")
        if i == 9:
            writeOriginal(G, "10_dimacs.txt")
            MaxG = readGraph(["10_dimacs.txt"])
            print x, nodeMap[x]
            writeFile(MaxG, "10_Directed_Dimacs.txt")
        x, G = drawApproximate(G, x)"""