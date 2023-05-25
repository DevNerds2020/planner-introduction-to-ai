from Model.Action import Action

class Domain:
    def __init__(self, name: str):
        # Initializes a new instance of the Domain class with a given name
        self.name = name
        self.actions = []

    def get_name(self) -> str:
        # Returns the name of the domain
        return self.name

    def get_actions(self) -> list[Action]:
        # Returns the list of actions defined in the domain
        return self.actions
