import sys
from graph import Graph


def path_has_duplicates(path):
    lowers = [n for n in path if n.islower()]
    if 'start' in lowers:
        lowers.remove('start')
    if 'end' in lowers:
        lowers.remove('end')
    counts = [path.count(ll) for ll in lowers if path.count(ll) > 1]
    return len(counts) > 0


def visit_this_node(v, path):
    if v.isupper():
        return True
    if v in ['start', 'end']:
        return v not in path
    dupes = path_has_duplicates(path)
    if not dupes and v.lower() and path.count(v) < 2:
        return True
    if dupes and v.lower() and path.count(v) < 1:
        return True
    return False


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
        if visit_this_node(v, path):
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
    # for p in foo:
    #     print(p)
    print(len(foo))


if __name__ == '__main__':
    main()
