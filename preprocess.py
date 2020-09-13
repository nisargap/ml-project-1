# Author: Nisarga Patel
# Language: Python 3 
# Class: Introduction to Machine Learning
# Description: This file pre-processes each dataset
import random
import os
from preprocessutils import processfile
from preprocess_breastcancer import preprocess_breast_cancer

def process():
    filemap = {
        "raw/breastcancer-unprocessed.data": {
            "filename": "processed/breastcancer-processed.data",
            "processor": preprocess_breast_cancer
        }
    }
    for raw_file in filemap:
        processed_file = filemap[raw_file]["filename"]
        if os.path.exists(processed_file):  
            os.remove(processed_file)
        processfile(raw_file, processed_file, filemap[raw_file]["processor"])

process()