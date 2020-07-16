#!/usr/bin/env python3

import wttrpy, argparse
parser = argparse.ArgumentParser()
parser.add_argument('--location', '-w', help="Set location")
parser.add_argument('--locale', '-l', help="Set locale")
args = parser.parse_args()

print(wttrpy.getWttr(args.location, args.locale))