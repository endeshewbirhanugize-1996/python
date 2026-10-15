
class ThermostatAgent:
    """A thermostat agent that stores percept history and selects actions."""
    def __init__(self, target: float = 20.0, tolerance: float = 2.0):
        self.target = target
        self.tolerance = tolerance
        self.history = []  # Store every temperature percept

    def act(self, temperature: float) -> str:
        # Store the current temperature
        self.history.append(temperature)
        # Rule 1: Alarm for dangerous temperatures
        if temperature > 40:
            return "ALARM"
        # Rule 2: Cool if the temperature is too high
        if temperature > self.target + self.tolerance:
            return "COOL"

        # Rule 3: Heat if the temperature is too low
        if temperature < self.target - self.tolerance:
            return "HEAT"

        # Rule 4: Otherwise, do nothing
        return "IDLE"
if __name__ == "__main__":
    agent = ThermostatAgent()

    temperatures = [15, 18, 20, 22, 27, 41]

    for percept in temperatures:
        print(
            f"Temperature {percept:>5} C -> "
            f"action: {agent.act(percept)}"
        )

    print("\nTemperature history:", agent.history)