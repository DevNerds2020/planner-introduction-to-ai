class Predicate:
    def __init__(self, name: str, objects: list[str]):
        # Initialize a Predicate object
        self.name = name  # Set the name of the predicate
        self.objects = objects  # Set the list of objects associated with the predicate

    def get_name(self) -> str:
        # Get the name of the predicate
        return self.name

    def get_objects(self) -> list[str]:
        # Get the list of objects associated with the predicate
        return self.objects

    def __hash__(self) -> int:
        # Compute the hash value of the Predicate object
        result = 0
        PRIME = 1073741789  # A prime number for hashing
        result += self.name.__hash__() % PRIME  # Hash the name of the predicate

        # Hash each object in the list of objects
        for obj in self.objects:
            result = (result + (obj.__hash__() % PRIME)) % PRIME

        return result

    def __eq__(self, other) -> bool:
        # Check if two Predicate objects are equal
        if self.name != other.get_name():
            return False

        if self.__hash__() != other.__hash__():
            return False

        return self.objects == other.get_objects()

    def __ne__(self, other):
        # Check if two Predicate objects are not equal
        return not self.__eq__(other)

    def __lt__(self, other):
        # Compare two Predicate objects for less than
        if self.name != other.get_name():
            return self.name < other.get_name()

        return self.objects < other.get_objects()

    def __gt__(self, other):
        # Compare two Predicate objects for greater than
        if self.name != other.get_name():
            return self.name > other.get_name()

        return self.objects > other.get_objects()

    def __str__(self) -> str:
        # Get the string representation of the Predicate object
        return self.name + "(" + ",".join(self.objects) + ")"
