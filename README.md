# OpenDocument Page Creator

Script to replace the background page style picture with an other one.

Reads in files from `input` folder and puts them to `output` folder.

Background picture was created with:

    $ convert -size 2226x3392 canvas: white.png
    $ convert -border 5x5 -bordercolor "#FF0000" white.png  white-with-red-frame.png
    $ file white-with-red-frame.png 
    white-with-red-frame.png: PNG image data, 2236 x 3402, 1-bit colormap, non-interlaced
