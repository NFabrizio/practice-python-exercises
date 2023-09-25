import os
import random
import re
import string

def write_list(file_name, list_data):
    current_dir = os.path.dirname(__file__)
    input_file = os.path.join(current_dir, file_name)

    with open(input_file, 'w') as open_file:
        for item in list_data:
            open_file.write(f'{item}\n')

        open_file.close()

# write_list('test.txt', ['a', 'b', 'c'])

def copy_file(file_name_read, file_name_write):
    current_dir = os.path.dirname(__file__)
    input_file = os.path.join(current_dir, file_name_read)
    output_file = os.path.join(current_dir, file_name_write)

    buffer_size = 8192
    file_size = os.path.getsize(input_file)

    with open(input_file, "r") as read_file:
        if buffer_size >= file_size:
            contents = read_file.read()

            with open(output_file, "w") as write_file:
                write_file.write(contents)

                write_file.close()

        read_file.close()

# copy_file('read-write-me.txt', 'test.txt')



def combine_lines(file_name1, file_name2):
    current_dir = os.path.dirname(__file__)
    input_file1 = os.path.join(current_dir, file_name1)
    input_file2 = os.path.join(current_dir, file_name2)
    output_file = os.path.join(current_dir, 'combined.txt')

    with open(input_file1, "r") as open_file1, open(input_file2, "r") as open_file2, open(output_file, "a") as write_file:
        for (line1, line2) in zip(open_file1, open_file2):
            write_file.write(f'{line1.strip()} - {line2}')

        write_file.close()
        open_file2.close()
        open_file1.close()

# combine_lines('read-write-me.txt', 'test.txt')



def remove_new_lines(file_name):
    current_dir = os.path.dirname(__file__)
    input_file = os.path.join(current_dir, file_name)

    with open(input_file, "r+") as open_file:
        content = open_file.read()
        # print(content)
        content = re.sub("\n", "", content)
        print(content)

        open_file.seek(0)

        open_file.write(content)

        open_file.truncate()

        open_file.close()

# remove_new_lines('test.txt')



def create_alphabet_files():
    current_dir = os.path.dirname(__file__)
    letters_dir = os.path.join(current_dir, 'letters')

    if not os.path.isdir(letters_dir):
        os.makedirs(letters_dir)

    for letter in string.ascii_uppercase:
        file_name = os.path.join(letters_dir, f'{letter}.txt')

        with open(file_name, 'a') as open_file:
            open_file.writelines(letter)
            open_file.close()

create_alphabet_files()
