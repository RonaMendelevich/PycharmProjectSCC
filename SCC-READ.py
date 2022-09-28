#graph = {
#    'A' : ['B'],
#    'B' : ['A'],
#    'C' : ['A', 'D', 'E'],
#    'D' : ['A'],
#    'E' : ['B'],
#    'F' : ['A'],
#    'G' : ['C']
#}


visited = set()  # Set to keep track of visited nodes.
finish = []
scc = set()
res = None

# dfs algorithm
def dfs(visited, graph, node):
    if node not in visited:
        #print(node)
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
def loop1(visited, graph):
    res = next(iter(graph))
    node = str(res)
    #print('THIS IS THE FIRST NODE!!!' + node)
    dfs(visited, graph, node)

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
        for k in g:
            if tempo is k:
                flag = 1
                break
        if flag == 0:
            g[tempo] = [None]
            #print("added!!!")
    for k in g:
        if g[k] == [None]:
            none_keys.append(k)
            #print("22222NONE KEYS ADDED!")


#def read_file(f):
    #print(f.readline())


def generator(path):
    word = ''
    with open(path) as file:
        while True:
            char = file.read(1)
            if char.isspace():
                if word:
                    yield word
                    word = ''
            elif char == '':
                if word:
                    yield word
                break
            else:
                word += char


def create_dict(path):
    graph = {}
    words = generator(path)
    key = next(words)
    #print(key)
    value = next(words)
    #print(value)
    graph.setdefault(key, [])
    graph[key].append(value)

    for word in words:
        print("word type")
        print(type(word))
        key = word
        #print(key)
        value = next(words)
        #print(value)
        graph.setdefault(key, [])
        graph[key].append(value)

    return graph


# main code

graph = create_dict('D:\\ronaaa\\PycharmProject\\scc-read.txt.txt')
#print(graph)
loop1(visited, graph)
g = invert_dol(graph)
none_keys = []
#g = in
mazal3(graph, g)
#print("reversed graph")
#print(g)
res = finish[::-1] # reversing using list slicing
finish = res
visited.clear()
loop2(finish, g)