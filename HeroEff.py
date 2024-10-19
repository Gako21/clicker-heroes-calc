import numpy as np
import matplotlib.pyplot as plt
import HeroesClass as hero

EXP_LEVEL_VALUE = 0.996545

class HeroEff:

    def __init__(self, herolist):
        """Creates the HeroEff instance

        Args:
            herolist (Hero[]): Array of heroes.
        """
        self.herolist = herolist

    def createheroes(self):
        """Creates and initializes the heroes.

        Returns:
            Hero[]: Array of heroes.
        """
        heroes1 = np.empty(25, dtype=hero.LowHero)
        heroes2 = np.empty(19, dtype=hero.MidHero)
        heroes3 = np.empty(5, dtype=hero.HighHero)
        heroes4 = np.empty(4, dtype=hero.EndHero)

        herofile = open("heroes.txt")
        heroupgrades = open("upgradesPersonal.txt")
        heroupgradelevels = open("upgradesPersonalLevel.txt")

        for i in range(0, 25):
            herotemp = hero.LowHero("hero", 0, 0, 0, 0)
            herotemp.parse(herofile.readline().rstrip('\n'), heroupgrades.readline().rstrip('\n'), heroupgradelevels.readline().rstrip('\n'))
            heroes1[i] = herotemp
        
        for i in range(0, 19):
            herotemp = hero.MidHero("hero", 0, 0, 0, 0)
            herotemp.parse(herofile.readline().rstrip('\n'), heroupgrades.readline().rstrip('\n'), heroupgradelevels.readline().rstrip('\n'))
            heroes2[i] = herotemp
        
        for i in range(0, 5):
            herotemp = hero.HighHero("hero", 0, 0, 0, 0)
            herotemp.parse(herofile.readline().rstrip('\n'), heroupgrades.readline().rstrip('\n'), heroupgradelevels.readline().rstrip('\n'))
            heroes3[i] = herotemp
        
        for i in range(0, 4):
            herotemp = hero.EndHero("hero", 0, 0, 0, 0)
            herotemp.parse(herofile.readline().rstrip('\n'), heroupgrades.readline().rstrip('\n'), heroupgradelevels.readline().rstrip('\n'))
            heroes4[i] = herotemp
        
        heroes = np.concatenate((heroes1, heroes2, heroes3, heroes4))
        herofile.close()

        self.herolist = heroes

    def damage(self, heronum, level):
        return self.herolist[heronum - 1].totaldamage(level)

    def costtolevel(self, level):
        costs = np.zeros(len(self.herolist))
        for i in range(0, len(costs)):
            costs[i] = self.herolist[i].levelcost(level)
        return costs

    def levelwithgold(self, money):
        levels = np.zeros(len(self.herolist))
        for i in range(0, len(levels)):
            levels[i] = self.herolist[i].costlevel(money)
        return np.floor(levels * EXP_LEVEL_VALUE)

    def damagewithgold(self, money):
        levels = self.levelwithgold(money)
        leveldiff = np.remainder(levels, 25)
        print(leveldiff)
        mask = np.zeros(53)
        for i in range (1, 53):
            if(leveldiff[0] - leveldiff[i] > 12):
                mask[i] = 0 #-np.log10(4)

        damages = np.zeros(len(levels))
        for i in range(0, len(levels)):
            damages[i] = self.herolist[i].totaldamage(levels[i]) + mask[i]
        return damages

    def drawheroes(self, start, iters, step):
        damagesmain = []
        for i in np.arange(start, iters, step):
            damagesmain.append(self.damagewithgold(i))
        # plt.figure(dpi=2000)
        damagesmain = np.swapaxes(damagesmain, 0, 1)

        starts = iters * np.ones(53, dtype=np.int64)
        for i in range(0, 53):
            for j in range(0, len(damagesmain[i])):
                if (damagesmain[i][j] > 0):
                    starts[i] = j
                    break

        for i in range(1, 53):
            damagesmain[i] = damagesmain[i] - damagesmain[0]
            plt.plot(np.arange(start + starts[i] * step, iters, step), damagesmain[i][starts[i]:])
        plt.show()