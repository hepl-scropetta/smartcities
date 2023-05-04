import utime
import os
from machine import I2C, Pin
from dht import DHT11

SENSOR = DHT11(Pin(18))

# Create a header row for the CSV file
header = "Timestamp,Temperature\n"

filename = "temperatures.csv"
# create new file if it doesn't exist
if filename not in os.listdir():
    with open(filename, 'w') as f:
        f.write(header)

# Open the CSV file in write mode
with open(filename, "a") as f:
    f.write(header)

    # Write temperature data to the file every 10 seconds
    while True:
        # Get the current timestamp and temperature
        timestamp = utime.localtime()
        print(timestamp)
        SENSOR.measure()
        temperature = SENSOR.temperature()
        print("{:.2f}".format(temperature))

        # Format the timestamp and temperature as strings
        timestamp_str = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(*timestamp)
        temperature_str = "{:.2f}".format(temperature)

        # Write the timestamp and temperature to the CSV file
        line = "{},{}\n".format(timestamp_str, temperature_str)
        f.write(line)

        # Wait for 10 seconds
        utime.sleep(1)
