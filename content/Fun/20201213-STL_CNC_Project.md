Title: STL files to CNC
Date: 2020-12-13
Tags: Maker

I purchased a discount Workbench CNC machine. I've been a 3D printing person for a while and was suprised how hard it has been to get gcode for a CNC machine.  I assumed that I could just upload something like an STL file but there are not a lot of software tools.  Or better yet, there are too many software tools and I can't figure out which ones work the best.  

Part of the problem is that CNC milling is not true 3D.  Instead it is more like 2.5D, where the tool only comes in from one direction. 

There are lot of STl designs that should work fine in a 2.5D setting. For example, I have been fascinated by these project cards you can find on Thingiverse:

- [Enterprise-D](https://www.thingiverse.com/thing:4601489)

In this project I am exploring ways to convert these types of one-directional stl files into something I can cut using my CNC machine.  So far I am trying to use the following steps:


1. Generate a depthmap from STL file using [Meshlab](https://www.meshlab.net/) and following directions [posted here](https://community.glowforge.com/t/tutorial-creating-a-depth-map-from-a-3d-model-for-3d-engraving).
2. Adjust the contrast of the depthmap to use full grayscale range. (I used preview on mac but any image processing tool should work)
3. Generate gcode from depthmap using [Dmap2gcode](http://scorchworks.com/Dmap2gcode/dmap2gcode.htm) python tool
4. Review the gcode using [g-code simulator](https://nraynaud.github.io/webgcode/)
5. [Hold down method for thin stock using glue and Painters tape](https://www.youtube.com/watch?v=gTUAAm0DFOQ)

## Step 1: STL to Depthmap

Using this [tutorial](https://community.glowforge.com/t/tutorial-creating-a-depth-map-from-a-3d-model-for-3d-engraving) as a guild, I downloaded [Meshlab](https://www.meshlab.net/) and imported the [Enterprise-D](https://www.thingiverse.com/thing:4601489) stl file.  

I do not use Meshlab that much so I was not sure how to set the camera view.  Fortunately the stl file loaded in the way I wanted so as long as I did not rotate it I could follow the tutorial directions and generate a depthmap.  It was a little tricky to figure out where to set the zmax and zmin values.  I tried really hard to pick settings that would show the most color contrast in the image.  

I found that values near the right side of the slider seemed to work well for this stl model.

When taking the image snapshot I set the background to black because I wanted to cut away the background.


**_Alternative to Step1:_** I found this website which seems to be much quicker and easier than using meshgrid. I can't adjust anything but the results are clean and could allow someone to skip step 2:

- [STL2PNG](https://fenrus75.github.io/FenrusCNCtools/javascript/stl2png.html)

## Step 2: Adjust contrast

I found it difficult to get the colors right in Meshlab so I loaded the image into preview (on mac), cropped the image and fiddled with the contrast.  Try using histogram equalization if it is available in your image processing program. The goal is to use the entire color range for the file with white being the highest peak in your cut and black being everything is removed. 

![Enterpise-D01](Enterpise-D01.png)

## Step 3: dmap2gcode

I found this interesting python project to convert depthmap files to gcode. 

- [dmap2gcode](http://scorchworks.com/Dmap2gcode/dmap2gcode.html)

I have no idea if this will work. Also the developer has executables for windows but not mac. Turns out not to be a big deal.  I am a python programmer and I was easily able to download and run the python code on my laptop.  **_NOTE_** python 3.9 did not work but python 3.7 was fine.  I ended up making a conda environment, installing the necessary packages and running from there.  Here is a link to my environment.yml file if you want to try it out.

- [environment.yml]()

Importing the image file seemed to work fine. The gcode takes hours to generate but once I downgraded to python 3.7 everything seemed to work fine. 

## Step 4: Preview G-code

I have no idea what settings I should be using for the dmap2gcode interface.  I found this online simulator which allows me to copy/paste my code and view the gcode (neat).  I used the following mac trick to copy the code:

```cat Enterprise-D.ngc | pbcopy```

The first few times generating the gcode did not seem like it worked well.  I fiddled for a bit and came up with this answer.


## Step 5: Milling a thin sheet

Next, I needed to figure out how to hold my sample into place.  I want to use a thin piece of wood and cut though the material.  This means I need a way to hold the entire sample down.  I found [this video tutorial](https://www.youtube.com/watch?v=gTUAAm0DFOQ) for using a special kind of super glue and painters tape.   Seems like a cool trick to do what I want. 


## Final Product

I haven't actually got this working yet.  I am keeping this blog post for notes and plan to update it as I get closer.

Like any project, there was a lot of learning for each of the above steps.  What I have shown here are some notes to remind my future self what I did to get this working.  I am posting these notes on-line just in case anyone else wants to give it a try. 

Please feel free to email me questions and/or let me know if you have found better ways to do any of these steps.

Take care,

- Dirk