from __future__ import annotations
from wardrobe import Component
from typing import List

class OutfitComposite(Component):
    def __init__(self):
        self._children: List[Component] = []
        self._parent: Component = None

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"OutfitComposite({'+'.join(results)})"
