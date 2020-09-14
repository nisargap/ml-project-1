# Author: Nisarga Patel
# Language: Python 3
# Class: Introduction to Machine Learning
# Description: This provides utils for preprocessing the datasets
import random


def processfile(rawfilename, processedfilename, processfunc):
    # store the data to be written
    data_to_write = []
    with open(rawfilename) as r:
        for line in r.readlines():
            new_arr = processfunc(line)
            data_to_write.append(str(new_arr)[1:-1].replace(" ", "")+"\n")
    with open(processedfilename, "a+") as w:
        # randomize the order of items to write to the file
        random.shuffle(data_to_write)
        for line in data_to_write:
            w.write(line)


def get_bucket_for_value(one_index, bucket_size):
    bucket = [0 for i in range(bucket_size)]
    bucket[one_index] = 1
    return bucket