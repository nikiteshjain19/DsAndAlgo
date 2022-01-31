"""
https://youtu.be/zaBhtODEL0w
Recursive algorithm
Goes to children before going to neighbor
"""


class Graph:

    def __init__(self, nodes):
        self.nodes = nodes
        self.visited = []

    def helper(self, child, adjacent_nodes, destination):
        if child in self.visited:
            return False
        self.visited.append(child)
        if child == destination:
            return True

        for i in adjacent_nodes:
            if self.helper(i, self.nodes[i], destination):
                return True
        return False

    def dfs(self, source, destination):
        if source not in self.nodes:
            print("Source node not found")
            return False
        return self.helper(source, self.nodes[source], destination)


def main():
    # dict is in format of node and adjacent nodes
    nodes = {"a": ["c", "k"],
             "c": ["x", "e", "a"],
             "e": ["c", "d"],
             "d": ["e", "k", "j"],
             "k": ["a", "d"],
             "x": ["c", "y"],
             "j": ["d", "l"],
             "y": ["x", "n"],
             "l": ["j", "m"],
             "m": ["l", "z"],
             "n": ["y", "z"],
             "z": ["m", "n"]}
    graph = Graph(nodes)
    print(graph.dfs("t", "a"))


if __name__ == '__main__':
    main()

