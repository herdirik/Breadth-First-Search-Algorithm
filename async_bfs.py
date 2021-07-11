import simpy
import random
import networkx as nx
from distsim import * 
import matplotlib.pyplot as plt


messageCount = 0
firstTime = None
lastTime = 0

class FNode(Node):
	def __init__(self,*args):
		Node.__init__(self, *args)
		#self.msgSent = False
		self.parent= None
		self.childs=[] # node çocuklerını tutacak
		self.others=[] # node çocuğu olmayan diğer nodeları tutacak.
		self.my_layer = None
		# message type LAYER, ACK, REJECT

	def run(self):
		global messageCount
		global firstTime
		global lastTime

		if self.id == 0:
			self.setTimer('timer1',2)

		while True:
			yield self.mailbox.get(1)
			msg = self.receiveMessage()
			print('%d: %s received from %d at time %d' % (self.id,msg['type'],msg['sender'],self.env.now))

			if firstTime == None:
				firstTime = self.env.now
			lastTime = self.env.now


			if msg['type'] == "LAYER":
				data = msg['data']
				if self.parent == None:
					self.parent = msg['sender']
					self.my_layer = data
					self.sendMessageTo(msg['sender'],{'type':'ACK'}) #parent ına ack mesajı gönderiyor.
					messageCount = messageCount + 1
					childs_layer = data + 1
					print('Hi, I am node %d and my layer %d' %(self.id,self.my_layer))
					for key in self.neighbors:
						if key != self.parent:
							self.sendMessageTo(key,{'type':'LAYER','data':childs_layer})
							messageCount = messageCount + 1

				elif self.parent != None and self.my_layer > data:
					#data = msg['data']
					print (' I am %d node my_layer updating...')
					self.parent = msg['sender']
					self.my_layer = data
					self.sendMessageTo(msg['sender'],{'type':'ACK'})
					messageCount = messageCount + 1
					childs_layer = data + 1
					print('Hi, I am node %d and my layer %d' %(self.id,self.my_layer))
					for key in self.neighbors:
						if key != self.parent:
							self.sendMessageTo(key,{'type':'LAYER','data':childs_layer})
							messageCount = messageCount + 1


				else :
					self.sendMessageTo(msg['sender'],{'type':'REJECT'})
					messageCount = messageCount + 1

			elif msg['type'] == "ACK":
				for other in self.others:
					if other == msg['sender']:
						self.others.remove(other)
				self.childs.append(msg['sender'])

			elif msg['type'] == "REJECT":
				for child in self.childs:
					if child == msg['sender']:
						self.childs.remove(msg['sender'])
				self.others.append(msg['sender'])

			elif msg['type'] == "TIMEOUT":
				if msg['name'] == 'timer1':
					if self.id == 0: 
						self.sendMessage({'type':'LAYER','data':1})
						messageCount = messageCount + len(self.neighbors)
						#self.msgSent = True
"""
G = nx.path_graph(5);
#G=nx.watts_strogatz_graph(20,4,0.9)
sys = System(FNode,nxGraph=G) 
sys.env.run(100)
print (messageCount)
print (lastTime - firstTime)
print(nx.diameter(G))

nx.draw_networkx(G)
plt.show()
"""

def test(G):
	global messageCount
	global firstTime
	global lastTime

	messageCount = 0
	firstTime = None
	lastTime = 0
	#G = nx.watts_strogatz_graph(nodeCount,4,0.9)
	sys = System(FNode,nxGraph=G) 
	sys.env.run(2000)
	
	return messageCount, lastTime - firstTime
