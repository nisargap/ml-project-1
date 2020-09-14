# Author: Nisarga Patel
# Language: Python 3
# Class: Introduction to Machine Learning
# Description: This file defines a pre-processing function for the iris data
from preprocessutils import get_bucket_for_value


'''
Relevant info from names file
7. Attribute Information:
   1. sepal length in cm
   2. sepal width in cm
   3. petal length in cm
   4. petal width in cm
   5. class: 
      -- Iris Setosa
      -- Iris Versicolour
      -- Iris Virginica

8. Missing Attribute Values: None

Summary Statistics:
	             Min  Max   Mean    SD   Class Correlation
   sepal length: 4.3  7.9   5.84  0.83    0.7826   
    sepal width: 2.0  4.4   3.05  0.43   -0.4194
   petal length: 1.0  6.9   3.76  1.76    0.9490  (high!)
    petal width: 0.1  2.5   1.20  0.76    0.9565  (high!)
'''

MIN_SEPAL_LEN = 4.3
MIN_SEPAL_WIDTH = 2.0
MIN_PETAL_LEN = 1.0
MIN_PETAL_WIDTH =  0.1

POSSIBLE_CLASSES = {
    "Iris-setosa": 0,
    "Iris-versicolor": 1,
    "Iris-virginica": 2
}

def preprocess_iris(line):
    # sample line: 5.1,3.5,1.4,0.2,Iris-setosa
    line_arr = line.rstrip().split(",")
    classification = line_arr[-1]
    attrs = line_arr[0:-1]
    vals = []
    for index, value in enumerate(attrs):
        if index == 0:
            diff_from_min = abs(round(float(value) - MIN_SEPAL_LEN))
            bucket = get_bucket_for_value(diff_from_min, 5)
            vals += bucket
        if index == 1:
            diff_from_min = abs(round(float(value) - MIN_SEPAL_WIDTH))
            bucket = get_bucket_for_value(diff_from_min, 5)
            vals += bucket
        if index == 2:
            diff_from_min = abs(round(float(value) - MIN_PETAL_LEN))
            bucket = get_bucket_for_value(diff_from_min, 7)
            vals += bucket
        if index == 3:
            diff_from_min = abs(round(float(value) - MIN_PETAL_WIDTH))
            bucket = get_bucket_for_value(diff_from_min, 5)
            vals += bucket
    vals.append(POSSIBLE_CLASSES[classification])
    return vals