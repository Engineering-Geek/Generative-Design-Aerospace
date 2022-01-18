from typing import List, Union, Tuple
import numpy as np
import gym
from gym import spaces

class WindTunnel:
    def __init__(self, parcel_dimensions: List[float], environment_dimensions: List[int], initial_temp: float = 298.15, wind_velocity: float = 30.0) -> None:
        """
        This is the core environment of the simulation, and in this specific case, a wind tunnel

        Args:
            parcel_dimensions (List[float, float, float]): dimensions of each fluid parcel in meters [x, y, z]
            environment_dimensions (List[int, int, int]): number of fluid parcels in each direction [x, y, z]
            initial_temp (float): surrounding environment temperature in kelvin
            air_velocity (float): speed in the wind tunnel in meters per second
        """
        # X Y Z component of acceleration and velocity at parcel location x y z
        self.acceleration_tensor = np.array([
            np.array(np.array([0, 0, 0]) * environment_dimensions[0]),
            np.array(np.array([0, 0, 0]) * environment_dimensions[1]),
            np.array(np.array([0, 0, 0]) * environment_dimensions[2])
        ])
        self.velocity_tensor = np.array([
            np.array(np.array([0, 0, 0]) * environment_dimensions[0]),
            np.array(np.array([0, 0, 0]) * environment_dimensions[1]),
            np.array(np.array([0, 0, 0]) * environment_dimensions[2])
        ])

        self.temperature_tensor = np.array([
            np.array([initial_temp] * environment_dimensions[0]),
            np.array([initial_temp] * environment_dimensions[1]),
            np.array([initial_temp] * environment_dimensions[2])
        ])
        self.wind_velocity = wind_velocity
        
        # 1m x 1m x 1m cube
    
    def _iterate(self):
        # Apply heat and fluid differential equations
        pass
    
    def calculate(self) -> Tuple[Tuple[np.float, np.float, np.float], Tuple[np.float, np.float, np.float]]:
        """
        calculates forces and moments

        Returns:
            Tuple[Tuple[np.float, np.float, np.float], Tuple[np.float, np.float, np.float]]: Forces in the X, Y, and Z direction + Moments on the X, Y, and Z axis
        """
        pass

    def reward(self) -> np.float:
        """[summary]

        Raises:
            NotImplementedError: implement your own damn reward function

        Returns:
            np.float: the reward value
        """
        raise NotImplementedError


class WindTunnelSimulation(gym.Env):
    metadata = {'render.modes': ['human']}
    def __init__(self) -> None:
        super().__init__()
        self.action_space = spaces.Discrete(1)
        self.observation_space = spaces.Box()
    
    def step(self, action):
        ...
        return observation, reward, done, info

    def reset(self):
        ...
        return observation  # reward, done, info can't be included

    def render(self, mode='human'):
        ...
    
    def close (self):
        ...


if __name__ == '__main__':
    WindTunnel([1e-3, 1e-3, 1e-3], [1e2, 1e2, 1e2])