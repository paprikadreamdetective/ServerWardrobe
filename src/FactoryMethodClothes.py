"""
Factory Method Design Pattern

Intent: Provides an interface for creating objects in a superclass, but allows
subclasses to alter the type of objects that will be created.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from ultralytics import YOLO
from rembg import remove


model = YOLO('model/clothes_classification.pt')


class Creator(ABC):
    """
    The Creator class declares the factory method that is supposed to return an
    object of a Product class. The Creator's subclasses usually provide the
    implementation of this method.
    """

    @abstractmethod
    def factory_method(self):
        """
        Note that the Creator may also provide some default implementation of
        the factory method.
        """
        pass

    def some_operation(self) -> str:
        """
        Also note that, despite its name, the Creator's primary responsibility
        is not creating products. Usually, it contains some core business logic
        that relies on Product objects, returned by the factory method.
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of product from it.
        """

        # Call the factory method to create a Product object.
        product = self.factory_method()

        # Now, use the product.
        result = f"Creator: The same creator's code has just worked with {product.operation()}"

        return result


"""
Concrete Creators override the factory method in order to change the resulting
product's type.
"""


class ConcreteCreator1(Creator):
    """
    Note that the signature of the method still uses the abstract product type,
    even though the concrete product is actually returned from the method. This
    way the Creator can stay independent of concrete product classes.
    """

    def factory_method(self) -> Clothe:
        return ConcreteButtomClothe()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Clothe:
        return ConcreteProduct2()


class Clothe(ABC):
    """
    The Product interface declares the operations that all concrete products
    must implement.
    """

    def remove_backgroud_images(self, input_image, output_image):
        if input_image.endswith(('.png', 'jpg', 'jpeg')):
            with open(input_image, 'rb') as inp, open(output_image, 'wb') as outp:
                backgroud_output = remove(inp.read())
                outp.write(backgroud_output)
        else:
            print("The file is not valid")

    def do_detection(self, image) -> str:
        results = model(image, verbose=False)
        for r in results:
            probs = r.probs  # Probs object for classification outputs
            names = r.names
            clothe = probs.top1

        clothing_detected = names[clothe]
        return clothing_detected

    @abstractmethod
    def do_classification(self, image):
        pass


"""
Concrete Products provide various implementations of the Product interface.
"""


class ConcreteButtomClothe(Clothe):
    def do_classification(self, image):
        clothe_type = super().do_detection(image)
        if clothe_type == "shorts" or "skirt" or "pants":
            return "bottom"
        else:
            return "not bottom"


class ConcreteProduct2(Clothe):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


def client_code(creator: Creator) -> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long as the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """

    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())
