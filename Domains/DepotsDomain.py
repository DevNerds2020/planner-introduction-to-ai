from Domains.Domain import Domain
from Model.Action import Action
from Model.Predicate import Predicate

class DepotsDomain(Domain):
    def __init__(self, number_of_crates, number_of_locations, number_of_trucks):
        # Initialize the DepotsDomain object with the given parameters
        self.number_of_crates = number_of_crates
        self.number_of_locations = number_of_locations
        self.number_of_trucks = number_of_trucks

        # Define the object types and their initial values
        self.object_type = {
            "crates": [],       # List to store crate objects
            "locations": [],    # List to store location objects
            "hoists": [],       # List to store hoist objects
            "trucks": [],       # List to store truck objects
            "pallets": [],      # List to store pallet objects
        }

        self.facts = []        # List to store facts about the objects

        # Define the objects and actions for the domain
        self.define_objects()
        self.define_actions()

    def define_objects(self):
        # Define the crates
        for i in range(1, self.number_of_crates + 1):
            crate_string = f"Crate{i}"
            self.object_type["crates"].append(crate_string)

        # Define the locations, hoists, and pallets
        for i in range(1, self.number_of_locations + 1):
            location_string = f"Location{i}"
            hoist_string = f"Hoist{i}"
            pallet_string = f"Pallet{i}"

            self.object_type["locations"].append(location_string)
            self.object_type["hoists"].append(hoist_string)
            self.object_type["pallets"].append(pallet_string)

            # Add facts about the hoist and pallet locations
            at_hoist_location = Predicate("At", [hoist_string, location_string])
            at_pallet_location = Predicate("At", [pallet_string, location_string])

            self.facts.append(at_hoist_location)
            self.facts.append(at_pallet_location)

        # Define the trucks
        for i in range(1, self.number_of_trucks + 1):
            truck_string = f"Truck{i}"
            self.object_type["trucks"].append(truck_string)

    def define_actions(self):
        # Define different types of actions for the domain
        self.define_drive_actions()
        self.define_lift_actions()
        self.define_drop_actions()
        self.define_load_actions()
        self.define_unload_actions()

    def define_drive_actions(self):
        # Define drive actions for each truck to move between locations
        for truck in self.object_type["trucks"]:
            for location_1 in self.object_type["locations"]:
                for location_2 in self.object_type["locations"]:
                    if location_1 != location_2:
                        self.add_drive_action(truck, location_1, location_2)

    def define_lift_actions(self):
        # Define lift actions for each hoist to lift crates and pallets
        for hoist in self.object_type["hoists"]:
            for crate in self.object_type["crates"]:
                for surface in self.object_type["crates"]:
                    if crate == surface:
                        continue
                    for location in self.object_type["locations"]:
                        self.add_lift_action(hoist, crate, surface, location)

                for surface in self.object_type["pallets"]:
                    for location in self.object_type["locations"]:
                        self.add_lift_action(hoist, crate, surface, location)

    def define_drop_actions(self):
        # Define drop actions for each hoist to drop crates and pallets
        for hoist in self.object_type["hoists"]:
            for crate in self.object_type["crates"]:
                for surface in self.object_type["crates"]:
                    if crate == surface:
                        continue
                    for location in self.object_type["locations"]:
                        self.add_drop_action(hoist, crate, surface, location)

                for surface in self.object_type["pallets"]:
                    for location in self.object_type["locations"]:
                        self.add_drop_action(hoist, crate, surface, location)

    def define_load_actions(self):
        # Define load actions for each truck to load crates and pallets
        for truck in self.object_type["trucks"]:
            for crate in self.object_type["crates"]:
                for location in self.object_type["locations"]:
                    for surface in self.object_type["crates"]:
                        if crate == surface:
                            continue
                        self.add_load_action(truck, crate, surface, location)

                for surface in self.object_type["pallets"]:
                    self.add_load_action(truck, crate, surface, location)

    def define_unload_actions(self):
        # Define unload actions for each truck to unload crates and pallets
        for truck in self.object_type["trucks"]:
            for crate in self.object_type["crates"]:
                for location in self.object_type["locations"]:
                    for surface in self.object_type["crates"]:
                        if crate == surface:
                            continue
                        self.add_unload_action(truck, crate, surface, location)

                for surface in self.object_type["pallets"]:
                    self.add_unload_action(truck, crate, surface, location)

    def add_drive_action(self, truck, location_1, location_2):
        # Add a drive action for a truck to move between two locations
        drive_action_name = "Drive(" + truck + ", " + location_1 + ", " + location_2 + ")"
        at_truck_location_1 = Predicate("At", [truck, location_1])
        at_truck_location_2 = Predicate("At", [truck, location_2])
        drive_action = Action(
            drive_action_name,
            [at_truck_location_1],
            [],
            [at_truck_location_2],
            [at_truck_location_1],
        )
        self.actions.append(drive_action)

    def add_lift_action(self, hoist, crate, surface, location):
        # Add a lift action for a hoist to lift a crate or pallet
        lift_action_name = "Lift(" + hoist + ", " + crate + ", " + surface + ", " + location + ")"

        at_hoist_location = Predicate("At", [hoist, location])
        available_hoist = Predicate("Available", [hoist])
        at_crate_location = Predicate("At", [crate, location])
        on_crate_surface = Predicate("On", [crate, surface])
        clear_crate = Predicate("Clear", [crate])
        clear_surface = Predicate("Clear", [surface])
        lifting_hoist_crate = Predicate("Lifting", [hoist, crate])

        lift_action = Action(
            lift_action_name,
            [at_hoist_location, available_hoist, at_crate_location, clear_crate],
            [],
            [lifting_hoist_crate, clear_surface],
            [at_crate_location, clear_crate, available_hoist, on_crate_surface],
        )

        self.actions.append(lift_action)

    def add_drop_action(self, hoist, crate, surface, location):
        # Add a drop action for a hoist to drop a crate or pallet
        drop_action_name = "Drop(" + hoist + ", " + crate + ", " + surface + ", " + location + ")"

        at_hoist_location = Predicate("At", [hoist, location])
        at_surface_location = Predicate("At", [surface, location])
        clear_surface = Predicate("Clear", [surface])
        lifting_hoist_crate = Predicate("Lifting", [hoist, crate])
        available_hoist = Predicate("Available", [hoist])
        at_crate_location = Predicate("At", [crate, location])
        clear_crate = Predicate("Clear", [crate])
        on_crate_surface = Predicate("On", [crate, surface])

        drop_action = Action(
            drop_action_name,
            [
                at_hoist_location,
                at_surface_location,
                clear_surface,
                lifting_hoist_crate,
            ],
            [],
            [available_hoist, at_crate_location, clear_crate, on_crate_surface],
            [lifting_hoist_crate, clear_surface],
        )

        self.actions.append(drop_action)

    def add_load_action(self, hoist, crate, truck, location):
        # Add a load action for a truck to load a crate or pallet
        load_action_name = "Load(" + hoist + ", " + crate + ", " + truck + ", " + location + ")"

        at_hoist_location = Predicate("At", [hoist, location])
        at_truck_location = Predicate("At", [truck, location])
        lifting_hoist_crate = Predicate("Lifting", [hoist, crate])
        in_crate_truck = Predicate("In", [crate, truck])
        available_hoist = Predicate("Available", [hoist])

        load_action = Action(
            load_action_name,
            [at_hoist_location, at_truck_location, lifting_hoist_crate],
            [],
            [in_crate_truck, available_hoist],
            [lifting_hoist_crate],
        )

        self.actions.append(load_action)

    def add_unload_action(self, hoist, crate, truck, location):
        # Add an unload action for a truck to unload a crate or pallet
        unload_action_name = "Unload(" + hoist + ", " + crate + ", " + truck + ", " + location + ")"

        at_hoist_location = Predicate("At", [hoist, location])
        at_truck_location = Predicate("At", [truck, location])
        available_hoist = Predicate("Available", [hoist])
        in_crate_truck = Predicate("In", [crate, truck])
        lifting_hoist_crate = Predicate("Lifting", [hoist, crate])

        unload_action = Action(
            unload_action_name,
            [at_hoist_location, at_truck_location, available_hoist, in_crate_truck],
            [],
            [lifting_hoist_crate],
            [in_crate_truck, available_hoist],
        )

        self.actions.append(unload_action)