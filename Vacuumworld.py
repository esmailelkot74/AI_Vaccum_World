class VacuumWorld:
    def __init__(self, agent_location, location_status):
        self.location_status = location_status
        self.agent_location = agent_location

    def is_location_clean(self, location):
        return self.location_status[location] == 'Clean'

    def clean_location(self, location):
        self.location_status[location] = 'Clean'

    def move_right(self):
        self.agent_location = 'B'

    def move_left(self):
        self.agent_location = 'A'

    def suck_dirt(self):
        self.location_status[self.agent_location] = 'Clean'

    def print_environment(self):
        print(f"Agent Location: {self.agent_location}")
        for location, status in self.location_status.items():
            print(f"Location {location}: {status}")

    def decide_action(self):
        if self.location_status[self.agent_location] == 'Dirty':
            return 'Suck'
        elif self.agent_location == 'A':
            return 'Right'
        else:
            return 'Left'

    def run_simulation(self):
        action_taken = False
        while not self.is_location_clean('A') or not self.is_location_clean('B'):
            self.print_environment()
            action = self.decide_action()
            print(f"Action: {action}")
            if action == 'Suck':
                self.suck_dirt()
                action_taken = True
            elif action == 'Right':
                self.move_right()
                action_taken = True
            elif action == 'Left':
                self.move_left()
                action_taken = True

        if not action_taken:
            print("No action more {'A' and 'B' are Clean}")

# Get initial state from user input
def get_initial_state():
    agent_location = input("Enter Agent Location (A/B): ").upper()
    while agent_location not in ['A', 'B']:
        print("Please enter 'A' or 'B' for Agent Location.")
        agent_location = input("Enter Agent Location (A/B): ").upper()

    location_a = input("Enter Location A (Dirty/Clean): ").capitalize()
    while location_a not in ['Dirty', 'Clean']:
        print("Please enter 'Dirty' or 'Clean' for Location A.")
        location_a = input("Enter Location A (Dirty/Clean): ").capitalize()

    location_b = input("Enter Location B (Dirty/Clean): ").capitalize()
    while location_b not in ['Dirty', 'Clean']:
        print("Please enter 'Dirty' or 'Clean' for Location B.")
        location_b = input("Enter Location B (Dirty/Clean): ").capitalize()

    location_status = {'A': location_a, 'B': location_b}
    return agent_location, location_status


# Create and run simulation for two agents
def run_simulation_for_two_agents():
    for _ in range(2):
        agent_location, location_status = get_initial_state()
        env = VacuumWorld(agent_location, location_status)
        print("Simple Reflex Agent:")
        env.run_simulation()
        print()

# Run simulation for two agents
run_simulation_for_two_agents()
