import random

class WeatherSimulator:
    def init(self):
        self.weather_states = ["Sunny", "Cloudy", "Rainy", "Stormy", "Snowy"]
        self.current_weather = random.choice(self.weather_states)

    def simulate_weather(self):
        print(f"Initial weather: {self.current_weather}")
        for _ in range(10):
            change = random.randint(-1, 1)
            index = (self.weather_states.index(self.current_weather) + change) % len(self.weather_states)
            self.current_weather = self.weather_states[index]
            print(f"New weather: {self.current_weather}")

class ClimateControl:
    def init(self):
        self.simulator = WeatherSimulator()

    def run_simulation(self):
        action = input("Do you want to run the weather simulation? (yes/no): ")
        if action == "yes":
            self.simulator.simulate_weather()
        else:
            print("Simulation aborted!")

def main():
    control = ClimateControl()
    while True:
        control.run_simulation()
        repeat = input("Do you want to run the simulation again? (yes/no): ")
        if repeat != "yes":
            break

if name == "main":
    main()
