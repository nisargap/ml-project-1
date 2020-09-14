# Author: Nisarga Patel
# Language: Python 3
# Class: Introduction to Machine Learning
# Description: This file defines a pre-processing function for the glass data
from preprocessutils import get_bucket_for_value

'''
Relevant info from the names file
   2. RI: refractive index
   3. Na: Sodium (unit measurement: weight percent in corresponding oxide, as
                  are attributes 4-10)
   4. Mg: Magnesium
   5. Al: Aluminum
   6. Si: Silicon
   7. K: Potassium
   8. Ca: Calcium
   9. Ba: Barium
  10. Fe: Iron
  11. Type of glass: (class attribute)
      -- 1 building_windows_float_processed
      -- 2 building_windows_non_float_processed
      -- 3 vehicle_windows_float_processed
      -- 4 vehicle_windows_non_float_processed (none in this database)
      -- 5 containers
      -- 6 tableware
      -- 7 headlamps
  Attribute:   Min     Max      Mean     SD      Correlation with class
 2. RI:       1.5112  1.5339   1.5184  0.0030  -0.1642
 3. Na:      10.73   17.38    13.4079  0.8166   0.5030
 4. Mg:       0       4.49     2.6845  1.4424  -0.7447
 5. Al:       0.29    3.5      1.4449  0.4993   0.5988
 6. Si:      69.81   75.41    72.6509  0.7745   0.1515
 7. K:        0       6.21     0.4971  0.6522  -0.0100
 8. Ca:       5.43   16.19     8.9570  1.4232   0.0007
 9. Ba:       0       3.15     0.1750  0.4972   0.5751
10. Fe:       0       0.51     0.0570  0.0974  -0.1879
'''

MIN_RI = 1.5112
MIN_NA = 10.73
MIN_MG = 0
MIN_AL = 0.29
MIN_SI = 69.81
MIN_K = 0
MIN_CA = 5.43
MIN_BA = 0
MIN_FE = 0


# using min boundary based equal width buckets
def preprocess_glass(line):
    line_arr = line.rstrip().split(",")[1:]
    attrs = line_arr[0:-1]
    classification = line_arr[-1]
    vals = []
    for index, val in enumerate(attrs):
        if index == 0:
            # Bucket RI by equal sized intervals 5
            diff_from_min = (float(val) - MIN_RI) * 100
            inx = abs(round(diff_from_min * 5)) % 5
            bucket = get_bucket_for_value(inx, 5)
            vals += bucket
        if index == 1:
            # Bucket Na
            diff_from_min = (float(val) - MIN_NA)
            inx = abs(round(diff_from_min))
            bucket = get_bucket_for_value(inx, 10)
            vals += bucket
        if index == 2:
            # Bucket Mg, bucket size = 5
            diff_from_min = (float(val) - MIN_MG)
            inx = abs(round(diff_from_min))
            bucket = get_bucket_for_value(inx, 5)
            vals += bucket
        if index == 3:
            # Bucket Al
            # Max value = 3, choose bucket size 4
            diff_from_min = (float(val) - MIN_AL)
            inx = abs(round(diff_from_min))
            bucket = get_bucket_for_value(inx, 4)
            vals += bucket
        if index == 4:
            # Bucket Si, multiply by 100 to not lose decimal precision
            # setting a fixed bucket size of 50
            diff_from_min = (float(val) - MIN_SI) * 100
            inx = abs(round(diff_from_min)) % 50
            bucket = get_bucket_for_value(inx, 50)
            vals += bucket
        if index == 5:
            # Bucket K
            # setting bucket size = 7, since max is 6
            diff_from_min = (float(val) - MIN_K)
            inx = abs(round(diff_from_min))
            bucket = get_bucket_for_value(inx, 10)
            vals += bucket
        if index == 6:
            # Bucket Ca
            # setting bucket size = 12
            diff_from_min = (float(val) - MIN_CA)
            inx = abs(round(diff_from_min))
            bucket = get_bucket_for_value(inx, 12)
            vals += bucket
        if index == 7:
            # Bucket Ba
            # setting bucket size = 4
            diff_from_min = (float(val) - MIN_BA)
            inx = abs(round(diff_from_min))
            bucket = get_bucket_for_value(inx, 4)
            vals += bucket
        if index == 8:
            # Bucket Fe
            diff_from_min = (float(val) - MIN_FE) * 100
            inx = abs(round(diff_from_min)) % 50
            bucket = get_bucket_for_value(inx, 50)
            vals += bucket
    vals.append(int(classification) - 1)
    return vals
