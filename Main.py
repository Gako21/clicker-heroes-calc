# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 20:51:46 2024

@author: petty
"""

import numpy as np
import matplotlib.pyplot as plt
import HeroEff as herocol


def calculatedmgandcost(heroes, level, offset=0):
    """
    Calculate the damage and cost of a hero from level "offset + 1" to "level".

    Parameters
    ----------
    heroes : array(Hero)
        Array of heroes whose values are to be calculated.
    level : int
        Final hero level where the values are calculated.
    offset : int, optional
        How many levels past 1 the first calculation should be made.

    Returns
    -------
    costs : array(array(float))
        Base 10 logarithm of a hero's cost for each level for each hero.
    damages : array(array(float))
        Base 10 logarithm of a hero's damage for each level for each hero.
    names : array(string)
        Names of the heroes.

    """
    heroamount = np.shape(heroes)[0]
    costs = np.zeros(heroamount, dtype=np.ndarray)
    damages = np.zeros(heroamount, dtype=np.ndarray)
    names = np.zeros(heroamount, dtype='<U12')

    for i in range(0, heroamount):
        cost = np.zeros(level - offset)
        damage = np.zeros(level - offset)
        for j in range(0, level - offset):
            cost[j] = heroes[i].levelcost(j + offset + 1)
            damage[j] = heroes[i].basedamage(j + offset + 1) + heroes[i].leveldamage(j + offset + 1)
        costs[i] = cost
        damages[i] = damage
        names[i] = heroes[i].getname()

    return costs, damages, names


def optimalheroes(cost, damage, name):
    dmgpercost = damage - cost
    for i in range(0, np.shape(cost)[0] - 1):
        cost[i] = np.around(cost[i])
    start = int(cost[-1][0])
    end = int(cost[0][-1])
    temp = np.full(end + 1, -np.inf)
    result = np.zeros(end + 1, dtype='<U12')
    if (start > end):
        return

    for i in range(0, np.shape(name)[0]):
        for j in range(0, np.shape(cost[i])[0]):
            index = int(cost[i][j])
            if (index > end):
                continue
            if (dmgpercost[i][j] > (temp[index])):
                temp[index] = dmgpercost[i][j]
                result[index] = name[i]
#            plt.plot(cost[i][j], dmgpercost[i][j], marker="o")
#    plt.show()

heroCollection = herocol.HeroEff(0)
heroCollection.createheroes()
heroCollection.drawheroes(0, 50, 0.03125)

# cost, damage, name = calculatedmgandcost(heroes, 3000, 0)
# optimalheroes(cost, damage, name)
# drawheroes(cost, damage)
