#!/usr/bin/env python

# The Computer Language Benchmarks Game
# https://salsa.debian.org/benchmarksgame-team/benchmarksgame/
#
# originally by Kevin Carson
# modified by Tupteq, Fredrik Johansson, and Daniel Nanz
# modified by Maciej Fijalkowski
# 2to3
# Update `BODIES` by long list representing `x, y, z, vx, vy, vz, mass`

import copy
import argparse
import rnbody_pyo3

def combinations(l):
    result = []
    length = len(l)
    for x in range(length - 1):
        ls = l[x+1:]
        for y in range(x+1, length):
            result.append((l[x], l[y]))
    return result

PI = 3.14159265358979323
SOLAR_MASS = 4 * PI * PI
DAYS_PER_YEAR = 365.24

BODIES = {
    'sun': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, SOLAR_MASS],

    'jupiter': [4.84143144246472090e+00,
                -1.16032004402742839e+00,
                -1.03622044471123109e-01,
                1.66007664274403694e-03 * DAYS_PER_YEAR,
                7.69901118419740425e-03 * DAYS_PER_YEAR,
                -6.90460016972063023e-05 * DAYS_PER_YEAR,
                9.54791938424326609e-04 * SOLAR_MASS],

    'saturn': [8.34336671824457987e+00,
               4.12479856412430479e+00,
               -4.03523417114321381e-01,
               -2.76742510726862411e-03 * DAYS_PER_YEAR,
               4.99852801234917238e-03 * DAYS_PER_YEAR,
               2.30417297573763929e-05 * DAYS_PER_YEAR,
               2.85885980666130812e-04 * SOLAR_MASS],

    'uranus': [1.28943695621391310e+01,
               -1.51111514016986312e+01,
               -2.23307578892655734e-01,
               2.96460137564761618e-03 * DAYS_PER_YEAR,
               2.37847173959480950e-03 * DAYS_PER_YEAR,
               -2.96589568540237556e-05 * DAYS_PER_YEAR,
               4.36624404335156298e-05 * SOLAR_MASS],

    'neptune': [1.53796971148509165e+01,
                -2.59193146099879641e+01,
                1.79258772950371181e-01,
                2.68067772490389322e-03 * DAYS_PER_YEAR,
                1.62824170038242295e-03 * DAYS_PER_YEAR,
                -9.51592254519715870e-05 * DAYS_PER_YEAR,
                5.15138902046611451e-05 * SOLAR_MASS]}


SYSTEM = list(BODIES.values())
PAIRS = combinations(SYSTEM)

def report_energy(bodies=SYSTEM, pairs=PAIRS, e=0.0):

    for ((x1, y1, z1, vx1, vy1, vz1, m1),
         (x2, y2, z2, vx2, vy2, vz2, m2)) in pairs:
        dx = x1 - x2
        dy = y1 - y2
        dz = z1 - z2
        e -= (m1 * m2) / ((dx * dx + dy * dy + dz * dz) ** 0.5)
    for (x, y, z, vx, vy, vz, m) in bodies:
        e += m * (vx * vx + vy * vy + vz * vz) / 2.
    print("%.9f" % e)

def offset_momentum(ref, bodies=SYSTEM, px=0.0, py=0.0, pz=0.0):

    for (x, y , z, vx, vy, vz, m) in bodies:
        px -= vx * m
        py -= vy * m
        pz -= vz * m

    ref[3] = px / ref[6]
    ref[4] = py / ref[6]
    ref[5] = pz / ref[6]


def run_planet_struct(n, ref='sun'):
    offset_momentum(BODIES[ref])
    report_energy()

    system = copy.deepcopy(SYSTEM)
    system = [
        rnbody_pyo3.Planet(x, y, z, vx, vy, vz, m)
        for (x, y, z, vx, vy, vz, m) in system
    ]
    system = rnbody_pyo3.advance_planet_struct(system, 0.01, n)
    pairs = combinations(system)
    report_energy(bodies=system, pairs=pairs)

def run_list(n, ref='sun'):
    offset_momentum(BODIES[ref])
    report_energy()

    system = rnbody_pyo3.advance_list(SYSTEM, 0.01, n)
    pairs = combinations(system)
    report_energy(bodies=system, pairs=pairs)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('steps', type=int)
    # Default use `planet_struct`. `--list` for list data type.
    parser.add_argument('--list', dest='list_struct', action='store_true')
    parser.set_defaults(list_struct=False)

    args = parser.parse_args()
    steps = args.steps
    list_struct = args.list_struct

    if not list_struct:
        run_planet_struct(steps)
    else:
        run_list(steps)
