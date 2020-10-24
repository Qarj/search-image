# search-image.py 0.3.2

A snippet of code was posted on stack overflow on how to find one image inside another. The question is here: http://stackoverflow.com/questions/4720168/image-in-image-algorithm

search-image.py implements this and also optionally draws a red rectangle around the location of the found image.

This script can be used as part of an automated regression testing framework to check for browser compatibility issues. For a responsive website you could check that the right version of the controls are being shown for a given horizontal resolution.


## Usage

```
search-image.py target_image.png image_to_find.png [markfile.png]
```

A number of image files are included which you can use with the following examples.

### Example 1

```
python search-image.py examples/100-orig.png examples/menu_hamburger.png
```

### Example 2

```
cp examples/100-orig.png marked.png
python search-image.py examples/100-orig.png examples/menu_hamburger.png marked.png
python search-image.py examples/100-orig.png examples/content_vertical_mobile.png marked.png
```

View `marked.png` (using Ubuntu)

```
eog marked.png
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


## Linux Installation

Download `Miniconda3-latest-Linux-x86_64.sh`

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -P ~/Downloads/
```

Intall Miniconda, accept all defaults (press space a few times when in `more`)

```bash
cd ~/Downloads
bash Miniconda3-latest-Linux-x86_64.sh
```

Activate Conda

```bash
eval "$(/home/$USERNAME/miniconda3/bin/conda shell.bash hook)"
conda init
```

Close shell prompt and open a fresh one.

At time of writing the conda version of opencv is not compatible with Python 3.8, so use 3.7.

```bash
conda create -n cv python=3.7.9
conda activate cv
python --version
.
Python 3.7.9
```

Now install dependencies

```bash
conda install opencv
conda install Pillow
```

Clone the repo and test

```bash
mkdir ~/git
cd ~/git
git clone https://github.com/Qarj/search-image.git
cd search-image
python search-image.py
.
Specify target image, followed by the image to search for.
Example: search-image.py target_image.png image_to_find.png [markfile.png]
```


## Windows Installation

Open a command prompt

```
cd %userprofile%/Downloads
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe --output %userprofile%/Downloads/miniconda.exe
```

Install miniconda, be sure to install for current user only, not all users. No need to add to path.
```
miniconda.exe
```

Now start the `Anaconda Prompt (miniconda3)` from the Start menu

We want to create a Python 3.7 environment (Miniconda Python 3.8 incompatible with opencv at time of writing)
```
conda create -n cv python=3.7.9
conda activate cv
python --version
.
Python 3.7.9
```

Now install dependencies

```
conda install opencv
conda install Pillow
```

Clone the repo and test

```
mkdir C:\git
cd C:\git
git clone https://github.com/Qarj/search-image.git
cd search-image
python search-image.py
.
Specify target image, followed by the image to search for.
Example: search-image.py target_image.png image_to_find.png [markfile.png]
```

## Additional Information

How template matching works:
http://opencv.itseez.com/doc/tutorials/imgproc/histograms/template_matching/template_matching.html

Fast image comparison with python (server down on last check):
See http://aatiis.me/2010/08/12/fast-image-comparison-with-python.html
