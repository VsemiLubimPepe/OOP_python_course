class Target:
    """

    Stub class to implement method attack() of the weapon

    """
    pass


class Weapon:
    def __init__(self, name: str, damage: float, attack_range: float):
        """

        Initializing instance of class "Weapon"

        :param name: Name of the weapon
        :param damage: Damage that the weapon deals per hit
        :param attack_range: Range of the weapon attack (in tiles)

        Example:
        >>> stick = Weapon("stick", 5, 2)

        """
        if not isinstance(name, str):
            raise TypeError("Name of the weapon should be string type.")
        self.name = name
        if not isinstance(damage, (float, int)):
            raise TypeError("Damage of the weapon should be float or int type.")
        if damage <= 0:
            raise ValueError("Damage should be a positive number.")
        self.damage = damage
        if not isinstance(attack_range, (float, int)):
            raise TypeError("Attack range of the weapon should be float or int type.")
        if attack_range < 0:
            raise ValueError("Attack range of the weapon should not be a negative number.")
        self.attack_range = attack_range

    def __str__(self) -> str:
        """

        Method to return the Weapon object info - its name and all stats.

        :return: info about the Weapon (name and stats)

        """
        return f"{self.__class__.__name__} - {self.name}. Stats: damage - {self.damage}, " \
               f"attack range - {self.attack_range}"

    def __repr__(self) -> str:
        """

        Method to return the representation of Weapon object (by copying it you can get instance of this class).

        :return: string representation of the Weapon object (used to create the same object)

        """
        return f"{self.__class__.__name__}(name={self.name!r}, damage={self.damage!r}, " \
               f"attack_range={self.attack_range!r})"

    def attack(self, target: Target) -> None:
        """

        Method for attacking target (dealing weapon damage to it).

        """
        # There should be some code for dealing damage to someone (there should also be a parameter -
        # object (someone who should be attacked), so I just made a stub (Target)).
        ...

    def upgrade_damage(self, damage_bonus: float) -> None:
        """

        Method for upgrading weapon damage.

        """
        if not isinstance(damage_bonus, (float, int)):
            raise TypeError("Damage bonus should be float or int type.")
        if damage_bonus <= 0:
            raise ValueError("Damage bonus should be a positive number.")
        self.damage += damage_bonus


class ColdWeapon(Weapon):
    def __init__(self, name: str, damage: float, attack_range: float, durability: int):
        """

        Initializing instance of class "Weapon"

        :param name: Name of the weapon
        :param damage: Damage that the weapon deals per hit
        :param attack_range: Range of the weapon attack (in tiles)
        :param durability: Durability of the cold weapon (amount of the attacks you can do)

        Example:
        >>> sword = ColdWeapon("sword", 25, 3, 100)

        """
        super().__init__(name, damage, attack_range)
        if not isinstance(durability, int):
            raise TypeError("Durability of cold weapon should be int type.")
        if (durability < 0) or (durability > 100):
            raise ValueError("Durability can be in range from 0 (broken) to 100 (new).")
        self.durability = durability

    def __str__(self) -> str:
        """

        Method to return the ColdWeapon object info - its name and all stats.

        :return: info about the ColdWeapon (name and stats)

        """
        return super().__str__() + f", durability - {self.durability}"

    def __repr__(self) -> str:
        """

        Method to return the representation of ColdWeapon object (by copying it you can get instance of this class).

        :return: string representation of the ColdWeapon object (used to create the same object)

        """
        return f"{self.__class__.__name__}(name={self.name!r}, damage={self.damage!r}, " \
               f"attack_range={self.attack_range!r}, durability={self.durability!r})"

    def attack(self, target: Target) -> None:
        """

        Method for attacking target (dealing weapon damage to it).

        """
        super().attack(target)
        self.durability -= 1

    def repair(self) -> None:
        """

        Method for repairing cold weapon (set durability = 100)

        """
        self.durability = 100


class Firearm(Weapon):
    def __init__(self, name: str, damage: float, attack_range: float, max_ammo: int, ammo: int):
        """

        Initializing instance of class "Weapon"

        :param name: Name of the weapon
        :param damage: Damage that the weapon deals per hit
        :param attack_range: Range of the weapon attack (in tiles)
        :param max_ammo: Capacity of the firearm magazine
        :param ammo: Current amount of ammo in firearm magazine

        Example:
        >>> m1911 = Firearm("m1911", 40, 10, 7, 5)

        """
        super().__init__(name, damage, attack_range)
        if not isinstance(max_ammo, int):
            raise TypeError("Firearm's max ammo should be int type.")
        if max_ammo <= 0:
            raise ValueError("Firearm's max ammo should be a positive number.")
        self.max_ammo = max_ammo
        if not isinstance(ammo, int):
            raise TypeError("Number of ammo should be int type.")
        if (ammo < 0) or (ammo > max_ammo):
            raise ValueError("Number of ammo should be in range from 0 (empty firearm) "
                             "to max_ammo value (full magazine).")
        self.ammo = ammo

    def __str__(self) -> str:
        """

        Method to return the Firearm object info - its name and all stats.

        :return: info about the Firearm (name and stats)

        """
        return super().__str__() + f", max ammo - {self.max_ammo}, ammo - {self.ammo}"

    def __repr__(self) -> str:
        """

        Method to return the representation of Firearm object (by copying it you can get instance of this class).

        :return: string representation of the Firearm object (used to create the same object)

        """
        return f"{self.__class__.__name__}(name={self.name!r}, damage={self.damage!r}, " \
               f"attack_range={self.attack_range!r}, max_ammo={self.max_ammo!r}, ammo={self.ammo!r})"

    def attack(self, target: Target) -> None:
        """

        Method for attacking target (dealing weapon damage to it).

        """
        super().attack(target)
        self.ammo -= 1

    def reload(self) -> None:
        """

        Method that is used for reloading firearm's magazine

        Example:
        >>> m1911 = Firearm("m1911", 40, 10, 7, 5)
        >>> m1911.reload()

        """
        self.ammo = self.max_ammo
