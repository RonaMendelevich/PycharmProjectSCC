import numpy as np
import numpy.random
import random
#import time
#start_time = time.time()

from datetime import datetime
#start=datetime.now()

#main code
input_a = input("How many nodes?")
nodes = int(input_a)
input_b = input("How many edges?")
edges = int(input_b)
#f = open("writescc.txt.txt", "w+")
#nodes = 1000
#edges = 888888
start = datetime.now()
graph = {}
graph = dict()
for i in range(nodes):
    graph[i+1] = []
print(graph)

for i in range(edges):
    # generate 2 random nodes and write to file
    node1 = random.randrange(1, nodes+1)
    print(node1)
    node2 = random.randrange(1, nodes+1)
    while node1 == node2:  # self loop check
        node2 = random.randrange(1, nodes)
    print(node2)
    # for value in graph[node]:
    no2 = str(node2)
    values1 = graph.get(node1)

    if node2 not in values1:
        print("entered")
        graph[node1].append(node2)
        print("dict is:")
        print(graph)
    else:
        print("else")
        i = i + 1
#print(start_time)
#print("--- %s seconds ---" % (time.time() - start_time))

#Statements

print (datetime.now()-start)
