from queue import Queue
graph = { 
   "a" : ["b","d"],
   "b" : ["a", "c"],
   "c" : ["b"],
   "d" : ["a","e","f"],
   "e" : ["d","f","g"],
   "f" : ["d","e","h"],
   "g" : ["e","h"],
   "h" : ["g","f"],
}	 
print(graph)

#bfscode
visited={}
level={}
parent={}
bfs_traversal_output =[]
queue=Queue()

for node in graph.keys():
    visited[node]=False
    parent[node]=None
    level[node]=-1
    
print(visited)    
print(level)
print(parent)

s="a"
visited[s]=True
level[s]=0
queue.put(s)

while not queue.empty():
    u=queue.get()
    bfs_traversal_output.append(u)

    for v in graph[u]:
        if not visited[v]:
            visited[v]=True
            parent[v]=u
            level[v]=level[u]+1
            queue.put(v)

print(bfs_traversal_output)

print(level)