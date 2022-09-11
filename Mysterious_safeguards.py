#!/usr/bin/env python

import math

def find_total_coverage(input_file):
    with open(input_file) as f:
        lines = f.readlines()
        N = int(lines[0].strip())
        intervals = []

        n = 1
        for interval in lines[1:]:
            [start, end] = interval.strip().split()
            intervals.append((int(start), n))
            intervals.append((int(end), n))
            n = n + 1

        intervals.sort(key=lambda x: x[0])

        total_coverage = 0
        lifeguard_coverage = [0] * N
        lifeguard_set = set()
        last_time = 0
        for (time, n) in intervals:
            diff = time - last_time
            if len(lifeguard_set) == 1:
                guard = next(iter(lifeguard_set)) - 1
                lifeguard_coverage[guard] += diff
            if len(lifeguard_set) != 0:
                total_coverage += diff
            if n in lifeguard_set:
                lifeguard_set.remove(n)
            else:
                lifeguard_set.add(n)
            last_time = time

        max_coverage = 0
        for cover in lifeguard_coverage:
            max_coverage = max(max_coverage, total_coverage - cover)

        print("Total coverage max ", total_coverage, max_coverage)
        return max_coverage

def run_tests():
    for i in range(1,11):
        print(i)
        input_file, output_file = str(i) + ".in", str(i) + ".out"
        max_coverage = find_total_coverage(input_file)
        open(output_file, 'w').write(str(max_coverage))


if __name__ == '__main__':
    run_tests()
