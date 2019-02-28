from inblc import read_input
from outblc import write_output
import sys
import os


def do_something(env):
    return env


dirs = os.listdir("input")
for file in dirs:
    env = read_input('input/' + file)
    filename = file.split('.')
    env = do_something(env)
    write_output('output/' + filename[0] + ".out", env)


