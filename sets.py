#!/usr/bin/env python3
import re, os

DEBUG = bool(os.getenv("DEBUG"))

def read_file_as_set(path) -> set:
    with open(path) as f:
        return set(x.strip() for x in f.readlines())

s = read_file_as_set


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('expression', help="expression of operations over files which contains set of lines. e.g. 'names_boy & names_girl'")
    parser.add_argument('-s', '--sort', action='store_true', help="sort result")
    args = parser.parse_args()

    exp = args.expression + ' '
    exp2 = re.sub(r'([a-zA-Z0-9/-_.]+) ', r's("\1") ', exp)
    if DEBUG:
        print("expression:", exp2)
    result = eval(exp2)
    if DEBUG:
        print("result:", result)
    if args.sort:
        print('\n'.join(sorted(result)))
    else:
        print('\n'.join(result))

if __name__ == '__main__':
    main()
