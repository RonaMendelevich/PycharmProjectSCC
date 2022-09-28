from binary_read_final_file import graph1
from binary_read_final_file import start
from datetime import datetime



visited = set()  # Set to keep track of visited nodes.
finish = []
scc = set()
res = None


# dfs algorithm
def dfs(visited, graph1, node):
    if node not in visited:
        #print("node entered now")
        #print(node)
        visited.add(node)

        for neighbour in graph1[node]:
            #print("node is " + str(node))
            if neighbour not in visited:
                #print("the neighbor is " + str(neighbour))
                dfs(visited, graph1, neighbour)
        finish.append(node)
        #print("added to finish " + node)


# edges reversed dfs
def dfs_rev(visited, g, node):
    #print("visited nodes are:")
    #print(visited)
    if node not in visited:
        #print("reversed node entered ")
        #print(node)
        visited.add(node)
        #print("none_keys:")
        #print(none_keys)
        if node not in none_keys:
            for neighbour in g[node]:
                if neighbour not in visited:
                    dfs_rev(visited, g, neighbour)
                    # if neighbour in visited:
        #print("node about to be added: " + str(node))
        scc.add(node)


# iterations over graph nodes in alphabet order
def loop1(visited, graph1, node):

    dfs(visited, graph1, node)
    #print("Hi im here")

    temp = iter(graph1)
    for key in temp:
        #print("the key is " + key)
        if key not in finish:
            #print("entered")
            dfs(visited, graph1, key)


# iterations over finish array in reverded order
def loop2(finish, g):
    #print("the SCC are:")
    for i in finish:
        scc.clear()
        dfs_rev(visited, g, i)
        is_empty = (len(scc) == 0)
        if not is_empty:

            print(scc)


# graph dictionary transpose
def invert_dol(graph1):
    newdict = {}
    for k in graph1:
        for v in graph1[k]:
            newdict.setdefault(v, []).append(k)
    #print("inverted fraph is: ")
    #print(newdict)
    return newdict


def mazal3(graph1, g):
    for tempo in graph1:
        flag = 0
        #tempo = k
        for k in g:

            if tempo == k:
                flag = 1
                break
        if flag == 0:
            g[tempo] = [None]
            #print("added!!!")
    for k in g:
        if g[k] == [None]:
            none_keys.append(k)
            #print("22222NONE KEYS ADDED!")
    #print("none_keys are:")
    #print(none_keys)

# main code

#graph = convert_int_graph_to_str(graph)
#(graph1)
res = list(graph1.keys())[0]

loop1(visited, graph1, res)
g = invert_dol(graph1)
none_keys = []


mazal3(graph1, g)
#print("reversed graph")
#print(g)
res = finish[::-1] # reversing using list slicing
finish = res
visited.clear()
print("the sccs are:")
loop2(finish, g)

print (datetime.now()-start)
