Title: OBS Default Backdrop on Mac
Date: 2021-08-17
Tags: Teaching


![My new default background picture](//colbrydi.github.io/images/placeholder.png) 


As we move online I have been experimenting with [Open Broadcast Software (OBS Studio)](https://obsproject.com/) as a way to improve my video input while I am in meetings and conducting lectures.  

Although it had a small learning curve and often produces a lag between the audio and video; I really like the flexibility that OBS brings to my remote meetings.  Some tools I particularly like include:

- Custom away messages
- On screen logos
- Changing background images
- Over the shoulder coding

Today I figured out how to change the default OBS image that appears when the software is not running.  Although I didn't mind the built in default I wanted to have something that was more personal and less distracting than an advertisement for OBS.  It took me a little searching so I thought I would share the steps that worked for me: 

1. Create a 1920x1080 image (Not sure if this exact size is required but I matched the size I found). Name this file ```placeholder.png```
2. Copy and replace the image in the corresponding```/Application/OBS.app``` folder and the ```obs-mac-virtualcam.plugin``` folder.  I assume that only the second one is required but I went ahead and copied both. here are the exact commands (note the second one requires root privliges)

    ```cp placeholder.png /Applications/OBS.app/Contents/Resources//data/obs-plugins/mac-virtualcam/obs-mac-virtualcam.plugin/Contents/Resources/placeholder.png```
    
    ```sudo cp placeholder.png /Library/CoreMediaIO/Plug-Ins/DAL/obs-mac-virtualcam.plugin/Contents/Resources```
    
That should be it! The new image started working for me right away.  I haven't done much else checking to see if I could use a different size image and/or if I needed to coy both files.  


### Edited Oct 6, 2021 
Recent update to OBS changed the wrokign path and overwrite my placeholder file. I updated the path in the first command from ```/Applications/OBS.app/Contents/Resources/data/obs-mac-virtualcam.plugin/Contents/Resources/placeholder.png``` to 
```/Applications/OBS.app/Contents/Resources//data/obs-plugins/mac-virtualcam/obs-mac-virtualcam.plugin/Contents/Resources/placeholder.png```.  Again, I am not sure if this copy is required. 