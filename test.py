import sync_bfs
import async_bfs
import matplotlib.pyplot as plt
import simpy
import random
import networkx as nx

x = [20,40,60,80]

G20_0 = nx.watts_strogatz_graph(20,4,0.9)
G20_1 = nx.watts_strogatz_graph(20,5,0.9)
G20_2 = nx.watts_strogatz_graph(20,6,0.9)

G40_0 = nx.watts_strogatz_graph(40,4,0.9)
G40_1 = nx.watts_strogatz_graph(40,5,0.9) 
G40_2 = nx.watts_strogatz_graph(40,6,0.9)

G60_0 = nx.watts_strogatz_graph(60,4,0.9)
G60_1 = nx.watts_strogatz_graph(60,6,0.9) 
G60_2 = nx.watts_strogatz_graph(60,5,0.9)

G80_0 = nx.watts_strogatz_graph(80,4,0.9)
G80_1 = nx.watts_strogatz_graph(80,5,0.9) 
G80_2 = nx.watts_strogatz_graph(80,6,0.9)



G20_async_bfs_messageCount = [0]*3
G20_async_bfs_runtime = [0]*3
G40_async_bfs_messageCount = [0]*3
G40_async_bfs_runtime = [0]*3
G60_async_bfs_messageCount = [0]*3
G60_async_bfs_runtime = [0]*3
G80_async_bfs_messageCount = [0]*3
G80_async_bfs_runtime = [0]*3

G20_async_bfs_messageCount[0],G20_async_bfs_runtime[0] = async_bfs.test(G20_0)
G20_async_bfs_messageCount[1],G20_async_bfs_runtime[1] = async_bfs.test(G20_1)
G20_async_bfs_messageCount[2],G20_async_bfs_runtime[2] = async_bfs.test(G20_2)

G40_async_bfs_messageCount[0],G40_async_bfs_runtime[0] = async_bfs.test(G40_0)
G40_async_bfs_messageCount[1],G40_async_bfs_runtime[1] = async_bfs.test(G40_1)
G40_async_bfs_messageCount[2],G40_async_bfs_runtime[2] = async_bfs.test(G40_2)

G60_async_bfs_messageCount[0],G60_async_bfs_runtime[0] = async_bfs.test(G60_0)
G60_async_bfs_messageCount[1],G60_async_bfs_runtime[1] = async_bfs.test(G60_1)
G60_async_bfs_messageCount[2],G60_async_bfs_runtime[2] = async_bfs.test(G60_2)

G80_async_bfs_messageCount[0],G80_async_bfs_runtime[0] = async_bfs.test(G80_0)
G80_async_bfs_messageCount[1],G80_async_bfs_runtime[1] = async_bfs.test(G80_1)
G80_async_bfs_messageCount[2],G80_async_bfs_runtime[2] = async_bfs.test(G80_2)

avrg_messageCount_async = [0]*4
avrg_messageCount_async[0] = (G20_async_bfs_messageCount[0]+G20_async_bfs_messageCount[1]+G20_async_bfs_messageCount[2])//3
avrg_messageCount_async[1] = (G40_async_bfs_messageCount[0]+G40_async_bfs_messageCount[1]+G40_async_bfs_messageCount[2])//3
avrg_messageCount_async[2] = (G60_async_bfs_messageCount[0]+G60_async_bfs_messageCount[1]+G60_async_bfs_messageCount[2])//3
avrg_messageCount_async[3] = (G80_async_bfs_messageCount[0]+G80_async_bfs_messageCount[1]+G80_async_bfs_messageCount[2])//3

avrg_runtime_async = [0]*4
avrg_runtime_async[0] = (G20_async_bfs_runtime[0]+ G20_async_bfs_runtime[1]+G20_async_bfs_runtime[2])//3
avrg_runtime_async[1] = (G40_async_bfs_runtime[0]+ G40_async_bfs_runtime[1]+G40_async_bfs_runtime[2])//3
avrg_runtime_async[2] = (G60_async_bfs_runtime[0]+ G60_async_bfs_runtime[1]+G60_async_bfs_runtime[2])//3
avrg_runtime_async[3] = (G80_async_bfs_runtime[0]+ G80_async_bfs_runtime[1]+G80_async_bfs_runtime[2])//3




G20_sync_bfs_messageCount = [0]*3
G20_sync_bfs_runtime = [0]*3
G40_sync_bfs_messageCount = [0]*3
G40_sync_bfs_runtime = [0]*3
G60_sync_bfs_messageCount = [0]*3
G60_sync_bfs_runtime = [0]*3
G80_sync_bfs_messageCount = [0]*3
G80_sync_bfs_runtime = [0]*3

G20_sync_bfs_messageCount[0],G20_sync_bfs_runtime[0] = sync_bfs.test(G20_0)
G20_sync_bfs_messageCount[1],G20_sync_bfs_runtime[1] = sync_bfs.test(G20_1)
G20_sync_bfs_messageCount[2],G20_sync_bfs_runtime[2] = sync_bfs.test(G20_2)

G40_sync_bfs_messageCount[0],G40_sync_bfs_runtime[0] = sync_bfs.test(G40_0)
G40_sync_bfs_messageCount[1],G40_sync_bfs_runtime[1] = sync_bfs.test(G40_1)
G40_sync_bfs_messageCount[2],G40_sync_bfs_runtime[2] = sync_bfs.test(G40_2)

G60_sync_bfs_messageCount[0],G60_sync_bfs_runtime[0] = sync_bfs.test(G60_0)
G60_sync_bfs_messageCount[1],G60_sync_bfs_runtime[1] = sync_bfs.test(G60_1)
G60_sync_bfs_messageCount[2],G60_sync_bfs_runtime[2] = sync_bfs.test(G60_2)

G80_sync_bfs_messageCount[0],G80_sync_bfs_runtime[0] = sync_bfs.test(G80_0)
G80_sync_bfs_messageCount[1],G80_sync_bfs_runtime[1] = sync_bfs.test(G80_1)
G80_sync_bfs_messageCount[2],G80_sync_bfs_runtime[2] = sync_bfs.test(G80_2)


avrg_messageCount_sync = [0]*4
avrg_messageCount_sync[0] = (G20_sync_bfs_messageCount[0] + G20_sync_bfs_messageCount[1] + G20_sync_bfs_messageCount[2])//3
avrg_messageCount_sync[1] = (G40_sync_bfs_messageCount[0] + G40_sync_bfs_messageCount[1] + G40_sync_bfs_messageCount[2])//3
avrg_messageCount_sync[2] = (G60_sync_bfs_messageCount[0] + G60_sync_bfs_messageCount[1] + G60_sync_bfs_messageCount[2])//3
avrg_messageCount_sync[3] = (G80_sync_bfs_messageCount[0] + G80_sync_bfs_messageCount[1] + G80_sync_bfs_messageCount[2])//3

avrg_runtime_sync = [0]*4
avrg_runtime_sync[0] = (G20_sync_bfs_runtime[0] + G20_sync_bfs_runtime[1]+G20_sync_bfs_runtime[2])//3
avrg_runtime_sync[1] = (G40_sync_bfs_runtime[0] + G40_sync_bfs_runtime[1]+G40_sync_bfs_runtime[2])//3
avrg_runtime_sync[2] = (G60_sync_bfs_runtime[0] + G60_sync_bfs_runtime[1]+G60_sync_bfs_runtime[2])//3
avrg_runtime_sync[3] = (G80_sync_bfs_runtime[0] + G80_sync_bfs_runtime[1]+G80_sync_bfs_runtime[2])//3
"""

print (G60_sync_bfs_runtime[0],G60_sync_bfs_runtime[1],G60_sync_bfs_runtime[2])
print(avrg_runtime_sync)
"""
plt.figure(1)
plt.subplot(111)
plt.plot(x,avrg_messageCount_async, label = "Async BFS (Ubdate BFS) Algorithm",linestyle='--', marker='o')
plt.plot(x,avrg_messageCount_sync, label = "Sync BFS Algorithm",linestyle='--', marker='o')
plt.legend()
plt.title('Message Counts')
plt.figure(2)
plt.subplot(111)
plt.plot(x,avrg_runtime_async, label = "Async BFS(Ubdate BFS) Algorithm",linestyle='--', marker='o')
plt.plot(x,avrg_runtime_sync, label = "Sync BFS Algorithm",linestyle='--', marker='o')
plt.legend()
plt.title('Runtimes')
plt.show()

