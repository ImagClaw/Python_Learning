#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project: 7 random Lottery Numbers (0-9) write to a list
#   Date: 4/24/2019

import random

lottery = []
i=0

while i < 7:
    ranNum = random.randrange(9)
    lottery.append(ranNum)
    i += 1

print("The winning lottery numbers are: ")
for item in lottery:
    print(item, end=" ")