# Author: Nisarga Patel
# Language: Python 3
# Class: Introduction to Machine Learning
# Description: This file defines pre-processing for the breast cancer dataset

import random


# use one-hot coding to return a bucket of 10 bool values, since values range from 1-10
def get_bucket_for_breast_cancer_attr(x):
    # each value is placed in a binary bucket of sized 10
    b = [0 for i in range(10)]
    if x == "?":
        rand = random.randint(1, 10)
        b[rand - 1] = 1
        return b
    else:
        b[int(x) - 1] = 1
        return b


def preprocess_breast_cancer(line):
    # get line split by , with no starting id
    arr = line.rstrip().split(",")[1:]
    attrs = arr[0:-1]
    classification = int(arr[-1])
    new_arr = []
    for i in attrs:
        binary_bucket = get_bucket_for_breast_cancer_attr(i)
        new_arr += binary_bucket
    if classification == 4:
        new_arr.append(1)
    else:
        new_arr.append(0)
    return new_arr