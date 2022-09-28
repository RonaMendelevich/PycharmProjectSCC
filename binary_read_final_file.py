from datetime import datetime
start=datetime.now()


def decimal_to_binary(n):
    return bin(n).replace("0b", "")


def binary_to_decimal(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        count = count + (int(arr[i]) * (2 ** i))

    return count


def convert_int_graph_to_str(graph):
    new_graph = dict()

    for key in graph:

        temp_key = str(key)
        temp_value = str(graph[key])
        temp_value_list = list(temp_value.split(","))
        new_graph[temp_key] = temp_value_list


    return new_graph


def node(x, n):  # puts binary vertex number into array
    idx = n - 1
    array = [0] * n
    new_x = x
    if len(x) <= n:
        for i in range(0, len(x)):
            array[idx] = int(new_x) % 10
            new_x = int(new_x) / 10
            idx -= 1
    # print(array)
    return array


def take_3_elements(temp1, n):
    arr.clear()
    idx_counter = 0  # need to return how many elements were handled
    not_flag = 0  # if there is a NOT it will be = 1
    number = 0  # need to count until 3, to take 3 variables to equation
    #print("temp1 in take is: ")
    #print(temp1)

    for idx, elem in enumerate(temp1):  # this needs to be 3 times or until temp is empty (the less option)

        number += 1
        if number > 3:
            break
        idx_counter += 1

        if elem == '~':  # if the operator is NOT
            not_flag = 1
            number -= 1
            #print("not flag= " + str(not_flag))

        elif elem in operator:  # element is operator
            arr.append(elem)

        else:  # element is X
            #if int(elem) in range(0, n + 1):
            if not_flag == 1:  # if there was a NOT sign
                #aa = int(temp1[])
                a = int(temp1[idx]) ^ 1  # XOR 1 works like NOT
                arr.append(a)  # add a to the equation array
                not_flag = 0

            else:  # if there wasn't a NOT sign
                arr.append(int(temp1[idx]))

    #print("arr is: ")
    #print(arr)
    #print("idx_counter is: " + str(idx_counter))
    return arr, idx_counter


def equation(arr1):  # computes the eqation of at most 3 elements

    i = 0
    answer1 = 0
    ans = []
    #print("arr1 is:")
    #print(arr1)

    # for i in range(len(arr1)):  # ans is copy of arr1
    # ans.append(arr1[i])

    if len(arr1) > 1:
        if arr1[1] == '|':
            answer1 = (arr1[0] or arr1[2])
            # print("answer for line number " + str(x) + " is:")
            # print(answer1)

        elif arr1[1] == '&':
            answer1 = (arr1[0] and arr1[2])
            # print("answer for line number " + str(x) + " is:")
            # print(answer1)

    else:
        answer1 = int(arr1[0])

    return answer1


def calc_next_node(node):
    file = open('fun_fun.txt.txt', 'r')
    n = file.readline()
    n = int(n)
    copy_temp.clear()
    min = 0
    # print("the n now is: " + str(n))
    # run on every line in the text file and read it
    for x in range(0, n):
        # x_next = [0] * n  # next node

        # print("read " + str(x) + " line")
        f = file.readline()
        # print("the read line is:")
        # print(f)
        temp = f.strip().split()
        #print("zero temp is")
        #print(temp)

        copy_temp.clear()
        for i in range(0, len(temp)):  # copy the temp array -bitewise- to a new array temp_new
            k = temp[i]

            if k in operator:
                copy_temp.append(k)
            else:
                #print("k is:")
                #print(k)
                bit = x_arr[int(k)-1]
                copy_temp.append(bit)

        #print("copy_temp is:")
        #print(copy_temp)

        if len(copy_temp) == 1:
            x_next[x] = int(copy_temp[0])
            # x_next[x]= node[ix - 1]
            # print("the x_next now is: ")
            # print(x_next)

        while len(copy_temp) > 1:
            min += 1
            arr, index = take_3_elements(copy_temp, n)  # returns arr and how many idx were taken
            # print("arr is:")
            # print(arr)
            # print("index is: " + str(index))
            answer = equation(arr)
            # print("the answer is: " + str(answer))

            # print("temp before pop is: ")
            # print(temp)
            temp_len = int(len(copy_temp))
            for i in range(0, index):
                # print("i is: " + str(i))
                # print("temp len is: " + str(len(temp)))

                if i in range(temp_len + 1):
                    # print(str(i) + "entered")
                    copy_temp.pop(0)

            copy_temp.insert(0, str(answer))  # the answer is inserted at index 0
            # print("temp now is: ")
            # print(temp)

            if len(copy_temp) == 1:  # if there is only answer in temp
                x_next[x] = int(copy_temp[0])
                # print("the x_next now is: ")
                # print(x_next)

    return x_next


def return_graph(graph):
    print("graph is:")
    print(graph)
  #  print("graph type is:")
 #   print(type(graph))
    return graph


operator = ['&', '|', '~']  # all operators possible
file = open('fun_fun.txt.txt', 'r')
n = file.readline()
#print("the n is:")
#print(n)
n = int(n)
# print(n)
temp = []
copy_temp = []
arr = []  # the read bool func goes here

x_arr = [0] * n  # current node
x_next = [0] * n  # next node

vertex_num = 2 ** n
    # print("vertex num is: " + str(vertex_num))

graph = dict()  # this dictionary will hold the graph

for i in range(0, vertex_num):  # decimal to binary

    i_binary = decimal_to_binary(i)

    #print("i_binary is: " + str(i_binary))
    x_arr = node(i_binary, n)
    x_next = calc_next_node(x_arr)
    x_next.reverse()
    next_node = binary_to_decimal(x_next)
    graph[i] = next_node

return_graph(graph)
graph1 = dict()
for key in graph:
    graph1[str(key)] = str(graph[key])

graph1 = convert_int_graph_to_str(graph)
#print("new graph is:")
#print(graph1)


#print("graph1 is:")
#print(graph1)


#print("--- %s seconds ---" % (time.time() - start_time))
#print(datetime.now()-start)
