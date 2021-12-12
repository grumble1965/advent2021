import sys
from graph import Graph


def find_all_paths(g, start, end, path=[]):
    path = path + [start]
    if start == end:
        # print('bail 1')
        return [path]
    if start not in g.nodes():
        # print('bail 2')
        return []
    paths = []
    for (_, v, _) in g.edges(from_node=start):
        # print('look at ', v, ' with type ', type(v), ' path = ', path)
        if v.isupper() or (v.islower() and v not in path):
            extended_paths = find_all_paths(g, v, end, path)
            for p in extended_paths:
                paths.append(p)
    return paths


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    g = Graph()
    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()
            # print(f"{tmp}")
            v1, v2 = tmp.split('-')
            g.add_edge(v1, v2, bidirectional=True)

    foo = find_all_paths(g, 'start', 'end', [])
    for p in foo:
        print(p)
    print(len(foo))


if __name__ == '__main__':
    main()
