from json import dumps


class Tree:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children if children is not None else []

    def __dict__(self):
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent=None):
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        return self.__dict__() == other.__dict__()

    def from_pov(self, from_node):
        graph = {}

        def build_graph(node, parent=None):
            graph.setdefault(node.label, [])
            if parent:
                graph[node.label].append(parent)
                graph[parent].append(node.label)

            for child in node.children:
                build_graph(child, node.label)

        build_graph(self)

        if from_node not in graph:
            raise ValueError("Tree could not be reoriented")

        def rebuild(label, parent=None):
            children = []

            for neighbor in graph[label]:
                if neighbor != parent:
                    children.append(rebuild(neighbor, label))

            return Tree(label, children)

        return rebuild(from_node)

    def path_to(self, from_node, to_node):
        graph = {}

        def build_graph(node, parent=None):
            graph.setdefault(node.label, [])
            if parent:
                graph[node.label].append(parent)
                graph[parent].append(node.label)

            for child in node.children:
                build_graph(child, node.label)

        build_graph(self)

        if from_node not in graph:
            raise ValueError("Tree could not be reoriented")

        if to_node not in graph:
            raise ValueError("No path found")

        path = []
        visited = set()

        def dfs(node):
            path.append(node)

            if node == to_node:
                return True

            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True

            path.pop()
            return False

        if dfs(from_node):
            return path

        raise ValueError("No path found")