visited = set()  # Set to keep track of visited nodes.
finish = []
scc = set()
res = None


def next_node(x):
    x33 = x % 10
    x22 = (x % 100) / 10
    x11 = x / 100

    x3 = int(x33)

    x2 = int(x22)
    x1 = int(x11)

    #print("now state")
    #print(x1, x2, x3)

    x1_new = x2 | x3
    x2_new = x1 & x2
    x3_new = x1

    next_state = ((x1_new * 100) + (x2_new * 10) + x3_new)

    #print("next state united:")
    #print(next_state)
    return next_state


def decimalToBinary(n):
    return bin(n).replace("0b", "")


def binary_to_decimal(binary):
    decimal = 0
    binary = list(str(binary)) #convert binary to a list
    binary = binary[::-1]      #reverse the list
    power = 0   #declare power variable (for 1st elem == 0)
    for number in binary:
        if number == '1':
            decimal += 2**power
        power += 1 #increase power by 1
    return decimal


# dfs algorithm
def dfs(visited, graph, node):
    if node not in visited:
        visited.add(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                dfs(visited, graph, neighbour)
        finish.append(node)
        #print("added to finish " + node)

# edges revered dfs
def dfs_rev(visited, g, node):
    if node not in visited:
        #print("reversed node entered ")
        #print(node)
        visited.add(node)
        if node not in none_keys:
            for neighbour in g[node]:
                if neighbour not in visited:
                    dfs_rev(visited, g, neighbour)
                    # if neighbour in visited:
        scc.add(node)


# iterations over graph nodes in alphabet order
def loop1(visited, graph, node_x):

    dfs(visited, graph, node_x)
    temp = iter(graph)
    for key in temp:
        #print("the key is " + key)
        if key not in finish:
            #print("entered")
            dfs(visited, graph, key)


# iterations over finish array in reverded order
def loop2(finish,g):
    print("the SCC are:")
    for i in finish:
        scc.clear()
        dfs_rev(visited, g, i)
        is_empty = (len(scc) == 0)
        if not is_empty:

            print(scc)


# graph dictionary transpose
def invert_dol(graph):
    newdict = {}
    for k in graph:
        for v in graph[k]:
            newdict.setdefault(v, []).append(k)
    return newdict


def mazal3(graph, g):
    for k in graph:
        flag = 0
        tempo = k
        int_tempo = int(k)
        print("tempo is")
        print(tempo)
        print("invert g")
        print(g)
        for k in g:
            int_k = int(k)
            print("k is:")
            print(k)
            if int_tempo == int_k:
                print("in")
                flag = 1
                break
        if flag == 0:  # tempo not found in g
            print("ma")
            g[tempo] = [None]
            #print("added!!!")
    for k in g:
        if g[k] == [None]:
            none_keys.append(k)
            print("none keys")
            print(none_keys)


nodes = 2**3

graph = {}
graph = dict()
for i in range(nodes):
    str_i = str(i)
    graph[str_i] = []

print(graph)

for i in range(nodes):
    x = i
    xx = decimalToBinary(x)
    int_x = int(xx)

    next_x = next_node(int_x)
    dec_next_x = binary_to_decimal(next_x)
    str_x = str(dec_next_x)
#    int_x = int(dec_next_x)

    # add to dict
    str_i = str(i)
    graph[str_i] = []
    graph[str_i].append(str_x)
print("dict is:")
print(graph)


# main code
loop1(visited, graph, str_x)
g = invert_dol(graph)
#print("invert is")
#print(g)
none_keys = []

mazal3(graph, g)
print("reversed graph")
print(g)
res = finish[::-1] # reversing using list slicing
finish = res
visited.clear()
loop2(finish, g)




