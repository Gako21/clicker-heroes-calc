# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 14:41:42 2024

@author: petty
"""

import numpy as np
import HeroesClass as hc


class TestClass:
    def test_LowHero(self):
        Betty = hc.LowHero("Betty", 9.76, 2, 2, 5, np.array([1, 1, 1, 1, 1, 1, 1]))
        Frostleaf = hc.LowHero("Frostleaf", 7.469, 22, 2.1, 27, np.array([2, 2, 1, 1, 1, 1, 1]))

        assert np.round(Betty.basedamage(1), decimals=3) == 2.989
        assert np.round(Betty.basedamage(150), decimals=3) == 5.166
        assert Betty.leveldamage(1) == 0
        assert np.round(Betty.leveldamage(400), decimals=3) == 5.419
        assert np.round(Betty.levelcost(1), decimals=3) == 5.301
        assert np.round(Betty.levelcost(150), decimals=3) == 10.850
        assert Betty.upgradedamage(500) == 1

        assert np.round(Frostleaf.basedamage(1), decimals=3) == 22.873
        assert np.round(Frostleaf.basedamage(125), decimals=3) == 24.970
        assert np.round(Frostleaf.leveldamage(1300), decimals=3) == 27.491
        assert np.round(Frostleaf.leveldamage(10300), decimals=3) == 247.018
        assert np.round(Frostleaf.levelcost(777), decimals=3) == 51.231
        assert np.round(Frostleaf.levelcost(1010), decimals=3) == 58.054
        assert Frostleaf.upgradedamage(9) == 1
        assert Frostleaf.upgradedamage(100) == 4

    def test_MidHero(self):
        Terra = hc.MidHero("Terra", 7.113, 57, 1, 70, np.array([2, 2, 2, 2.5, 1, 1, 1]))
        Zilar = hc.MidHero("Zilar", 7.283, 3333, 1, 4000, np.array([11, 1, 1, 1, 1, 1, 1]))

        assert np.round(Terra.basedamage(1), decimals=3) == 57.852
        assert np.round(Terra.basedamage(175), decimals=3) == 60.095
        assert Terra.leveldamage(1) == 0
        assert np.round(Terra.leveldamage(800), decimals=3) == 15.924

        assert np.round(Zilar.basedamage(1), decimals=3) == 3333.862
        assert np.round(Zilar.basedamage(125), decimals=3) == 3335.959
        assert np.round(Zilar.leveldamage(2222), decimals=3) == 50.435
        assert np.round(Zilar.leveldamage(12222), decimals=3) == 293.647

    def test_HighHero(self):
        Xavira = hc.HighHero("Xavira", 3.954, 11681, 1, 14000, np.array([1, 1, 1, 1, 1, 1, 1]))
        Maw = hc.HighHero("The Maw", 1.581, 61730, 1, 45500, np.array([1, 1, 1, 1, 1, 1, 1]))

        assert np.round(Xavira.basedamage(1), decimals=3) == 11681.597
        assert np.round(Xavira.basedamage(175), decimals=3) == 11683.840
        assert Xavira.leveldamage(100) == 0
        assert np.round(Xavira.leveldamage(800), decimals=3) == 16.330

        assert np.round(Maw.basedamage(1), decimals=3) == 61730.199
        assert np.round(Maw.basedamage(150), decimals=3) == 61732.375
        assert np.round(Maw.leveldamage(1001), decimals=3) == 21.556
        assert np.round(Maw.leveldamage(1234), decimals=3) == 27.435

    def test_EndHero(self):
        Rose = hc.EndHero("Rose", 8.586, 148592, 1, 108000, np.array([1, 1, 1, 1, 1, 1, 1]))
        Blanche = hc.EndHero("Blanche", 4.661, 178104, 1, 127500, np.array([1, 1, 1, 1, 1, 1, 1]))

        assert np.round(Rose.basedamage(1), decimals=3) == 148592.934
        assert np.round(Rose.basedamage(175), decimals=3) == 148595.177
        assert Rose.leveldamage(100) == 0
        assert Rose.leveldamage(400) == 27
        assert Rose.levelcost(1) == 108000
        assert np.round(Rose.levelcost(150), decimals=3) == 108013.612

        assert np.round(Blanche.basedamage(1), decimals=3) == 178104.668
        assert np.round(Blanche.basedamage(150), decimals=3) == 178106.845
        assert Blanche.leveldamage(750) == 69
        assert Blanche.leveldamage(1234) == 126
        assert np.round(Blanche.levelcost(752), decimals=3) == 127565.600
        assert np.round(Blanche.levelcost(2251), decimals=3) == 127695.054
