#!/usr/bin/env python3
from datetime import datetime as dt
import random
import os
import sys

import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def get_ip_and_timestamp_from_line(l):
    """This function takes a line and returns tuple
    of IP address and timestamp.
    """
    splitted_line = l.split()
    ip = splitted_line[0]
    timestamp = splitted_line[3][1:]

    return  ip, dt.strptime(timestamp, "%d/%b/%Y:%H:%M:%S")


def analyze_file(fn):
    with open(fn) as f:
        text = f.read()

    lines = text.split("\n")

    accesses = [get_ip_and_timestamp_from_line(l) for l in lines if l]

    #print(accesses[0], accesses[-1])

    N = len(accesses)

    times = [access[1] for access in accesses]

    print(times[0], times[-1])

    ys = [random.random() for i in range(N)]

    plt.title(fn)
    plt.plot(times, ys, 'k.')
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    plt.gcf().autofmt_xdate()
    plt.show()


if __name__ == "__main__":
    directory = sys.argv[1] if len(sys.argv) > 1 else "."
    files = [os.path.join(directory, fn)
             for fn in os.listdir(directory)
             if fn.startswith("access.log")]
    files.sort()

    print(files)

    for fn in sorted(files):
        analyze_file(fn)
