import sys, fileinput, collections

def main():
    fileInput = fileinput.input()
    graph = collections.defaultdict(dict)
    distgraph = collections.defaultdict(dict)
    # reads first line (default speed)
    defaultSpeed = float(input())

    # reads graph adjacency list
    for line in fileInput:
        if len(line) > 2:
            if line.count(" ") < 3:
                node0, node1, dist = map(str, line.split())
                maxSpd = defaultSpeed
            else:
                node0, node1, dist, maxSpd = map(str, line.split())
            graph[node0][node1] = [float(maxSpd)]
            distgraph[node0][node1] = float(dist)
        else:
            break


    graph['aa']['b'].append(69.0)
    print(graph['aa'])

    path = []
    # reads waze velocities
    for line in fileInput:
        if line.count(" ") > 0:
            spl = line.split()
            node0 = spl[0]
            node1 = spl[1]
            for i in range(2,len(spl)):
                graph[node0][node1].append(float(spl[i]))
        else:
            spl = line.split()
            path.append(spl[0])

    print(path)
    print(graph)


if __name__ == '__main__':
    main()
