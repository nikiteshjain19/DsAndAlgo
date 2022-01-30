"""
Non - recursive
Goes to neighbor before going to children
Mostly used for searching when you do not want to traverse all nodes

"""


class Graph:

    def __init__(self, nodes):
        self.nodes = nodes
        self.visited = []

    def bfs(self, source, destination):
        if source not in self.nodes:
            print("Source node not found")
            return False
        queue = [source]
        while len(queue) > 0:
            root = queue.pop(0)
            if root in self.visited:
                continue
            self.visited.append(root)
            if root == destination:
                return True
            for i in self.nodes[root]:
                queue.append(i)
        return False


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
    print(graph.bfs("z", "6"))


if __name__ == '__main__':
    main()
