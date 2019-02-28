from inblc import read_input
from outblc import write_output
import sys
import os
import pprint
import numpy as np


def sort_orientation(photos):
    photos_res = {
        "V": [],
        "H": []
    }

    for photo in photos:
        if (photo['direction'] == "H"):
            photos_res['H'].append(photo)
        else:
            photos_res['V'].append(photo)

    return photos_res


def calc_score(photo1, photo2):
    if (photo1['id'] == photo2['id']):
        return 0

    common_els = np.intersect1d(photo1['tags'], photo2['tags'],  True).size

    if (common_els == 0):
        return 0

    uncommon_els1 = np.setdiff1d(photo1['tags'], photo2['tags'], True).size

    if (uncommon_els1 == 0):
        return 0

    uncommon_els2 = np.setdiff1d(photo2['tags'], photo1['tags'], True).size


    return min([common_els, uncommon_els1, uncommon_els2])


def do_something(env):

    for photo1 in env['photos']:
        if photo1['direction'] == 'V':
            continue
        slide = dict()
        slide['photos'] = list()
        print(photo1["id"])
        top_score = 0
        top_photo = []

        if photo1["id"] > 1000:
            break

        slide['photos'].append(photo1)
        env['slides'].append(slide)
        i = 0
        for photo2 in env['photos']:

            if photo2['direction'] == 'V':
                continue
            if photo1['id'] == photo2['id']:
                continue

            i = i + 1

            score = calc_score(photo1, photo2)

            if score > top_score:
                top_score = score
                top_photo = photo2

            if (top_score > 0):
                if (top_photo == []):
                    top_photo = photo2
                slide = dict()
                slide['photos'] = list()
                slide['photos'].append(top_photo)
                env['slides'].append(slide)
                break


    return env

'''
dirs = os.listdir("input")
for file in dirs:
    env = read_input('input/' + file)
    filename = file.split('.')
    env = do_something(env)
    write_output('output/' + filename[0] + ".out", env)

'''


env = read_input('input/b_lovely_landscapes.txt')
filename ="b_lovely_landscapes."
env = do_something(env)
write_output('output/b_lovely_landscapes.out', env)

