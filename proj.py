import fileinput, random
from heapq import *
from collections import defaultdict

def main():
    fileInput = fileinput.input()
    graph = defaultdict(dict)
    distgraph = defaultdict(list)
    path = []
    avgs = set([])

    defaultSpeed = float(input())
    for line in fileInput:
        if len(line) > 2:
            readNode(line, graph, distgraph, defaultSpeed)
        else:
            break

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

    # print("\n== iterations ==")
    for i in range(0,100):
        # print('\n=> it ', end="")
        # print(i+1)
        gs = sample(graph) # adjacency list w/ sample max speed
        tgs = timefy(gs, distgraph) # multiplies distances with max speed and creates a graph with 'time' as key
        sp = dijkstra(tgs, path[0], path[1])
        if sp != float("inf"):
            avgs.add(sp)

    avgs = sorted(list(avgs), key=lambda x: x[0])

    if len(avgs) > 0:
        res1 = avgs[0]
        print("{:.1f}".format(res1[0]))
        print(' '.join(res1[1]))
    if len(avgs) > 1:
        res2 = avgs[1]
        print("{:.1f}".format(res2[0]))
        print(' '.join(res2[1]))


def readNode(line, graph, distgraph, defSpeed):
    if line.count(" ") < 3:
        node0, node1, dist = map(str, line.split())
        maxSpd = defSpeed
    else:
        node0, node1, dist, maxSpd = map(str, line.split())
    graph[node0][node1] = [float(maxSpd)]
    distgraph[node0].append((float(dist),node1))
    # distgraph[node0][node1] = float(dist)

def dijkstra(g, f, t):
    q, seen, mins = [(0,f,())], set(), {f: 0}
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path += (v1,)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next,v2,path))
    return float("inf")

def sample(g):
    r = defaultdict(dict)
    for k, subdict in g.items():
        for sk, value in subdict.items():
            rv = random.choice(value)
            r[k][sk] = rv
    return r

def timefy(g, dg):
    tg = defaultdict(list)
    for key, value in dg.items():
        for dist, dest in value:
            time = g[key][dest]
            if (time*dist) != 0:
                tg[key].append((time*dist, dest))
    return tg

if __name__ == '__main__':
    main()
