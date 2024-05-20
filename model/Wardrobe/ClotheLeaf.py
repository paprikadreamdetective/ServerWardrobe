from composite import Leaf

class ClotheLeaf(Leaf):
    def __init__(self, name: str):
        self._name = name

    def operation(self) -> str:
        return self._name

# Optional: Helper function to create leaves
def create_clothe(name: str) -> ClotheLeaf:
    return ClotheLeaf(name)
