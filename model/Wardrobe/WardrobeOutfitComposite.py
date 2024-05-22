from .Wardrobe import Wardrobe

class WardrobeOutfitComposite(Wardrobe): # Concrete Composite
	def __init__(self):
		self._children = []

	def add(self, child):
		self._children.append(child)

	def remove(self, child):
		self._children.remove(child)

	def is_composite(self):
		return True

	def execute(self):
		print('Wardrobe Outfit Composite')
		for child in self._children:
			print(child.wear())
		
