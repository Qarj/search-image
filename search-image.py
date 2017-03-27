#!/usr/bin/env python2.7

# version 0.2.0

# http://stackoverflow.com/questions/4720168/image-in-image-algorithm

#find the image_to_find inside the target_image, if found optionally mark a rectangle on markfile
import sys, subprocess, cv
from PIL import Image, ImageDraw

if (len(sys.argv) > 2):
   print sys.argv[1], sys.argv[2]
   target_image = sys.argv[1]
   image_to_find = sys.argv[2]
else:
   print 'Specify target image, followed by the image to search for.'
   print 'Example: search-image.py target_image.png image_to_find.png [markfile.png]'
   sys.exit()

# Example 1:
# search-image.py examples\100-orig.png examples\menu_hamburger.png
#
# Example 2:
# copy examples\100-orig.png marked_result.png
# search-image.py examples\100-orig.png examples\menu_hamburger.png marked_result.png

print '\nSTEP 1: Load images and get dimensions - x,y'

im = cv.LoadImage(target_image)
tmp = cv.LoadImage(image_to_find)

image_size = cv.GetSize(im)
template_size = cv.GetSize(tmp)

print 'DEBUG:image_size', image_size
print 'DEBUG:template_size', template_size
print ('DEBUG:image_size is of type', type(image_size))

print '\nSTEP 2: Calculate result_size'

result_size = [ s[0] - s[1] + 1 for s in zip(image_size, template_size) ]

print 'DEBUG:result_size - x,y', result_size

print '\nSTEP 3: Use Computer Vision to create a result image of the desired result_size'

print 'DEBUG:CreateImage doco:', cv.CreateImage.__doc__

result = cv.CreateImage(result_size, cv.IPL_DEPTH_32F, 1)

print 'DEBUG:result', result

print "\n"

#CV_TM_SQDIFF is the match method, smaller min_val means better match. min_loc is the best match location
#with other matching methods you need to look at max_val and max_loc
#http://opencv.itseez.com/doc/tutorials/imgproc/histograms/template_matching/template_matching.html
#http://docs.opencv.org/doc/tutorials/imgproc/histograms/template_matching/template_matching.html
cv.MatchTemplate(im, tmp, result, cv.CV_TM_SQDIFF)
min_val, max_val, min_loc, max_loc = cv.MinMaxLoc(result)

print 'result', result
print 'min_val', min_val
print 'max_val', max_val
print 'min_loc', min_loc, 'X'
print 'max_loc', max_loc

confidence = (9999999999 - min_val) / 100000000
print 'primary confidence', '%.2f %%' % confidence

altconfidence = 100 - ((min_val / max_val)*100)
print 'alternate confidence', '%.2f %%' % altconfidence

topleftx = min_loc[0]
toplefty = min_loc[1]
sizex = template_size[0]
sizey = template_size[1]

if (altconfidence > 99) or ((confidence > 97) and (altconfidence > 93)) or ((confidence > 95.7) and (altconfidence > 96.3)):
   print 'The image of size', template_size, 'was found at', min_loc
   if (len(sys.argv) > 3):
      print 'Marking', sys.argv[3], 'with a red rectangle'
      marked = Image.open(sys.argv[3])
      draw = ImageDraw.Draw(marked)
      draw.line(((topleftx,         toplefty),         (topleftx + sizex, toplefty)),           fill="red", width=2)
      draw.line(((topleftx + sizex, toplefty),         (topleftx + sizex, toplefty + sizey)),   fill="red", width=2)
      draw.line(((topleftx + sizex, toplefty + sizey), (topleftx,         toplefty + sizey)),   fill="red", width=2)
      draw.line(((topleftx,         toplefty + sizey), (topleftx,         toplefty)),           fill="red", width=2)
      del draw 
      marked.save(sys.argv[3], "PNG")
else:
   print 'The image was not found'

