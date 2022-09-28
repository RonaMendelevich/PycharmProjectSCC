from binary_read_final_file import graph1
#from SCC1 import graph1

import random


# picks random vertex from a vertex list
def pick(x):
    return random.choice(x)


# convert dict.keys into a list
def getlist(g):
    return list(g.keys())


# union of lst1+lst2
def union(lst1, lst2):
    final_list = list(set(lst1) | set(lst2))
    return final_list


# lst1 cuts lst2
def cut(lst1, lst2):
    intersection_set = set.intersection(set(lst1), set(lst2))
    return list(intersection_set)


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


# lst1 - lst2
def exclude(lst1, lst2):
    c = cut(lst1, lst2)
    for i in c:
        if i in lst1:
            lst1.remove(i)
    return lst1


# returns set of vertexes that are neighbours of v
def img(v):
    list_img = []
    for i in v:
        list_img.append(graph1.get(i))

    flat_list = [item for sublist in list_img for item in sublist]

    return flat_list


# returns set of vertexes that v is their neighbour:
def preimg(v):
    list_img = []
    items_list = graph1.items()
    for i in v:
        for item in items_list:
            if i in item[1]:
                list_img.append(item[0])

    flat_list = [item for sublist in list_img for item in sublist]

    return flat_list


'''def img(v):
    list_img = []
    for i in v:
        list_img.append(graph.get(i))
    #print("img list is:")
    #print(list_img)
    flat_list = list_img.copy()
    #flat_list = [item for sublist in list_img for item in sublist]

    return flat_list


# returns set of vertexes that v is their neighbour:
def preimg(v):
    list_img = []
    items_list = graph.items()
    for i in v:
        for item in items_list:
            if i in item[1]:
                list_img.append(item[0])

    #flat_list = [item for sublist in list_img for item in sublist]
    flat_list = list_img.copy()

    return flat_list'''


def partial_graph(a, b):  # return the partial graph needed
    '''print("list a is:")
    print(a)
    print("list b is:")
    print(b)'''
    exclude_list = exclude(a, b)
    '''print("exclude_list is:")
    print(exclude_list)'''

    new_graph = {key: graph1[key] for key in exclude_list}

    '''for key in new_graph:
        # print("the key is:")
        # print(key)
        for value in new_graph.values():
            for i in value:
                if i not in exclude_list:
                    # print("the i is:" )
                    # print(i)
                    value.remove(i)
'''
    print("the new graph is:")
    print(new_graph)
    return new_graph


def lockstep(graph):
    p = getlist(graph)
    print(p)
    print(type(p))

    f = []
    f_front = []
    b = []
    b_front = []
    c = []
    converged = []

    if p:  # check if p is empty. if so, return from algorithm
        print("list is not empty")
    else:
        return

    v = pick(p)
    print("v= ")
    print(v)

    f.append(v)
    f_front.append(v)
    b.append(v)
    b_front.append(v)

    '''f_front = exclude(cut(img(f_front), p), f)
    print("f_front is:")
    print(f_front)

    b_front = exclude(cut(preimg(b_front), p), b)
    print("b_front:")
    print(b_front)

    f = union(f, f_front)
    b = union((b, b_front))'''
    while (len(f_front) > 0) and (len(b_front) > 0):
        print("say hi")
        f_front = exclude(cut(img(f_front), p), f)
        print("f_front is:")
        print(f_front)

        b_front = exclude(cut(preimg(b_front), p), b)
        print("b_front:")
        print(b_front)

        f = union(f, f_front)
        b = union(b, b_front)

    if len(f_front) == 0:  # if f_front is an empty group
        converged.clear()
        converged = f.copy()

    else:
        converged.clear()
        converged = b.copy()
    print("converged is:")
    print(converged)

    while (len(cut(f_front, b)) > 0) or (len(cut(b_front, f)) > 0):
        print("entereddd")
        f_front = exclude(cut(img(f_front), p), f)
        print("ffffff_front is:")
        print(f_front)

        b_front = exclude(cut(preimg(b_front), p), b)
        print("bbbbbbb_front:")
        print(b_front)

        f = union(f, f_front)
        b = union(b, b_front)

    c = cut(f, b)
    scc.append(c)

    copy_converged = list(converged)
    # print("copy_converged111 now is:")
    # print(converged)
    part_graph1 = partial_graph(converged, c)
    # print("copy_converged222 now is:")
    # print(converged)
    part_graph2 = partial_graph(p, copy_converged)

    print("part_graph1 is:")
    print(part_graph1)
    print("part_graph2 is:")
    print(part_graph2)

    if len(part_graph1) > 0:
        lockstep(part_graph1)
    else:
        print("end of lockstep1 here")

    if len(part_graph2) > 0:
        lockstep(part_graph2)
    else:
        print("end of lockstep2 here")

    print("the final scc are:")
    print(scc)


scc = []
print("start graph is:")
print(graph1)
lockstep(graph1)
print("the final scc are:")
print(scc)

