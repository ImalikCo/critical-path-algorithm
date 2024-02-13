class Graph:

    def __init__(self):
        # Makes empty graph
        self.nodes = {}  
        self.edges = {}  
        self.rev_edges = {}  
        self.unseen_sources = set()  
        self.longest_in_weight = {}  
        self.longest_in_route = {}    
        self.longest_route = None
        self.longest_route_weight = None

    def add_node(self, label, weight): 
        self.nodes[label] = weight
        self.edges[label] = set()
        self.rev_edges[label] = set()
        self.unseen_sources.add(label)
       
    def add_edge(self, source, target):
        self.edges[source].add(target)
        self.rev_edges[target].add(source)
        self.unseen_sources.discard(target)
        
    def delete_edge(self, source):
        #Deletes all edges of activity
        targets = self.edges[source]
        self.edges[source] = set()
        for target in targets:
            self.rev_edges[target].discard(source)
            if len(self.rev_edges[target]) == 0:
                self.unseen_sources.add(target)                
                           
    def longest_path(self):
        while len(self.unseen_sources) > 0:
            # Returns first node and deletes it.
            sourcenode = self.unseen_sources.pop()
            
            # Takes weight of activity, returns 0 if no weight. Adds them together
            new_weight = self.longest_in_weight.get(sourcenode, 0) + self.nodes[sourcenode]
            # Takes route of activity, returns empty list if no route. Adds them together
            new_route = self.longest_in_route.get(sourcenode, []) + [sourcenode]

            # Checks if edges of activity is 0.
            if len(self.edges[sourcenode]) == 0:
                # If so; Checks if longest route exists or is smaller than current weight.
                if self.longest_route is None or self.longest_route_weight < new_weight:
                    self.longest_route = new_route
                    self.longest_route_weight = new_weight
                # Repeat if unseen_sources is bigger than 0.
            else:
                for target in self.edges[sourcenode]:
                    # Checks if longest weight is smaller.
                    if self.longest_in_weight.get(target, 0) < new_weight:
                        self.longest_in_weight[target] = new_weight
                        self.longest_in_route[target] = new_route
                # Deletes edge of activity
                self.delete_edge(sourcenode)
                
        return self.longest_route, self.longest_route_weight

if __name__ == '__main__':
    # Add nodes with their weight. Example graph.add_node('A', 4)
    graph = Graph()
    graph.add_node('', 0)
    graph.add_node('', 0)
    graph.add_node('', 0)

    
    # Add edges between two nodes. Example: graph.add_edge('A', 'B')
    graph.add_edge('', '')
    graph.add_edge('', '')
    graph.add_edge('', '')


    graph.longest_path()

    print("The critical path is %s, with a weight of %s" % (graph.longest_route, graph.longest_route_weight))
