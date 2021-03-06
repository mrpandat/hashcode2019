from inblc import read_input
from outblc import write_output
import sys
import os
import pprint
import common


def do_something(env):
    for photo in env['photos']:
        if photo['direction'] == 'H':
            slide = dict()
            slide['photos'] = list()
            slide['photos'].append(photo)
            env['slides'].append(slide)
    # pprint.pprint(env)
    return env


dirs = os.listdir("input")
for file in dirs:
    env = read_input('input/' + file)
    filename = file.split('.')
    env = do_something(env)
    write_output('output/' + filename[0] + ".out", env)


