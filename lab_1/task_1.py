# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union
import doctest

class FireArm:
    def __init__(self, name: str, damage: Union[int, float], mag_capacity: int, ammo_left: int):
        """

        Initializing instance of class "FireArm"

        :param name: Name of the firearm
        :param damage: Damage that the firearm deals per shot
        :param mag_capacity: Capacity of the firearm magazine (how many bullets it can hold)
        :param ammo_left: Number of bullets left in magazine

        Example:
        >>> glock17 = FireArm("glock-17", 20, 17, 17)

        """
        self.name = name

        if not isinstance(damage, (int, float)):
            raise TypeError("Firearm's damage should be int or float type.")
        if damage <= 0:
            raise ValueError("Firearm's damage should be a positive number.")
        self.damage = damage

        if not isinstance(mag_capacity, int):
            raise TypeError("Magazine capacity of the firearm should be int type.")
        if mag_capacity <= 0:
            raise ValueError("Magazine capacity of the firearm should be a positive number.")
        self.mag_capacity = mag_capacity

        if not isinstance(ammo_left, int):
            raise TypeError("Number of bullets left in magazine should be int type.")
        if (ammo_left < 0) or (ammo_left > mag_capacity):
            raise ValueError("Number of bullets left in magazine should not be negative or greater than magazine "
                             "capacity.")
        self.ammo_left = ammo_left

    def check_mag(self) -> int:
        """

        Method that is used for checking ammo left in firearm's magazine

        :return: Number of bullets left in magazine

        Example:
        >>> glock17 = FireArm("glock-17", 20, 17, 15)
        >>> glock17.check_mag()
        15
        """
        return self.ammo_left

    def reload(self) -> None:
        """

        Method that is used for reloading firearm's magazine

        Example:
        >>> glock17 = FireArm("glock-17", 20, 17, 10)
        >>> glock17.reload()
        >>> glock17.check_mag()
        17

        """
        self.ammo_left = self.mag_capacity

    def shoot(self, times: int) -> None:
        """

        Method that is used for shooting the firearm certain number of times

        :param times: Number of times the firearm should shoot
        :raise ValueError: If number of times is nonpositive or greater than bullets
        left in the magazine, raise the error

        Example:
        >>> glock17 = FireArm("glock-17", 20, 17, 17)
        >>> glock17.shoot(5)

        """
        if not isinstance(times, int):
            raise TypeError("Number of times the firearm will shoot should be int type.")
        if (times <= 0) or (times > self.ammo_left):
            raise ValueError("Number of times the firearm will shoot should be positive and not greater "
                             "than ammo left.")
        ...


class Kettle:
    def __init__(self, powered: bool, water_capacity: Union[int, float], water_left: Union[int, float],
                 water_temperature: Union[int, float]):
        """

        Initializing instance of class "Kettle"

        :param powered: If the kettle powered with electricity
        :param water_capacity: Maximum volume of water which the kettle can hold
        :param water_left: Volume of water left in kettel
        :param water_temperature: Tempreture of the water in kettle

        Example:
        >>> kettle = Kettle(False, 1700, 1000, 18)
        """

        if not isinstance(powered, bool):
            raise TypeError('Condition "powered" of kettle should be boolean type.')
        self.powered = powered

        if not isinstance(water_capacity, (int, float)):
            raise TypeError("Capacity of the kettle should be int or float type.")
        if water_capacity <= 0:
            raise ValueError("Capacity of the kettle should be positive number.")
        self.water_capacity = water_capacity

        if not isinstance(water_left, (int, float)):
            raise TypeError("Volume of water left in the kettle should be int or float type.")
        if (water_left < 0) or (water_left > water_capacity):
            raise ValueError("Volume of water left in the kettle should not be negative or greater than "
                             "kettle capacity.")
        self.water_left = water_left

        if not isinstance(water_temperature, (int, float)):
            raise TypeError("Temperature of water in the kettle should be int or float type.")
        if (water_temperature < 0) or (water_temperature > 100):
            raise ValueError("Temperature of water in the kettle should be in the interval of [0, 100]")
        self.water_temperature = water_temperature

    def boil_water(self) -> None:
        """

        Method that is used to boil water in the kettle (set it to 100)

        Example:
        >>> kettle = Kettle(False, 1700, 1000, 17)
        >>> kettle.boil_water()
        >>> kettle.water_temperature
        100

        """
        self.water_temperature = 100

    def add_water(self, water_volume: Union[int, float]) -> None:
        """

        Method that is used to add water in the kettle

        :param water_volume: Volume of water added in the kettle
        :raise ValueError: If volume of additional water is greater than the left volume of the kettle, raise the error

        Example:
        >>> kettle = Kettle(False, 1700, 1000, 17)
        >>> kettle.add_water(500)
        """

        if not isinstance(water_volume, (int, float)):
            raise TypeError("Volume of added water should be int or float type.")
        if self.water_capacity - self.water_left < water_volume:
            raise ValueError("Volume of added water should not be greater than the left volume of the kettle.")
        self.water_left += water_volume


class Interval:
    def __init__(self, left_endpoint: Union[int, float], right_endpoint: Union[int, float]):
        """

        Initializing instance of class "Interval"

        :param left_endpoint: Left endpoint of the interval
        :param right_endpoint: Right endpoint of the interval

        Example:
        >>> unit_interval = Interval(0, 1)
        """

        if not isinstance(left_endpoint, (int, float)):
            raise TypeError("Left endpoint of the interval should be int or float type.")
        if not isinstance(right_endpoint, (int, float)):
            raise TypeError("Right endpoint of the interval should be int or float type.")
        if left_endpoint > right_endpoint:
            raise ValueError("Left endpoint should not be greater than right endpoint")
        self.left_endpoint = left_endpoint
        self.right_endpoint = right_endpoint

    def length(self) -> Union[int, float]:
        """

        Method that is used to find the length of the interval

        :return: Length of the interval

        Example:
        >>> interval = Interval(10, 15.5)
        >>> interval.length()
        5.5

        """
        return self.right_endpoint - self.left_endpoint

    def intersection(self, interval: "Interval") -> Union["Interval", None]:
        """

        Method used to find the intersection with another interval

        :param interval: Another interval with which you want to find the intersection

        :return: If there is an intersection return interval of it, else return None

        Example:
        >>> interval1 = Interval(10, 15)
        >>> interval2 = Interval(12, 20)
        >>> interval3 = interval1.intersection(interval2)
        >>> interval3.left_endpoint
        12
        >>> interval3.right_endpoint
        15

        """
        if (self.left_endpoint > interval.right_endpoint) or (self.right_endpoint < interval.left_endpoint):
            return None
        if self.left_endpoint > interval.left_endpoint:
            left_endpoint = self.left_endpoint
        else:
            left_endpoint = interval.left_endpoint
        if self.right_endpoint < interval.right_endpoint:
            right_endpoint = self.right_endpoint
        else:
            right_endpoint = interval.right_endpoint
        return Interval(left_endpoint, right_endpoint)


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()