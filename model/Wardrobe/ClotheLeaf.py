from composite import Composite

class OutfitComposite(Composite):
    def operation(self) -> str:
        """
        The Composite executes its primary logic in a particular way. It
        traverses recursively through all its children, collecting and summing
        their results. Since the composite's children pass these calls to their
        children and so forth, the whole object tree is traversed as a result.
        """
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"OutfitComposite({'+'.join(results)})"
