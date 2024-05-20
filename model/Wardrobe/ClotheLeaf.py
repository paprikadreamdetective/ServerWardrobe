from __future__ import annotations
from wardrobe import Component

class ClotheLeaf(Component):
    def __init__(self, name: str):
        self._name = name
        self._parent: Component = None

    @property
    def name(self) -> str:
        return self._name

    def operation(self) -> str:
        return self._name

# Optional: Helper function to create leaves
def create_clothe(name: str) -> ClotheLeaf:
    return ClotheLeaf(name)
