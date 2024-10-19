# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 14:18:25 2024

@author: gako.
"""
import numpy as np


class Hero:
    """
    A class for a hero in Clicker Heroes.
    """

    def __init__(self, name, damage, cost, upgrademultis, upgradelevels):
        """
        Initialize a new hero.

        Parameters
        ----------
        name : string
            Name of the hero.
        damage : float
            Base 10 logarithm of hero base damage.
        cost : float
            Base 10 logarithm of hero base cost.
        upgrademultis : array(float)
            Personal damage multipliers for each upgrade.
        upgradelevels : array(int)
            Levels for each personal damage multiplier espficied above.

        Returns
        -------
        None.

        """
        self.name = name
        self.damage = damage
        self.cost = cost
        self.upgrademultis = upgrademultis
        self.upgradelevels = upgradelevels

    def basedamage(self, level):
        """
        Calculate the damage from base damage and hero level.

        Parameters
        ----------
        level : int
            Hero level.

        Returns
        -------
        float
            Base 10 logarithm of hero damage.

        """
        if (level < 1): return 0
        return self.damage + np.log10(level)

    def leveldamage(self, level):
        """
        Calculate the damage multiplier from hero level bonuses. This is a template
        method that is replaced by individual hero subclasses.

        Parameters
        ----------
        level : int
            Hero level.

        Returns
        -------
        int
            One.

        """
        return 1

    def upgradedamage(self, level):
        """
        Calculate the damage multiplier from individual upgrades
        
        Parameters
        ----------
        level : int
            Hero level.
        
        Returns
        -------
        float
            Base 10 logarithm of damage multiplier.
        
        """
        multiplier = 0
        for i in range(len(self.upgradelevels) - 1, -1, -1):
            if (self.upgradelevels[i] <= level):
                multiplier = self.upgrademultis[i]
                break

        return multiplier

    def totaldamage(self, level):
        """Calculate the total damage of hero at given level.

        Args:
            level (int): Hero level.

        Returns:
            float: Base 10 logarithm of hero damage.
        """
        return self.basedamage(level) + self.leveldamage(level) + self.upgradedamage(level)

    def levelcost(self, level):
        """
        Calculate the cumulative cost of levelling a hero to given level. Uses approximation
        if level is above 200.

        Parameters
        ----------
        level : int
            Hero level.

        Returns
        -------
        float
            Base 10 logarithm of hero levelling cost.

        """
        if (level <= 200):
            return self.cost + np.log10(1.06975**level - 1) - np.log10(0.06975)
        return self.cost - np.log10(0.06975) + level * np.log10(1.06975)
    
    def costlevel(self, money):
        """Calculate the level to which a hero can be levelled to with given amount of money.
        Uses approximation if money is less than 10 + base cost.

        Args:
            money (float): Base 10 logarithm of money available.

        Returns:
            float: Level of hero.
        """
        if (money < 10 + self.cost):
            return np.floor(np.log10(0.06975 * np.power(10, money - self.cost) + 1) / np.log10(1.06975))
        return np.floor((money - self.cost + np.log10(0.06975)) / np.log10(1.06975))

    def getname(self):
        """
        Return hero's name.

        Returns
        -------
        string
            Hero's name.

        """
        return self.name

    def parse(self, linehero, lineupgrade, linelevel):
        """
        Initializes the hero based on the given .csv file.

        Parameters
        ----------
        linehero : string
            Hero initialization data.
        lineupgrade : string
            Hero's personal upgrade damage multiplier data.
        linelevel : string
            Hero's personal upgrade level data.
        """
        values = linehero.split(",")
        upgrades = lineupgrade.split(",")
        levels = linelevel.split(",")
        
        self.name = values[0]
        self.damage = float(values[1])
        self.cost = float(values[2])

        self.upgrademultis = []
        self.upgradelevels = []

        for i in range(0, len(upgrades)):
            self.upgrademultis.append(float(upgrades[i]))
            self.upgradelevels.append(int(levels[i]))


class LowHero(Hero):
    """A class for a low-level hero; from Treebeast to Frostleaf."""

    def leveldamage(self, level):
        """
        Calculate the damage multiplier from hero level bonuses.

        Parameters
        ----------
        level : int
            Hero level.

        Returns
        -------
        float
            Base 10 logarithm of hero damage.

        """
        if (level < 200):
            return 0
        # Convert to same base, then convert to base 10 exponent.
        return (np.floor((level - 175) / 25) + np.min([8, np.floor(level / 1000)]) *
                np.log(2.5) / np.log(4)) * np.log(4) / np.log(10)


class MidHero(Hero):
    """A class for a mid-level hero; from Dark Knight to Madzi."""

    def leveldamage(self, level):
        """
        Calculate the damage multiplier from hero level bonuses.

        Parameters
        ----------
        level : int
            Hero level.

        Returns
        -------
        float
            Base 10 logarithm of hero damage.

        """
        if (level < 200):
            return 0
        # Convert to same base, then convert to base 10 exponent.
        return ((np.floor((level - 175) / 25) + np.min([8, np.floor(level / 1000)]) *
                 np.log(2.5) / np.log(4)) * np.log(4) / np.log(10) +
                np.min([9, np.floor(np.max([0, level - 500]) / 25)]) * np.log(1.25) / np.log(10))


class HighHero(Hero):
    """A class for a high-level hero; from Xavira to Yachiyl."""

    def leveldamage(self, level):
        """
        Calculate the damage multiplier from hero level bonuses.

        Parameters
        ----------
        level : int
            Hero level.

        Returns
        -------
        float
            Base 10 logarithm of hero damage.

        """
        if (level < 200):
            return 0
        return np.floor((level - 175) / 25) * np.log(4.5) / np.log(10)


class EndHero(Hero):
    """A class for an end-level hero; from Rose to Dorothy."""

    def leveldamage(self, level):
        """
        Calculate the damage multiplier from hero level bonuses.

        Parameters
        ----------
        level : int
            Hero level.

        Returns
        -------
        float
            Base 10 logarithm of hero damage.

        """
        if (level < 200):
            return 0
        return 3 * np.floor((level - 175) / 25)

    def levelcost(self, level):
        """
        Calculate the cumulative cost of levelling a hero to given level. Uses approximation
        if level is above 200.

        Parameters
        ----------
        level : int
            Hero level.

        Returns
        -------
        float
            Base 10 logarithm of hero levelling cost.

        """
        if (level <= 200):
            return self.cost + np.log10(1.22**level - 1) - np.log10(0.22)
        return self.cost - np.log10(0.22) + level * np.log10(1.22)
    
    def costlevel(self, money):
        """Calculate the level to which a hero can be levelled to with given amount of money.
        Uses approximation if money is less than 10 + base cost.

        Args:
            money (float): Base 10 logarithm of money available.

        Returns:
            float: Level of hero.
        """
        if (money < 10 + self.cost):
            return np.floor(np.log10(0.22 * np.power(10, money - self.cost) + 1) / np.log10(1.22))
        return np.floor((money - self.cost + np.log10(0.22)) / np.log10(1.22))