"""
	Composite
	- a structural design pattern that lets you compose objects into tree structures
	and then work with these structures as if they were individual objects.
"""
import abc

class Wardrobe(abc.ABC): # Abstract Component
	def add(self, child):
		pass

	def remove(self, child):
		pass

	def is_composite(self):
		return False

	@abc.abstractmethod
	def execute(self):
		pass


class Clothe(Wardrobe): # Leaf
	def __init__(self, name):
		self.name = name

	def execute(self):
		print(f'Clothe: {self.name}')


class OutfitComposite(Wardrobe): # Concrete Composite
	def __init__(self):
		self._children = []

	def add(self, child):
		self._children.append(child)

	def remove(self, child):
		self._children.remove(child)

	def is_composite(self):
		return True

	def execute(self):
		print('Outfit Composite')

		for child in self._children:
			child.execute()


class Shoes(OutfitComposite): # Leaf
	def __init__(self, name):
		self.name = name

	def is_composite(self):
		return False

	def execute(self):
		print(f'\tShoes: {self.name}')


class Jacket(OutfitComposite): # Leaf
	def __init__(self, name):
		self.name = name

	def is_composite(self):
		return False

	def execute(self):
		print(f'\tJacket: {self.name}')


def client_composite():
	shoes1 = Shoes('Sport Shoes')
	shoes2 = Shoes('Boots')
	jacket1 = Jacket('Winter Jacket')

	outfit = OutfitComposite()
	outfit.add(shoes1)
	outfit.add(shoes2)
	outfit.add(jacket1)

	outfit.execute()


client_composite()