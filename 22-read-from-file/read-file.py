# These exercises taken from https://www.w3resource.com/python-exercises/file/

import os
import random
import re
import time

# Write a Python program to read an entire text file
def read_file(file_name):
    current_dir = os.path.dirname(__file__)
    input_file = os.path.join(current_dir, file_name)

    open_file = open(input_file)

    print(open_file.read())

    open_file.close()

# read_file('read-write-me.txt')

# Write a Python program to read first n lines of a file
def read_n_file(file_name, n_lines):
    current_dir = os.path.dirname(__file__)
    input_file = os.path.join(current_dir, file_name)

    with open(input_file) as open_file:
        iter = n_lines

        for line in open_file:
            if n_lines <= 0:
                break

            print(line.strip())
            n_lines -= 1

        open_file.close()

# read_n_file('read-write-me.txt', 2)

# Write a Python program to append text to a file and display the text
def append_file(file_name, input_text):
    current_dir = os.path.dirname(__file__)
    input_file = os.path.join(current_dir, file_name)

    with open(input_file, 'a+') as open_file:
        open_file.write(input_text + "\n")

        # Move file pointer back to start of file
        open_file.seek(0)

        # for line in open_file:
        #     print(line.strip())
        print(open_file.read())

        open_file.close()

# append_file('read-write-me.txt', 'Just one more line')

# Write a Python program to read last n lines of a file
def read_file_n(file_name, n_lines):
    current_dir = os.path.dirname(__file__)
    input_file = os.path.join(current_dir, file_name)

    # # Naive approach
    # # Requires enough memory to hold the entire file contents
    # file_list = []
    #
    # with open(input_file) as open_file:
    #     file_list = open_file.readlines()
    #
    #     open_file.close()
    #
    # # print(file_list[-n_lines:])
    # for line in file_list[-n_lines:]:
    #     print(line.strip())

    # Better approach - This solution started from https://www.w3resource.com/python-exercises/file/python-io-exercise-4.php
    # Get file size to make sure it will fit in memory before reading it
    # Buffer size set to two memory pages for 32-bit platforms to handle
    buffer_size = 8192
    # file_size = os.stat(input_file).st_size
    file_size = os.path.getsize(input_file)

    with open(input_file) as open_file:
        # Ensure file size is small enough to fit in system page buffer
        if buffer_size > file_size:
            buffer_size = file_size

        data = []
        # print(f'buffer_size: {buffer_size}, file_size: {file_size}')

        # print(f'tell position 1: {f.tell()}')
        # print(f'seek position: {file_size - buffer_size * iter}')
        open_file.seek(file_size - buffer_size)
        # print(f'tell position 2: {f.tell()}')

        data.extend(open_file.readlines())
        # print(f'data: {data}')

        if len(data) >= n_lines or open_file.tell() == 0:
            print(''.join(data[-n_lines:]))

        open_file.close()

    # If dealing with very large files and trying to conserve system memory,
    # the following might be more efficient
    # 1. Get the first n lines of the file and estimate the average number of
    #    chars per line
    # 2. Using the estimate from above, estimate how far from the end of the
    #    file we need to seek to in order to get the desired number of lines
    #
    #    For example, if we want the last 10 lines and we estimate 30 chars
    #    per line, seek to file_size - 10 * 30 and check to see if we were able
    #    to get the correct number of lines from that point
    #
    # Note: This could require multiple loops for trial and error if we do not
    #    get the correct number of lines on the first try due to inaccurate
    #    estimates of chars per line. Filling up the system page buffer would
    #    save time in this case.


# read_file_n('read-write-me.txt', 5)


def find_longest_word(file_name):
    current_dir = os.path.dirname(__file__)
    input_file = os.path.join(current_dir, file_name)

    buffer_size = 8192
    file_size = os.path.getsize(input_file)

    file_contents = ''
    file_words = []
    longest_word = ''
    longest_words = []
    max_length = 0

    with open(input_file) as open_file:
        if file_size <= buffer_size:
            # file_contents = open_file.readlines()
            file_contents = open_file.read()
            # print(file_contents)
            file_words = file_contents.split()

            # for word in file_words:
            #     if len(word) > len(longest_word):
            #         longest_word = word

            max_length = len(max(file_words, key=len))

        # else
        open_file.close()

    longest_words = [word for word in file_words if (len(word) == max_length)]

    print(longest_words)

    return longest_words

# find_longest_word('read-write-me.txt')



def count_lines(file_name):
    current_dir = os.path.dirname(__file__)
    input_file = os.path.join(current_dir, file_name)

    duration_time = -time.time()

    # buffer_size = 8192
    # file_size = os.path.getsize(input_file)

    line_count = 0

    with open(input_file, 'r') as open_file:
        # if buffer_size >= file_size:
        #     line_count = len(open_file.readlines())
        # More efficient solution from https://www.w3resource.com/python-exercises/file/python-io-exercise-9.php
        for idx, line in enumerate(open_file):
            pass

        line_count = idx + 1

        open_file.close()

    duration_time += time.time()
    print(f'Execution time: {duration_time}')

    return line_count

# print(count_lines('read-write-me.txt'))



def word_count(file_name):
    current_dir = os.path.dirname(__file__)
    input_file = os.path.join(current_dir, file_name)

    buffer_size = 8192
    file_size = os.path.getsize(input_file)

    word_dict = {}

    with open(input_file, 'r') as open_file:
        if buffer_size >= file_size:
            # words = open_file.read().split()
            words = open_file.read()
            words = re.split("[\s+.,]", words)
        # for line in open_file:
        #     words = line.split()

            for word in words:
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1

        open_file.close()

    return word_dict

# print(word_count('read-write-me.txt'))



def get_file_size(file_name):
    current_dir = os.path.dirname(__file__)
    input_file = os.path.join(current_dir, file_name)

    return os.path.getsize(input_file)

# print(get_file_size('read-write-me.txt'))



def random_lines(file_name):
    current_dir = os.path.dirname(__file__)
    input_file = os.path.join(current_dir, file_name)

    with open(input_file, 'r') as open_file:
        lines = open_file.readlines()

        return random.choice(lines)

# print(random_lines('read-write-me.txt'))



def count_words(file_name):
    current_dir = os.path.dirname(__file__)
    input_file = os.path.join(current_dir, file_name)

    with open(input_file) as open_file:
        content = open_file.read()
        content = content.replace(",", " ")
        
        return len(content.split())

        open_file.close()

print(count_words('test.txt'))
