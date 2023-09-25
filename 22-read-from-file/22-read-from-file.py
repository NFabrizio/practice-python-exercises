import os

def read_from_file(file_name):
    name_dict = {}
    current_dir = os.path.dirname(__file__)
    absolute_file_path = os.path.join(current_dir, file_name)

    with open(absolute_file_path, 'r') as open_file:
        # Process each line as it is read to conserve memory
        for line in open_file:
            line = line.rstrip()

            if line in name_dict:
                name_dict[line] += 1
            else:
                name_dict[line] = 1

        open_file.close()

    print(name_dict)

def read_from_file_extra(file_name):
    name_dict = {}
    current_dir = os.path.dirname(__file__)
    absolute_file_path = os.path.join(current_dir, file_name)

    with open(absolute_file_path, 'r') as open_file:
        for line in open_file:
            line_exploded = line.split('/')
            category = line_exploded[2]

            if category in name_dict:
                name_dict[category] += 1
            else:
                name_dict[category] = 1

        open_file.close()

    print(name_dict)


read_from_file('star_wars_names.txt')
# read_from_file_extra('sun_files.txt')
