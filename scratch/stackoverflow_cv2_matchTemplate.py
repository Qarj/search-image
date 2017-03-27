#!/usr/bin/env python3

# on stackoverflow, this solution apparently works for Python 2.7
# http://stackoverflow.com/questions/35642497/python-opencv-cv2-matchtemplate-with-transparency
# with Python 3 we get an error with numpy

import cv2
import numpy as np
import sys

if len(sys.argv) < 3:
    print ('Usage: python match.py <template.png> <image.png>')
    sys.exit()

template_path = sys.argv[1]
template = cv2.imread(template_path, cv2.IMREAD_UNCHANGED)
channels = cv2.split(template)
zero_channel = np.zeros_like(channels[0])
mask = np.array(channels[3])

image_path = sys.argv[2]
image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

mask[channels[3] == 0] = 1
mask[channels[3] == 100] = 0

# transparent_mask = None
# According to http://www.devsplanet.com/question/35658323, we can only use
# cv2.TM_SQDIFF or cv2.TM_CCORR_NORMED
# All methods can be seen here:
# http://docs.opencv.org/2.4/doc/tutorials/imgproc/histograms/template_matching/template_matching.html#which-are-the-matching-methods-available-in-opencv
method = cv2.TM_SQDIFF  # R(x,y) = \sum _{x',y'} (T(x',y')-I(x+x',y+y'))^2 (essentially, sum of squared differences)

transparent_mask = cv2.merge([zero_channel, zero_channel, zero_channel, mask])
result = cv2.matchTemplate(image, template, method, mask=transparent_mask)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
print ('Lowest squared difference WITH mask', min_val)

# Now we'll try it without the mask (should give a much larger error)
transparent_mask = None
result = cv2.matchTemplate(image, template, method, mask=transparent_mask)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
print ('Lowest squared difference WITHOUT mask', min_val)