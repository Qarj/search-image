# search-image.py

A snippet of code was posted on stack overflow on how to find one image inside another. The question is here: http://stackoverflow.com/questions/4720168/image-in-image-algorithm

search-image.py implements this and also optionally draws a red rectangle around the location of the found image.

This script can be used as part of an automated regression testing framework to check for browser compatibility issues. For a responsive website you could check that the right version of the controls are being shown for a give horizontal resolution.

## Windows Installation

1. Install 32-bit python-2.6.6.msi
   https://www.python.org/download/releases/2.6.6/

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

## Usage

```
search-image.py target_image.png image_to_find.png [markfile.png]
```

A number of image files are included which you can use with the following examples.

### Example 1

```
search-image.py examples\100-orig.png examples\menu_hamburger.png
```

### Example 2

```
copy examples\100-orig.png marked_result.png
search-image.py examples\100-orig.png examples\menu_hamburger.png marked_result.png
search-image.py examples\100-orig.png examples\content_vertical_mobile.png marked_result.png
```

In this example we are trying to find the hamburger menu control

![Alt text](examples/menu_hamburger.png?raw=true "Hamburger Menu Control")

and also the vertical content

![Alt text](examples/content_vertical_mobile.png?raw=true "Vertical Content")

inside the target image (Selenium WebDriver screen shot)

![Alt text](examples/100-orig.png?raw=true "Mobile View")

We made a copy of this screen shot and search-image.py marked the found locations:

![Alt text](examples/100-marked.png?raw=true "Hamburger Menu Control")


## Caution!

The Open Source Computer Vision (OpenCV) library returns the co-ordinates where the best match is found. It will always return co-ordinates regardless of whether the target image really exists or not. It also returns some numbers representing how confident it is that it found the match - the "primary confidence" and the "alternate confidence".

If you set the threshold too high (100% match), then even very minor changes in how a browser renders the control will result in non matches.

On the other hand, if you set the threshold too low, then you will find matches that do not in fact exist!

After a lot of experimentation with regression testing over the years I have come up with some numbers that seem to work well for the image found threshold.

You may need to update the threshold based on your own use cases.

## Additional Information

How template matching works:
http://opencv.itseez.com/doc/tutorials/imgproc/histograms/template_matching/template_matching.html

Fast image comparison with python (server down on last check):
See http://aatiis.me/2010/08/12/fast-image-comparison-with-python.html
