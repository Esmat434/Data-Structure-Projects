from cities import nodes,routes

class MiniGoogleMaps:
    def __init__(self,nodes,edges):
        self.nodes=nodes
        self.edges=edges
        self.adj_dict=self.create_adj_dict()
        self.adj_matrix=self.create_adj_matrix()
    
    def create_adj_dict(self):
        adj_dict = {}
        for start, dist, _ in self.edges:
            if start in adj_dict:
                adj_dict[start].append(dist)
            else:
                adj_dict[start]=[dist]
        return adj_dict
    
    def create_adj_matrix(self):
        matrix = [[0 for i in range(len(self.nodes))] for j in range(len(self.nodes))]
        for route in self.edges:
            s_i = self.nodes.index(route[0])
            d_i = self.nodes.index(route[1])
            matrix[s_i][d_i]=route[2]
        return matrix
    
    def get_path(self, start, dist, path=[]):
        path = path + [start]
        if start == dist:
            return [path]
        if start not in self.adj_dict:
            return []
        paths = []
        for vertex in self.adj_dict[start]:
            if vertex not in path:
                new_paths = self.get_path(vertex, dist, path)
                for i in new_paths:
                    paths.append(i)
        return paths
    
    def distance(self,paths):
        distance = 0
        for i in range(len(paths)):
            for j in range(len(paths[i])-1):
                s_i = self.nodes.index(paths[i][j])
                d_i = self.nodes.index(paths[i][j+1])
                distance+= self.adj_matrix[s_i][d_i]
            paths[i].append(distance)
            distance=0
        return paths

    def get_path_cost(self, start, dist):
        paths = self.get_path(start, dist)
        paths = self.distance(paths)        
        return paths

    def get_shortest_path(self, start, dist, path=[]):
        path = path + [start]
        if start == dist:
            return path
        if start not in self.adj_dict:
            return None
        shortest_path=None
        for vertex in self.adj_dict[start]:
            if vertex not in path:
                n_sp = self.get_shortest_path(vertex, dist, path)
                if n_sp:
                    if shortest_path is None or len(shortest_path)>len(n_sp):
                        shortest_path=n_sp
        return shortest_path
    
    def get_shortest_path_cost(self, start, dist):
        paths = self.get_path_cost(start, dist)
        shortest_path = None
        for path in paths:
            if shortest_path is None or shortest_path[-1]>path[-1]:
                shortest_path=path
        return shortest_path
