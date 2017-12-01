#!/usr/bin/env python3

import numpy as np


def get_sequence():
    with open("input.dat", "r") as f:
        lines = f.readlines()
        sequence_str = lines[0].strip()
    return sequence_str

def get_solution(sequence_str):
    sequence = np.array(list(sequence_str), dtype=int)
    sum = 0
    for current, next in zip(sequence, np.roll(sequence, -1)):
        if current == next:
            sum += current
    return sum


if __name__=="__main__":
    s = get_sequence()
    solution = get_solution(s)
    print("Solution: {}".format(solution))
