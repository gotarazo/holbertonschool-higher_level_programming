#!/usr/bin/python3
for a in range(0, 26, 2):
    print("{:c}{:c}".format(122 - a, (122 - a - 1) - 32), end='')
