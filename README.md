# search-image.py

A snippet of code was posted on stack overflow on how to find one image inside another. The question is here: http://stackoverflow.com/questions/4720168/image-in-image-algorithm

search-image.py implements this and also optionally draws a red rectangle around the location of the found image.

This script can be used as part of an automated regression testing framework to check for browser compatibility issues. For a responsive website you could check that the right version of the controls are being shown for a give horizontal resolution.

## Windows Installation

1. Install python-2.6.6.msi

2. Install opencv-python-2.4.1.win32-py2.6.exe
python bindings for OpenCV
http://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv

3. Install numpy-1.6.1-win32-superpack-python2.6.exe

4. Install python-Levenshtein-0.10.1.win32-py2.6.exe

5. Install PIL-1.1.7.win32-py2.6.exe - Python Image Library

6. Check the Environment Variables

   In the Path, C:\Python26\; should be before other versions of Python

   Ensure PYTHONHOME=C:\Python26\ for imageinimage.py to work

Note that last time I checked (years ago), versions of Python newer than 2.6.x (e.g. 2.7.x or 3.x.x)
will not work. This is due to dependencies in the libraries. Python 3.x is also not backwards
compatible - the print command has been turned into a function for example.

## Additional Information

How template matching works:
http://opencv.itseez.com/doc/tutorials/imgproc/histograms/template_matching/template_matching.html

Fast image comparison with python (server down on last check):
See http://aatiis.me/2010/08/12/fast-image-comparison-with-python.html
