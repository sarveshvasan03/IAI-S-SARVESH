graph1 = { 
   "a" : ["b","c"],
   "b" : ["d", "e"],
   "c" : ["b","f"],
   "d" : [],
   "e" : ["f"],
   "f" : []
}	 
print(graph1)
color={}
parent={}
trav_time={}
dfs_traversal_output=[]

for node in graph1.keys():
    color[node]= "W"
    parent[node]= None
    trav_time[node]= [-1,-1]

print(color)
print(parent)
print(trav_time)

time=0
def dfs_util(u):
    global time
    color [u] = "G"
    trav_time[u][0]=time
    dfs_traversal_output.append(u)
    for v in graph1[u]:
        if color[v] == "w":
            parent[v]=u
            dfs_util (v)	    
    color[u]="B"
    trav_time[u][1]=time
    time+=1

dfs_util("a")
print(dfs_traversal_output)
print(parent)
print(trav_time)