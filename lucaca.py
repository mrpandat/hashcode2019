from inblc import read_input
from outblc import write_output
import sys
import os
import pprint
import common


def do_something(env):
    for index, photo in enumerate(env['photos']):
        if photo['direction'] == 'H':
            slide = dict()
            slide['photos'] = list()
            slide['photos'].append(photo)
            env['slides'].append(slide)
    slide = dict()
    slide['photos'] = list()
    for index, photo in enumerate(env['photos']):
        if photo['direction'] == 'V':
            slide['photos'].append(photo)
            if len(slide['photos']) > 1:
                env['slides'].append(dict(slide))
                slide = dict()
                slide['photos'] = list()
    # pprint.pprint(env)
    return env


dirs = os.listdir("input")
for file in dirs:
    env = read_input('input/' + file)
    filename = file.split('.')
    env = do_something(env)
    write_output('output/' + filename[0] + ".out", env)


