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
    Total = [42386761714.0,42158338560.0, 40115509756.0, 32883228430.0, 20134083778.0, 7911841702.0]
    Node = [10589014.0201, 350050670.634, 1715417960.14,  4857640744.96, 5325363855.22, 3009862742.87]
    Norm = [0.000249818896087, 0.00830323685872, 0.0427619634045, 0.14772396072, 0.264494968529, 0.380425045929]
    Time = [ 5*60+12.796 ,  10*60+44.934, 13*60+35.715, 14*60+30.349, 14*60+41.543, 14*60+42.633]
    Total = [41118428808.0,  32346725624.0, 18213064022.0, 6688875402.0, 1271750808.0, 129843924.0]
    Node = [2025985036.03, 5734455090.51,  5140384069.45, 2741962011.79, 660323291.628,  72895857.1766]
    Norm = [0.049271946783, 0.177280852386, 0.282236095104, 0.409928702061,0.519223803496,0.561411384769]
    Time = [0*60+6.677, 1*60+2.249, 4*60+40.717, 9*60+54.543, 13*60+23.598, 14*60+45.286]
    tot = sum(Time)
    newTime = []
    for x in reversed(Time):
        newTime.append(x/tot)
    line1, = plt.plot(Total, label='Total')
    line2, = plt.plot(Node, label='BC of Node')
    line = [line1, line2]
    leg = ['Total','BC of Node']
    plt.legend(line, leg)
    plt.show()
    line1, = plt.plot(Norm, label='Normalized BC of node')
    line2, = plt.plot(newTime, label='Time')
    leg = ['Normalized BC of Node', 'Time']
    plt.legend([line1, line2], leg)
    plt.show()

if __name__ == "__main__":
    plot()
    """
    global nodeMap
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