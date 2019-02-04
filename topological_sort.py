#Kahn's Algorithm For Topological Sort
from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices

    def add_directed_edge(self, src, dest):
        self.graph[src].append(dest) 

    def topological_sort(self):
        indegree_count = [0]*self.vertices
        top_order = []
        queue = []
        count = 0

        for key, val in self.graph.iteritems():
            for node in val:
                indegree_count[node]+=1

        for i in xrange(self.vertices):
            if indegree_count[i] == 0:
                queue.append(i)

        while queue:
            node = queue.pop(0)
            top_order.append(node)

            for i in self.graph[node]:
                indegree_count[i]-=1
                if indegree_count[i] == 0:
                    queue.append(i)
            count+=1

        if count != self.vertices:
            print "Topological sort not possible"
        else :
            print top_order 

def main():
    g = Graph(8)
    g.add_directed_edge(5,0)
    g.add_directed_edge(5,2)
    g.add_directed_edge(4,0)
    g.add_directed_edge(4,1)
    g.add_directed_edge(2,3)
    g.add_directed_edge(3,1)
    g.add_directed_edge(7,6)
    print "Topological Sort"
    g.topological_sort()

if __name__ == "__main__":
    main()
