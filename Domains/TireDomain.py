from Domains.Domain import Domain
from Model.Action import Action
from Model.Predicate import Predicate


class TireDomain(Domain):
    def __init__(self):
        # Initialize name, object types and actions for the domain
        self.name = "Tire Domain"
        self.object_type = {"tires": [], "locations": []}
        self.actions = []
        
        # Define the possible objects in the domain (tires and locations)
        self.define_objects()
        # Define the available actions in the domain
        self.define_actions()

    def define_objects(self):
        # Add two types of tires and two locations to the domain
        self.object_type["tires"].append("Flat")
        self.object_type["tires"].append("Spare")
        self.object_type["locations"].append("Axle")
        self.object_type["locations"].append("Trunk")

    def define_actions(self):
        # Define the actions that can be performed in the domain
        other = {"Flat": "Spare", "Spare": "Flat"}

        # For each tire type, create remove and put actions for each location
        for tire in self.object_type["tires"]:
            # Define predicate for tire being on ground
            at_tire_ground = Predicate(
                "At",
                [tire, "Ground"],
            )
            
            # For each location, create remove and put action
            for location in self.object_type["locations"]:
                # Define action names
                remove_action_name = f"Remove({tire}, {location})"
                put_action_name = f"Put({tire}, {location})"
                
                # Define predicates for current tire being at its location and the other tire being at the same location
                at_tire_location = Predicate(
                    "At",
                    [tire, location],
                )
                at_other_location = Predicate(
                    "At",
                    [other[tire], location],
                )

                # Define remove and put actions for current tire at the current location
                # Remove action removes the tire from its location and puts it on ground
                remove_action = Action(
                    remove_action_name,
                    [at_tire_location],
                    [],
                    [at_tire_ground],
                    [at_tire_location],
                )
                # Put action puts the tire back to its location and moves the other tire to the same location
                put_action = Action(
                    put_action_name,
                    [at_tire_ground],
                    [at_other_location],
                    [at_tire_location],
                    [at_tire_ground],
                )

                # Add remove and put actions to the list of available actions in the domain
                self.actions.append(remove_action)
                self.actions.append(put_action)