"""
The input graph must be connected and undirected.
DFS is done to detect to cycle and to find its length.
Few flag are used to check the process.
"""

from collections import defaultdict

class Graph:
    
    def __init__(self,v):
        self.v = v
        self.graph = defaultdict(list)
        self.end = False
        self.rob = False
        self.length = 0

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def checkCycle(self):
        visited = [False for i in range(self.v)]
        length = 0
        for i in range(self.v):
            if visited[i] == False:
                if self.dfs(i,visited,-1) == True:
                    #if cycle exists and length is more than 3 the robber will always win.
                    if self.length >= 4:
                        self.rob = True
                    self.length = 0

    def dfs(self,i,visited,parent):
        visited[i] = True
        for j in self.graph[i]:
            
            #if again starting from same node than new direction and so length becomes zero.
            if self.end:
                self.length = 0
                
            #Not visited --> than do DFS
            if visited[j] == False:
                self.length += 1
                if self.dfs(j,visited,i):
                    return True
                
            #if cycle exists than below condition holds.
            elif parent != j:
                return True
            
        self.end = True
        return False
"""
some examples
"""
"""
g = Graph(9) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(0, 6)
g.addEdge(1, 7)
g.addEdge(7,8)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(2,5)
g.addEdge(2,4)
----------------
g = Graph(9)
g.addEdge(0, 1) 
g.addEdge(1, 2) 
g.addEdge(3, 6)
g.addEdge(2, 4)
g.addEdge(4,5)
g.addEdge(5,0)
g.addEdge(3,7)
g.addEdge(7,6)
g.addEdge(0,8)
g.addEdge(3,8)
"""
g = Graph(9)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(3,5)
g.addEdge(4,5)
g.addEdge(5,6)
g.addEdge(6,8)
g.addEdge(6,7)
g.addEdge(7,8)
g.checkCycle()
if  g.rob:
    print("Robber wining graph")
else:
    print("Cop wins")
    
