class Node:

	def __init__(self, label):
		self.label = label
		self.left = None
		self.right = None

	def getLabel(self):
		return self.label

	def setLabel(self, label):
		self.label = label

	def getLeft(self):
		return self.left

	def setLeft(self, left):
		self.left = left

	def getRight(self):
		return self.right

	def setRight(self, right):
		self.right = right

class BinarySearchTree:

	def __init__(self):
		self.root = None

	def insert(self, label):

		# cria um novo nÃ³
		node = Node(label)

		# verifica se a Ã¡rvore estÃ¡ vazia
		if self.empty():
			self.root = node
		else:

			# Ã¡rvore nÃ£o vazia, insere recursivamente

			dad_node = None
			curr_node = self.root

			while True:

				if curr_node != None:

					dad_node = curr_node

					# verifica se vai para esquerda ou direita
					if node.getLabel() < curr_node.getLabel():
						# vai para esquerda
						curr_node = curr_node.getLeft()
					else:
						# vai para direita
						curr_node = curr_node.getRight()
				else:

					# se curr_node Ã© None, entÃ£o encontrou onde inserir

					if node.getLabel() < dad_node.getLabel():
						dad_node.setLeft(node)
					else:
						dad_node.setRight(node)

					break # sai do loop

	def empty(self):
		if self.root == None:
			return True
		return False

	# mostra em prÃ©-ordem (raiz-esq-dir)
	def show(self, curr_node):

		if curr_node != None:
			print('%d' % curr_node.getLabel(), end=' ')
			self.show(curr_node.getLeft())
			self.show(curr_node.getRight())

	def getRoot(self):
		return self.root

	def remove(self, label):
		'''
			3 casos

			Caso 1
			o nÃ³ a ser removido nÃ£o tem filhos
			esse caso Ã© simples, basta setar a ligaÃ§Ã£o
			do pai para None

			Caso 2
			o nÃ³ a ser removido tem somente 1 filho
			basta colocar o seu filho no lugar dele

			Caso 3
			o nÃ³ a ser removido possui dois filhos
			basta pegar o menor elemento da subÃ¡rvore Ã  direita
		'''

		dad_node = None # parent
		curr_node = self.root

		while curr_node != None:

			# verifica se encontrou o nÃ³ a ser removido
			if label == curr_node.getLabel():

				# caso 1: o nÃ³ a ser removido nÃ£o possui filhos (nÃ³ folha)
				if curr_node.getLeft() == None and curr_node.getRight() == None:

					# verifica se Ã© a raiz
					if dad_node == None:
						self.root = None
					else:
						# verifica se Ã© filho Ã  esquerda ou Ã  direita
						if dad_node.getLeft() == curr_node:
							dad_node.setLeft(None)
						elif dad_node.getRight() == curr_node:
							dad_node.setRight(None)

				# caso 2: o nÃ³ a ser removido possui somente um filho
				elif (curr_node.getLeft() == None and curr_node.getRight() != None) or \
					(curr_node.getLeft() != None and curr_node.getRight() == None):

					# verifica se o nÃ³ a ser removido Ã© a raiz
					if dad_node == None:
						# verifica se o filho de curr_node Ã© filho Ã  esquerda
						if curr_node.getLeft() != None:
							self.root = curr_node.getLeft()
						else: # senÃ£o o filho de curr_node Ã© filho Ã  direita
							self.root = curr_node.getRight()
					else:
						# verifica se o filho de curr_node Ã© filho Ã  esquerda
						if curr_node.getLeft() != None:
							# verifica se curr_node Ã© filho Ã  esquerda
							if dad_node.getLeft() and dad_node.getLeft().getLabel() == curr_node.getLabel():
								dad_node.setLeft(curr_node.getLeft())
							else: # senÃ£o curr_node Ã© filho Ã  direita
								dad_node.setRight(curr_node.getLeft())
						else: # senÃ£o o filho de curr_node Ã© filho Ã  direita
							# verifica se curr_node Ã© filho Ã  esquerda
							if dad_node.getLeft() and dad_node.getLeft().getLabel() == curr_node.getLabel():
								dad_node.setLeft(curr_node.getRight())
							else: # senÃ£o curr_node Ã© filho Ã  direita
								dad_node.setRight(curr_node.getRight())

				# caso 3: o nÃ³ a ser removido possui dois filhos
				# pega-se o menor elemento da subÃ¡rvore Ã  direita
				elif curr_node.getLeft() != None and curr_node.getRight() != None:

					dad_smaller_node = curr_node
					smaller_node = curr_node.getRight()
					next_smaller = curr_node.getRight().getLeft()

					while next_smaller != None:
						dad_smaller_node = smaller_node
						smaller_node = next_smaller
						next_smaller = smaller_node.getLeft()

					# verifica se o nÃ³ a ser removido Ã© a raiz
					if dad_node == None:

						# Caso especial: o nÃ³ que vai ser a nova raiz Ã© filho da raiz
						if self.root.getRight().getLabel() == smaller_node.getLabel():
							smaller_node.setLeft(self.root.getLeft())
						else:

							'''
								verifica se o smaller_node Ã© filho Ã  esquerda ou Ã  direita
								para setar para None o smaller_node
							'''
							if dad_smaller_node.getLeft() and \
								dad_smaller_node.getLeft().getLabel() == smaller_node.getLabel():
								dad_smaller_node.setLeft(None)
							else:
								dad_smaller_node.setRight(None)

							# seta os filhos Ã  direita e esquerda de smaller_node
							smaller_node.setLeft(curr_node.getLeft())
							smaller_node.setRight(curr_node.getRight())

						# faz com que o smaller_node seja a raiz
						self.root = smaller_node

					else:

						'''
							verifica se curr_node Ã© filho Ã  esquerda ou Ã  direita
							para setar o smaller_node como filho do pai do curr_node (dad_node)
						'''
						if dad_node.getLeft() and dad_node.getLeft().getLabel() == curr_node.getLabel():
							dad_node.setLeft(smaller_node)
						else:
							dad_node.setRight(smaller_node)

						'''
							verifica se o smaller_node Ã© filho Ã  esquerda ou Ã  direita
							para setar para None o smaller_node
						'''
						if dad_smaller_node.getLeft() and \
							dad_smaller_node.getLeft().getLabel() == smaller_node.getLabel():
							dad_smaller_node.setLeft(None)
						else:
							dad_smaller_node.setRight(None)

						# seta os filhos Ã  direita e esquerda de smaller_node
						smaller_node.setLeft(curr_node.getLeft())
						smaller_node.setRight(curr_node.getRight())

				break # sai do loop

			dad_node = curr_node

			# verifica se vai para esquerda ou direita
			if label < curr_node.getLabel():
				# vai para esquerda
				curr_node = curr_node.getLeft()
			else:
				# vai para direita
				curr_node = curr_node.getRight()


t = BinarySearchTree()
t.insert(8)
t.insert(3)
t.insert(1)
t.insert(6)
t.insert(4)
t.insert(7)
t.insert(10)
t.insert(14)
t.insert(13)
t.insert(9)

t.remove(8)

t.show(t.getRoot())