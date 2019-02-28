def write_output(file, env):
    with open(file, 'w') as output_file:
        output_file.write(str(len(env['slides'])) + '\n')
        for slide in env['slides']:
            line = ''
            for index, photo in enumerate(slide['photos']):
                line += str(photo['id']) + ' '
            line.strip(' ')
            line += '\n'
            output_file.write(line)
