# Distance of cup from camera -2 centimeters?
# By: Cymberly Tsai 12/27/2021
# most accurate when cup in center of image

import math
import numpy
import sys
sys.path.append("..")
from detector import detector

x = [867, 806, 783, 759, 678, 681, 677, 673, 657, 651, 649, 643, 630, 620, 616, 539, 536, 541, 533, 530, 519, 505, 496, 483, 474, 459, 447, 423, 409, 389, 385, 372, 370, 364, 357, 349, 340, 350, 341, 331, 322, 322, 323, 298, 294]
y  = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,46,47,48,49,50]
ci = numpy.polyfit(x, y, 2)

def measure(x1, y1, x2, y2):
    pixi = int(math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2))
    centi = ci[0]*pixi**2 + ci[1]*pixi + ci[2]
    return centi

def getCenti():
    c = []
    for i in range(100):
        re = detector.pops()
        d = measure(re[1][0], re[1][1], re[2][0], re[2][1])
        c.append(d)
    print(c)

#while True:
#    go = input("Go?")
#    if go == "y":
#        re = detector.pops()
#        if re[0] == 'cup':
#            print(measure(re[1][0], re[1][1], re[2][0], re[2][1]))
#            print(re)

