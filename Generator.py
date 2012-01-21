#!/usr/bin/env python3
#//==========================================================================//
#// Copyright (c) 2012 Wen-Han Gu. All rights reserved.
#//
#// Author: Nowar Gu (Wen-Han Gu)
#// E-mail: wenhan.gu <at> gmail.com
#//
#// Any advice is welcome. Thank you!
#//==========================================================================//

import random

class Generator(object):

  def __init__(self):
    pass


  def gen(self):
    City = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    CityNum= (10, 11, 12, 13, 14, 15, 16, 17, 34, 18, 19, 20, 21,
              22, 35, 23, 24, 25, 26, 27, 28, 29, 32, 30, 31, 33)
    CityDict = dict(zip(City, CityNum))

    Char = random.choice(City)
    Nums = [random.choice((1, 2))] + random.sample(range(0, 10), 7)

    Nums_Val = [Elmnt*(8-i) for i, Elmnt in enumerate(Nums)]
    Checksum = CityDict[Char]//10 + CityDict[Char]%10*9 + sum(Nums_Val)
    Checksum = (10-Checksum%10)%10
    Nums.append(Checksum)

    return Char + "".join(map(str, Nums))
