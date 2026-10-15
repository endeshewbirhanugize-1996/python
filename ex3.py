class ThermostatAgent:
    """Perceives the temperature and chooses an action using condition-action rules."""
    def __init__(self, target: float = 22.0, tolerance: float = 1.0):
        self.target = target
        self.tolerance = tolerance
        self.history = []  # Store every temperature percept
    def act(self, temperature: float) -> str:
        self.history.append(temperature)  # Store the current temperature
        if temperature > self.target + self.tolerance:
            return "COOL"
        if temperature < self.target - self.tolerance:
            return "HEAT"
        return "IDLE"
if __name__ == "__main__":
    agent = ThermostatAgent()
    for percept in [15, 21.5, 22, 27]:
        print(f"Temperature {percept:>5} C -> action: {agent.act(percept)}")
    print("Temperature history:", agent.history)

