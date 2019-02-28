def write_output(file, env):
    with open(file, 'w') as output_file:
        output_file.write(str(len(env['slides'])) + '\n')
        for slide in env['slides']:
            for index, photo in enumerate(slide['photos']):
                slide['photos'][index] = str(photo)
            line = ' '.join(slide['photos']) + '\n'
            output_file.write(line)
