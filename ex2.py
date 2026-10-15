class ThermostatAgent:
    def __init__(self, target=22.0, tolerance=1.0):
        self.target = target
        self.tolerance = tolerance

    def act(self, temperature):
        if temperature > 40:
            return "ALARM"
        elif temperature > self.target + self.tolerance:
            return "COOL"
        elif temperature < self.target - self.tolerance:
            return "HEAT"
        else:
            return "IDLE"

if __name__ == "__main__":
    agent = ThermostatAgent()

    for temperature in [15, 22, 27, 41]:
        print(
            f"Temperature {temperature:>5} C -> "
            f"action: {agent.act(temperature)}"
        )