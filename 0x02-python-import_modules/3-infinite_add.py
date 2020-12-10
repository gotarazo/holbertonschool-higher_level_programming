#!/usr/bin/python3
import sys
if __name__ == "__main__":
    _sum = 0
    for i in range(len(sys.argv) - 1):
        _sum += int(sys.argv[i + 1])
    print("{}".format(_sum))
