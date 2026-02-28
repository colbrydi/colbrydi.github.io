Title: Video Processing and Enthought Python
Date: 2012-05-15
Tags: HPC, researchblog, Migration

Blog post **edited** by Anonymous \- "Migrated to Confluence 4.0"

One of the reasons for choosing to work with the [Enthought version of Python
](http://www.enthought.com/) is that future users of software that we develop
do not need to download and figure out how to install all of the different
Python modules that they may need to work with. This is particularly important
to me because I want to distribute our code to researchers that may not have
expertise using Python. I was particularly excited to learn that the Enthought
distribution of Python came with the [scikits-image](http://scikits-
image.org/) module and the [Python Image Library (PIL)
](http://www.pythonware.com/products/pil/). Initially, I hoped that these
packages would contain everything I need right out of the box.

Unfortunately, I just learned that Enthought Python is missing some libraries
that are essential to my research. In particular, scikits-image works with the
OpenCV library but does not actually require OpenCV, and OpenCV is not
included in the Enthought install. Part of my goal for this summer is to
extend the functionality of the ChamView software which is written in Python
and requires OpenCV to read and write to video files. This limitation is
frustrating because video is particular important and can be difficult to work
with. I also remember that there were different procedures for installing
OpenCV on different OS platforms.

Since OpenCV is not available by default in the Enthought installation, I did
some quick web searching to see if I could find any alternatives. So far I
have come up with the following possibilities:

  * pyffmpeg <http://code.google.com/p/pyffmpeg/>.
  * PyMedia <http://pymedia.org/tut/>
  * VTK <http://www.vtk.org/>
  * pyglet <http://www.pyglet.org/>

Unfortunately, these first two options are also not installed by default in
the [Enthought distribution
](http://www.enthought.com/products/epdlibraries.php), so they are no better
than OpenCV. VTK and pyglet are installed but I am having trouble finding
documentation and getting an example to work. It may be that my best bet is to
install OpenCV. I will probably need to logically separate my code so as to
isolate functions that require OpenCV, in case it is not available when users
are installing and using our software elsewhere.

  * Dirk

[View
Online](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2012/05/15/Video+Processing+and+Enthought+Python)

Blogpost migrated from [ICER Wiki](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2012/05/15/Video+Processing+and+Enthought+Python) using custom python script. Comment on errors below.
