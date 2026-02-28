Title: Movie Color Visualization
Date: 2013-02-04
Tags: HPC, researchblog, Migration

Blog post **edited** by Anonymous \- "Migrated to Confluence 4.0"

As part of my work with the Campus Champion Fellowship I have been asked to
look into methods for displaying color for an entire movie similar to the
following:

[ColourSpectrograms](http://www.garethwilliamsportfolio.com/?page_id=55)  
[MovieBarCode](http://moviebarcode.tumblr.com/)

I tried installing the ColourSpectrograms java software but had some trouble.
So, I tried implimenting an algorithm myself. The following are my results so
far:

Average Image|HSV Video Colormap|Average Bar|Link to video  
  
---|---|---|---  
  
![](https://wiki.hpcc.msu.edu/download/attachments/5411567/[GlobusOnline_mean.png](./images/GlobusOnline_mean.png)?version=1&modificationDate=1359575480000&api=v2)|![](https://wiki.hpcc.msu.edu/download/attachments/5411567/[GlobusOnline_bar.png](./images/GlobusOnline_bar.png)?version=1&modificationDate=1359575480000&api=v2)|![](https://wiki.hpcc.msu.edu/download/attachments/5411567/[GlobusOnline_Abar.png](./images/GlobusOnline_Abar.png)?version=1&modificationDate=1359600408000&api=v2)|[Video Tutorial -
GlobusOnline.org](https://wiki.hpcc.msu.edu/display/ITH/Video+Tutorial+-+GlobusOnline.org)  
  
![](https://wiki.hpcc.msu.edu/download/attachments/5411567/[HPCCUSB_mean.png](./images/HPCCUSB_mean.png)?version=1&modificationDate=1359575480000&api=v2)|![](https://wiki.hpcc.msu.edu/download/attachments/5411567/[HPCCUSB_Bar.png](./images/HPCCUSB_Bar.png)?version=1&modificationDate=1359575480000&api=v2)|![](https://wiki.hpcc.msu.edu/download/attachments/5411567/[HPCCUSB_ABar.png](./images/HPCCUSB_ABar.png)?version=1&modificationDate=1359600413000&api=v2)|Video Tutorial - HPCCUSB  
  
![](https://wiki.hpcc.msu.edu/download/attachments/5411567/[ChamB_mean.png](./images/ChamB_mean.png)?version=1&modificationDate=1359575480000&api=v2)|![](https://wiki.hpcc.msu.edu/download/attachments/5411567/[ChamB_Bar.png](./images/ChamB_Bar.png)?version=1&modificationDate=1359575480000&api=v2)|![](https://wiki.hpcc.msu.edu/download/attachments/5411567/[ChamB_ABar.png](./images/ChamB_ABar.png)?version=1&modificationDate=1359600403000&api=v2)|No video available on-line  
  
Currently the algorithm is very slow and written in Python. The colors are
based on the HSV colorspace which can be visually understood using the
following image:

![](https://wiki.hpcc.msu.edu/download/attachments/5411567/[images.jpeg](./images/images.jpeg)?version=1&modificationDate=1359575868000&api=v2)  Note: Image obtained from <http://www.mathworks.com/help/images/converting-color-data-between-color-spaces.html>I use the V (value) channel to determine if a color is black then I use the H
(Hue) channel to histogram the remaining colors for each image and display the
histogram linerally by color. I think this is working but it doesn't really
show the variations in color that you see with the MovieBarCode. Most notably
is that since I do not use the S (saturation) channel there is no white or
offwhite colors in the graph. I think this is a good start but will have to
talk though the best way to proceed with the rest of the team.

  * Dirk

[View
Online](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2013/01/30/Movie+Color+Visualization)

Blogpost migrated from [ICER Wiki](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2013/01/30/Movie+Color+Visualization) using custom python script. Comment on errors below.
