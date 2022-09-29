# SCC PROJECT

#### INTRODUCTION


Our project deals with strongly connected components, that is, given a graph we would like to find the connected components in it.
We chose to implement the project in the Python language.
SCC is a set of vertices in which every vertex is connected to every other vertex in the set.

A directed graph is called well connected (or strongly connected) if there is a route from every node to every other node.
For a general directed graph, the graph can always be decomposed into well-connected components - maximal subgraphs of
The original graph, each of which is a well-connected graph in itself.
This decomposition constitutes a division of the graph into foreign classes - two different components cannot contain a common node.


## The project files

#### SCC1

Computes the SCC for a given graph in the code via dfs algorithm.
The graph in the code represented via a dictionary by the following way: each key represents a node (the source vertex) and the values for that key represent its neighbors.
This file prints the graph's SCC.

#### SCC-READ

Compute the SCC via dfs algorithm, for a graph computed from a given txt file (scc-read.txt)
The graph in scc-read.txt file described by the following: Each line represent an edge from vertex to vertex, for example the first line: 1  2 describes an outgoing edge
from vertex 1 to vertex 2. 
See the example from the file:

![image](https://user-images.githubusercontent.com/75082928/193045280-32d73c07-b63e-426c-8937-a45a077530eb.png)


#### SCC-RANDOM

In this code file it receives as input from the user the number of vertices and number of edges, and based on this
a graph will be randomly computed (using the random function).The SCC is computed from this graph.

#### binary_read_SCC.py

Computes the SCC from a graph constructed out of binary logical functions.

The graph constructed by the following way:
A path from node to node will be determined with the help of logical functions when each variable is defined as one bit and each bit has a logical function that calculates its next state(node).
This is how it is determined from which vertex to which vertex an edge will go.
Example:

![image](https://user-images.githubusercontent.com/75082928/193059239-670cbed9-4a28-416c-bfbd-bf0a625bf9fa.png)


'binary_read_SCC.py' file imports the graph from the file: 'binary_read_final_file.py'.
'binary_read_final_file.py' computed the graph from a text file from the user: 'fun_fun.txt'
In the text file each line represents the binary logical function for each variable respectively.
Example:

![image](https://user-images.githubusercontent.com/75082928/193056885-a816b02e-9027-41ff-bb82-c93d4c775bf0.png)


*First line holds the number of 
Line number 2 contains the binary logical function for variable number 2. (starts from 1 not zero)



