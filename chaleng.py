
class ThermostatAgent:
    """Thermostat agent that considers temperature and electricity price."""

    def __init__(self, target=22.0, tolerance=1.0):
        self.target = target
        self.tolerance = tolerance
    def act(self, temperature, electricity_price):
        # Adjust tolerance based on electricity price
        if electricity_price == "expensive":
            tolerance = 3
        elif electricity_price == "cheap":
            tolerance = 1
        else:
            raise ValueError("Price must be cheap or expensive")
        # Choose an action
        if temperature > self.target + tolerance:
            return "COOL"
        elif temperature < self.target - tolerance:
            return "HEAT"
        else:
            return "IDLE"
# Create the thermostat agent
agent = ThermostatAgent(target=22)
# Test different temperatures and electricity prices
tests = [
    (20, "cheap"),
    (20, "expensive"),
    (18, "expensive"),
    (27, "expensive"),
    (25, "cheap")
]
for temperature, price in tests:
    action = agent.act(temperature, price)
    print(f"Temperature: {temperature}°C, "
          f"Electricity: {price} -> Action: {action}")