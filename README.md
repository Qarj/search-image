# search-image.py 0.2.0

A snippet of code was posted on stack overflow on how to find one image inside another. The question is here: http://stackoverflow.com/questions/4720168/image-in-image-algorithm

search-image.py implements this and also optionally draws a red rectangle around the location of the found image.

This script can be used as part of an automated regression testing framework to check for browser compatibility issues. For a responsive website you could check that the right version of the controls are being shown for a given horizontal resolution.

## Windows Installation

1. Install 32-bit python-2.7.11.msi from
   https://www.python.org/downloads/release/python-2711/

   Choose the option to install `python.exe` in the path which will ensure that `C:\Python` and `C:\Python\Scripts` are added to the path for you

2. Ensure pip is up to date
    ```
    python -m pip install --upgrade pip
    ```

3. Download python bindings for OpenCV, `opencv_python-2.4.13-cp27-cp27m-win32.whl`, from http://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv and install
    ```
    pip install opencv_python-2.4.13-cp27-cp27m-win32.whl
    ```

4. Download numpy, `numpy-1.10.4+mkl-cp27-cp27m-win32.whl`, from http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy and install
    ```
    pip install numpy-1.10.4+mkl-cp27-cp27m-win32.whl
    ```

4. Download Python Image Library, Python Imaging Library 1.1.7 for Python 2.7, from http://www.pythonware.com/products/pil/ and install
   (the exe is `PIL-1.1.7.win32-py2.7.exe`)

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
