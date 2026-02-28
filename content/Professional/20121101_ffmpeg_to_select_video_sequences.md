Title: ffmpeg to select video sequences
Date: 2012-11-01
Tags: HPC, example, researchblog, Migration

Blog post **edited** by Anonymous \- "Migration of unmigrated content due to
installation of a new plugin"

ffmpeg can be used to crop the start and end times of a video sequece. Use the
following command to read though the ffmpeg help message in the terminal
window:

    
    
           man ffmpeg
    

Use arrow keys to move the text up and down and use 'q' key to quit. The two
options we are interested in are as follows:

    
    
    
    -i filename
       input file name
    
    -ss position
       Seek to given time position in seconds.  "hh:mm:ss[.xxx]" syntax is also supported.
    
    -t duration
       Restrict the transcoded/captured video sequence to the duration specified in seconds.
       "hh:mm:ss[.xxx]" syntax is also supported.
    

The following command should trim out the interesting area of the video:

    
    
         ffmpeg -i ChamC_Jul12_2011_LB3.MOV -ss  "00:01:40" -t 23 ChamC_Jul12_2011_LB3.mpg
    

That worked for me but the quality is not right. I did some more searching of
the ffmpeg man page and came up with the following item that will impact
quality:

    
    
    -sameq
       Use same video quality as source (implies VBR).
    

This seems to work better:

    
    
         ffmpeg -i ChamC_Jul12_2011_LB3.MOV -ss  "00:01:40" -t 23 -sameq ChamC_Jul12_2011_LB3.mpg
    

[View
Online](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2012/11/01/ffmpeg+to+select+video+sequences)

Blogpost migrated from [ICER Wiki](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2012/11/01/ffmpeg+to+select+video+sequences) using custom python script. Comment on errors below.
