import simpy
import random
import networkx as nx
from distsim import * 
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite

messageCount = 0
runtime = 0
bipart = True # ilk olarak bipartiate true yapıyoruz.

class FNode(Node):
	def __init__(self,*args):
		Node.__init__(self, *args)
		self.msgSent = False
		self.shouldSent = False #bir dahaki rounda mesaj gönderip göndermeyeceğimize dair değişken
		self.childs = []
		self.others = []
		self.parent = None
		self.my_layer = None
		

	def run(self):

		global messageCount
		global runtime
		global bipart

		while True:
			yield self.mailbox.get(1)
			msg = self.receiveMessage()
			print('%d: %s received from %d at time %d' % (self.id,msg['type'],msg['sender'],self.env.now))

			if msg['type'] == "ROUND":
				if self.id == 0 and not self.msgSent: #root her round da mesaj göndermemeli
					runtime = runtime + 1
					self.sendMessage({'type':'PROBE','data':1,'runtime': runtime})
					messageCount = messageCount + len(self.neighbors)
					print('%d probe sending' % self.id)
					self.msgSent = True
				else:
					if self.shouldSent and not self.msgSent:
						for key in self.neighbors:
							if key != self.parent:
								self.sendMessageTo(key,{'type':'PROBE','data':self.my_layer + 1,'runtime':runtime})
								messageCount = messageCount + 1
						print('%d probe sending' % self.id)
						self.msgSent = True #probe mesajı attı bir daha atmayacak.


			elif msg['type'] == "PROBE":
				currentRuntime = msg['runtime'] + 1
				if currentRuntime > runtime:
					runtime = currentRuntime

				if self.parent == None:
					self.parent = msg['sender']
					self.my_layer = msg['data']
					print('%d probe received from soruce %d' %(self.id,msg['sender']))
					self.sendMessageTo(msg['sender'],{'type':'ACK'})
					messageCount = messageCount + 1
					self.shouldSent = True #ben bu round da mesaj aldım bir sonraki rounda da göndermeliyim.
				else :
					#bipartitate olup olmadığını kontrol ediyoruz.
					if self.my_layer + 1 == msg['data']: # benim göndereceğim layer ile bana gelen layer bilgisi eşit ise bipartiate değil.
						bipart = False
					self.sendMessageTo(msg['sender'],{'type':'REJECT'})
					messageCount = messageCount + 1

			elif msg['type'] == "ACK":
				self.childs.append(msg['sender'])

			elif msg['type'] == "REJECT":
				self.others.append(msg['sender'])


#G = nx.path_graph(5);
#G = bipartite.random_graph(5, 7, 0.2)
G = nx.watts_strogatz_graph(5,4,0.9)
sys = System(FNode,nxGraph=G,roundInterval=3) #roundInterval=10 for rounds in 10 time
sys.env.run(30)
print(messageCount)
print(runtime)
print(bipart)
print(nx.is_bipartite(G))
print (nx.diameter(G)+1)
nx.draw_networkx(G)
plt.show()

