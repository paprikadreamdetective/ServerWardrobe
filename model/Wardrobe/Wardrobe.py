
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
