#!/usr/bin/env python3

import math
import sys

from calc import calc_average, calc_stdev, back_one_minute, back_two_minutes, fif_percent, nin_percent

def check_float(string):
    try:
        fl = float(string)
        return fl
    except ValueError:
        return None

def check_args():
    if len(sys.argv) != 2:
        return None
    return check_float(sys.argv[1])


if __name__ == "__main__":
    a = check_args()
    if a is None or a < 0 or a > 2.5:
        sys.exit(84)

    av = calc_average(a)
    print("mean return time: {mi}m {se}s".format(mi=(int(math.ceil(av * 60)) // 60), se=(int(math.ceil(av * 60)) % 60)))

    stdev = calc_stdev(av, a)
    print("standard deviation: %.3f" % stdev)

    fif = fif_percent(a)
    print("time after which 50% of the ducks are back: {mi}m {zero}{se}s".format(mi=(int(math.ceil(fif * 60)) // 60), zero=("" if (int(math.ceil(fif * 60)) % 60) > 9 else "0") ,se=(int(math.ceil(fif * 60)) % 60)))

    nin = nin_percent(a)
    print("time after which 99% of the ducks are back: {mi}m {zero}{se}s".format(mi=(int(math.ceil(nin * 60)) // 60), zero=("" if (int(math.ceil(nin * 60)) % 60) > 9 else "0"), se=(int(math.ceil(nin * 60)) % 60)))

    one_minute = back_one_minute(a)
    print("percentage of ducks back after 1 minute: %.1f%%" % one_minute)

    two_minutes = back_two_minutes(a)
    print("percentage of ducks back after 2 minutes: %.1f%%" % two_minutes)
