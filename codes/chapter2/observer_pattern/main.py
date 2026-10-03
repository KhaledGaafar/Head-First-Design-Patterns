from subject import WeatherData
from observers import CurrentConditionsDisplay

# 1. Create the single Subject instance
weather_data = WeatherData()

# 2. Create the Observer instance (it registers itself automatically inside __init__)
current_display = CurrentConditionsDisplay(weather_data)

# 3. Simulate new measurements
weather_data.set_measurements(temperature=30.8, humidity=0.9, pressure=500.0)
