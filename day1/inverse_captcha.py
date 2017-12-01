#!/usr/bin/env python3

import numpy as np


def get_sequence():
    with open("input.dat", "r") as f:
        lines = f.readlines()
        sequence_str = lines[0].strip()
    return sequence_str

def get_sum_of_equal_consecutive_pairs(sequence_str, shift):
    sequence = np.array(list(sequence_str), dtype=int)
    sum = 0
    for current, next in zip(sequence, np.roll(sequence, shift)):
        if current == next:
            sum += current
    return sum

def get_solution_part1(sequence_str):
    return get_sum_of_equal_consecutive_pairs(sequence_str, -1)

def get_solution_part2(sequence_str):
    shift = int(0.5*len(sequence_str))
    return get_sum_of_equal_consecutive_pairs(sequence_str, shift)


if __name__=="__main__":
    s = get_sequence()
    solution_part1 = get_solution_part1(s)
    solution_part2 = get_solution_part2(s)
    print("Solution part1: {}".format(solution_part1))
    print("Solution part2: {}".format(solution_part2))
