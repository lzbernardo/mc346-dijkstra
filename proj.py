import sys, fileinput

def main():
    fileInput = fileinput.input()
    graph = {}
    # reads first line
    defaultSpeed = input()

    # reads graph adjacency list
    for line in fileInput:
        if line == "\n":
            break
        if line.count(" ") < 3:
            node0, node1, dist = map(str, line.split())
            maxSpd = defaultSpeed
        else:
            node0, node1, dist, maxSpd = map(str, line.split())

        print(node0 + ' ' + node1 + ' ' + dist + ' ' + maxSpd)
        # splitted = list(map(str, line.split()))
        # node0 = splitted[0]
        # node1 = splitted[1]
        # dist = splitted[2]
        # maxSpd = defaultSpeed
        # if len(splitted) > 3:
        #     maxSpd = splitted[3]

    print("heeeey")
    # reads velocities (?)
    for line in fileInput:
        print(line)


if __name__ == '__main__':
    main()
