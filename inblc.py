import pprint


def read_input(file):
    print(file)
    env = dict()
    with open(file, mode='r') as input_file:
        line = input_file.readline()
        nb_photos = line.strip('\n')
        env['nb_photos'] = int(nb_photos)
        env['photos'] = list()
        env['slides'] = list()
        for n in range(env['nb_photos']):
            line = input_file.readline()
            line = line.strip('\n')
            line = line.split(' ')
            photo = dict()
            photo['id'] = n
            photo['direction'] = line[0]
            photo['tags'] = list()
            nb_tags = int(line[1])
            for m in range(nb_tags):
                photo['tags'].append(line[2 + m])
            env['photos'].append(photo)
    return env


if __name__ == "__main__":
    lol = read_input('input/a_example.txt')
    pprint.pprint(lol)
