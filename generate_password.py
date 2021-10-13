#!/usr/bin/env python3
import random
import argparse
from string import digits, ascii_letters


def main():
    parser = argparse.ArgumentParser(
        description='Generate alphanumeric password of given length.')
    parser.add_argument('-n', help='Password length, default is 10.',
        required=False, default=10)
    args = parser.parse_args()

    chars = digits + ascii_letters

    print(''.join(random.choices(chars, k=args.n)))


if __name__ == "__main__":
    main()
