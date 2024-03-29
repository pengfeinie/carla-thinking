# hello world - weather

## 1. Weather

The weather is not a class on its own, but a world setting. However, there is a helper class named [carla.WeatherParameters](https://carla.readthedocs.io/en/0.9.8/python_api/#carla.WeatherParameters) that allows to define a series of visual characteristics such as sun orientation, cloudiness, lightning, wind and much more. The changes can then be applied using the world as the following example does:

```
weather = carla.WeatherParameters(
    cloudiness=80.0,
    precipitation=30.0,
    sun_altitude_angle=70.0)

world.set_weather(weather)

print(world.get_weather())
```

## 2. Hello World Code

```
import carla


try: 
    client = carla.Client("localhost", 2000)
    client.set_timeout(10)
    world = client.get_world()
    maps = client.get_available_maps()
    print(maps)
    world = client.load_world('Town05')
    world = client.load_world('Town04')
    
    weather = carla.WeatherParameters(
    cloudiness=80.0,
    precipitation=30.0,
    sun_altitude_angle=70.0)
    world.set_weather(weather)
    print(world.get_weather())
    
finally:
    print("all cleaned up.")
```

## 3. Run Demonstration

### 3.1 Start Carla Server

Please double click CarlaUE4.exe to start Carla server.

### 3.2 Run Hello World Weather

![](images/2022-08-18_134511.png)

<video width="700" controls>
	<source src="/en/latest/_static/HelloWorld_Weather.mp4" />
</video>
## 4. Dynamic Weather

```
"""
CARLA Dynamic Weather:

Connect to a CARLA Simulator instance and control the weather. Change Sun
position smoothly with time and generate storms occasionally.
"""

import glob
import os
import sys
import carla
import argparse
import math


def clamp(value, minimum=0.0, maximum=100.0):
    return max(minimum, min(value, maximum))


class Sun(object):
    def __init__(self, azimuth, altitude):
        self.azimuth = azimuth
        self.altitude = altitude
        self._t = 0.0

    def tick(self, delta_seconds):
        self._t += 0.008 * delta_seconds
        self._t %= 2.0 * math.pi
        self.azimuth += 0.25 * delta_seconds
        self.azimuth %= 360.0
        self.altitude = (70 * math.sin(self._t)) - 20

    def __str__(self):
        return 'Sun(alt: %.2f, azm: %.2f)' % (self.altitude, self.azimuth)


class Storm(object):
    def __init__(self, precipitation):
        self._t = precipitation if precipitation > 0.0 else -50.0
        self._increasing = True
        self.clouds = 0.0
        self.rain = 0.0
        self.wetness = 0.0
        self.puddles = 0.0
        self.wind = 0.0
        self.fog = 0.0

    def tick(self, delta_seconds):
        delta = (1.3 if self._increasing else -1.3) * delta_seconds
        self._t = clamp(delta + self._t, -250.0, 100.0)
        self.clouds = clamp(self._t + 40.0, 0.0, 90.0)
        self.rain = clamp(self._t, 0.0, 80.0)
        delay = -10.0 if self._increasing else 90.0
        self.puddles = clamp(self._t + delay, 0.0, 85.0)
        self.wetness = clamp(self._t * 5, 0.0, 100.0)
        self.wind = 5.0 if self.clouds <= 20 else 90 if self.clouds >= 70 else 40
        self.fog = clamp(self._t - 10, 0.0, 30.0)
        if self._t == -250.0:
            self._increasing = True
        if self._t == 100.0:
            self._increasing = False

    def __str__(self):
        return 'Storm(clouds=%d%%, rain=%d%%, wind=%d%%)' % (self.clouds, self.rain, self.wind)


class Weather(object):
    def __init__(self, weather):
        self.weather = weather
        self._sun = Sun(weather.sun_azimuth_angle, weather.sun_altitude_angle)
        self._storm = Storm(weather.precipitation)

    def tick(self, delta_seconds):
        self._sun.tick(delta_seconds)
        self._storm.tick(delta_seconds)
        self.weather.cloudiness = self._storm.clouds
        self.weather.precipitation = self._storm.rain
        self.weather.precipitation_deposits = self._storm.puddles
        self.weather.wind_intensity = self._storm.wind
        self.weather.fog_density = self._storm.fog
        self.weather.wetness = self._storm.wetness
        self.weather.sun_azimuth_angle = self._sun.azimuth
        self.weather.sun_altitude_angle = self._sun.altitude

    def __str__(self):
        return '%s %s' % (self._sun, self._storm)


def main():
    argparser = argparse.ArgumentParser(
        description=__doc__)
    argparser.add_argument(
        '--host',
        metavar='H',
        default='127.0.0.1',
        help='IP of the host server (default: 127.0.0.1)')
    argparser.add_argument(
        '-p', '--port',
        metavar='P',
        default=2000,
        type=int,
        help='TCP port to listen to (default: 2000)')
    argparser.add_argument(
        '-s', '--speed',
        metavar='FACTOR',
        default=1.0,
        type=float,
        help='rate at which the weather changes (default: 1.0)')
    args = argparser.parse_args()

    speed_factor = args.speed
    update_freq = 0.1 / speed_factor

    client = carla.Client(args.host, args.port)
    client.set_timeout(2.0)
    world = client.get_world()

    weather = Weather(world.get_weather())

    elapsed_time = 0.0

    while True:
        timestamp = world.wait_for_tick(seconds=30.0).timestamp
        elapsed_time += timestamp.delta_seconds
        if elapsed_time > update_freq:
            weather.tick(speed_factor * elapsed_time)
            world.set_weather(weather.weather)
            sys.stdout.write('\r' + str(weather) + 12 * ' ')
            sys.stdout.flush()
            elapsed_time = 0.0


if __name__ == '__main__':
    main()
```

## 5. Reference

1. [https://carla.org/](https://carla.org/)
2. [https://carla.readthedocs.io/en/0.9.8/start_quickstart/](https://carla.readthedocs.io/en/0.9.8/start_quickstart/)
3. [https://carla.readthedocs.io/en/0.9.8/core_world/](https://carla.readthedocs.io/en/0.9.8/core_world/)
4. [https://carla.readthedocs.io/en/0.9.8/core_world/#weather](https://carla.readthedocs.io/en/0.9.8/core_world/#weather)
