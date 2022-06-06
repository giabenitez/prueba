import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.parrow("hello, "+ sys.argv[1])