Title: video size and bitrates
Date: 2012-05-24
Tags: HPC, researchblog, Migration

Blog post **edited** by Anonymous \- "Migrated to Confluence 4.0"

A question that comes up in my research periodically is how much hardware is
needed to store and transmit video data? Generally, I get away with the off-
the-cuff estimate of 1 hour of video needing 1GB of space. Recently, I needed
some better estimates for a proposal so I did some quick digging. The
following table (found
[here](http://www.ezs3.com/public/What_bitrate_should_I_use_when_encoding_my_video_How_do_I_optimize_my_video_for_the_web.cfm))
is a starting point to estimate file sizes and bit rates for MP4 files.

Output size, Bitrate, FileSize  
  320x240 pixels, 400 kbps, 3MB / minute  
  480x270 pixels, 700 kbps, 5MB / minute  
  1024x576 pixels, 1500 kbps, 11MB / minute  
  1280x720 pixels, 2500 kbps, 19MB / minute  
  1920x1080 pixels, 4000 kbps, 30MB / minute

My 1gb/hour estimate doesn't specify the resolution of the video, the audio
content, the compression algorithm used, nor how much change is occurring in
the video (which affects the amount of compression that can be done). Using
the table above, we can see that 1gb/hour comes out to a file size of about 17
MB/sec, which is about the middle point in the table - making my original 1gb-
per-hour-of-video estimate fairly reasonable.

Based on this table, a single camera could easily generate between 4GB and
43GB of data per day. Many research projects gather data using systems of
multiple cameras with data piped directly into a computer.

For example, I am working on one (small) project that has two cameras, each
running about 5 minutes for three trials a day. While this initial setup only
generates about 510MB of data per day, we would like to eventually expand the
system to 5 cameras, generating about 1GB of data per day. If we also wanted
to process the data "in real time" (i.e., as quickly as possible), then we
would need to maintain a transfer rate of around 10MB/second. Even if we
bought high-end cameras, our transfer rate would probably top out around
20MB/second when using five cameras for this project.

This type of estimating is useful when writing proposals or designing
experiments, because it gives a realistic idea of the type of network that
will be required to handle the data transfer in “real time.”

  * Dirk

[View
Online](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2012/05/24/video+size+and+bitrates)

Blogpost migrated from [ICER Wiki](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2012/05/24/video+size+and+bitrates) using custom python script. Comment on errors below.
