# Author: Nisarga Patel
# Language: Python 3 
# Class: Introduction to Machine Learning
# Description: This file pre-processes each dataset
import os
from preprocessutils import processfile
from preprocess_breastcancer import preprocess_breast_cancer
from preprocess_glass import preprocess_glass
from preprocess_iris import preprocess_iris

def process():
    filemap = {
        "raw/breastcancer-unprocessed.data": {
            "filename": "processed/breastcancer-processed.data",
            "processor": preprocess_breast_cancer
        },
        "raw/glass-unprocessed.data": {
            "filename": "processed/glass-processed.data",
            "processor": preprocess_glass
        },
        "raw/iris-unprocessed.data": {
            "filename": "processed/iris-processed.data",
            "processor": preprocess_iris
        }
    }
    for raw_file in filemap:
        processed_file = filemap[raw_file]["filename"]
        if os.path.exists(processed_file):  
            os.remove(processed_file)
        processfile(raw_file, processed_file, filemap[raw_file]["processor"])

process()