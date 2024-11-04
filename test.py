#!/bin/env python3

import subprocess
import sys

proc = subprocess.run([sys.argv[1]], capture_output=True, shell=True, check=True)
assert proc.stdout == b"Hello, World!\n"
