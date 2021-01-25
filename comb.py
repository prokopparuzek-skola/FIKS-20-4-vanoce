#!/usr/bin/python3
import itertools as it
from sys import argv, exit

prev = dict()

def solve(blue :int, red :int) -> (int, int):
    if blue == 1 and red == 1:
        return (1, 0)
    elif blue == 1 and red == 0:
        return (1, 0)
    elif blue == 0 and red == 1:
        return (0, 1)
    elif blue == 2 and red == 0 or blue == 0 and red == 2:
        return (0, 1)
    else:
        i = [0]*blue + [1]*red
        if tuple(i) in prev:
            return prev[tuple(i)]
        else:
            out = [0, 0]
            for l in it.combinations(i, 2):
                if l[0] == l[1]:
                    if l[0] == 0:
                        a, b = solve(blue-2, red+1)
                        out[0] += a
                        out[1] += b
                    else:
                        a, b = solve(blue, red-1)
                        out[0] += a
                        out[1] += b
                else:
                    a, b = solve(blue, red-1)
                    out[0] += a
                    out[1] += b
            prev[tuple(i)] = out
            return out

if __name__ == "__main__":
    if len(argv) != 3:
        print("Špatný počet argumentů (3)")
        exit(1)
    else:
        o = solve(int(argv[1]), int(argv[2]))
        if o[0] > o[1]:
            print(f'Modrá({o[0]}:{o[1]})')
        elif o[0] < o[1]:
            print(f'Červená({o[0]}:{o[1]})')
        else:
            print(f'Stejně({o[0]}:{o[1]})')
