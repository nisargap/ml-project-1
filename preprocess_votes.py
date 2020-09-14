# Author: Nisarga Patel
# Language: Python 3
# Class: Introduction to Machine Learning
# Description: This file defines a pre-processing function for the votes data
import random

"""

4. Relevant Information:
      This data set includes votes for each of the U.S. House of
      Representatives Congressmen on the 16 key votes identified by the
      CQA.  The CQA lists nine different types of votes: voted for, paired
      for, and announced for (these three simplified to yea), voted
      against, paired against, and announced against (these three
      simplified to nay), voted present, voted present to avoid conflict
      of interest, and did not vote or otherwise make a position known
      (these three simplified to an unknown disposition).

5. Number of Instances: 435 (267 democrats, 168 republicans)

6. Number of Attributes: 16 + class name = 17 (all Boolean valued)

7. Attribute Information:
   1. Class Name: 2 (democrat, republican)
   2. handicapped-infants: 2 (y,n)
   3. water-project-cost-sharing: 2 (y,n)
   4. adoption-of-the-budget-resolution: 2 (y,n)
   5. physician-fee-freeze: 2 (y,n)
   6. el-salvador-aid: 2 (y,n)
   7. religious-groups-in-schools: 2 (y,n)
   8. anti-satellite-test-ban: 2 (y,n)
   9. aid-to-nicaraguan-contras: 2 (y,n)
  10. mx-missile: 2 (y,n)
  11. immigration: 2 (y,n)
  12. synfuels-corporation-cutback: 2 (y,n)
  13. education-spending: 2 (y,n)
  14. superfund-right-to-sue: 2 (y,n)
  15. crime: 2 (y,n)
  16. duty-free-exports: 2 (y,n)
  17. export-administration-act-south-africa: 2 (y,n)

8. Missing Attribute Values: Denoted by "?"

   NOTE: It is important to recognize that "?" in this database does
         not mean that the value of the attribute is unknown.  It
         means simply, that the value is not "yea" or "nay" (see
         "Relevant Information" section above).

   Attribute:  #Missing Values:
           1:  0
           2:  0
           3:  12
           4:  48
           5:  11
           6:  11
           7:  15
           8:  11
           9:  14
          10:  15
          11:  22
          12:  7
          13:  21
          14:  31
          15:  25
          16:  17
          17:  28
"""
POSSIBLE_CLASSES = {
    "democrat": 1,
    "republican": 0
}


def preprocess_votes(line):
    line_arr = line.rstrip().split(",")
    classification = line_arr[0]
    attrs = line_arr[1:]
    vals = []
    for index, value in enumerate(attrs):
        if value == "y":
            vals.append(1)
        elif value == "n":
            vals.append(0)
        elif value == "?":
            rand = random.randint(0, 1)
            vals.append(rand)
    vals.append(POSSIBLE_CLASSES[classification])
    return vals
