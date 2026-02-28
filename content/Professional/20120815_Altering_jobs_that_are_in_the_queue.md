Title: Altering jobs that are in the queue
Date: 2012-08-15
Tags: HPC, example, moab, torque, job, alter, change, Migration

Blog post **edited** by Anonymous \- "Migration of unmigrated content due to
installation of a new plugin"

Recently a user came by my office to complain that his jobs where not running
in the queue. This is a reasonable complainte because many of our nodes are
being drained to reboot and avoid the 208 day bug. Fortunately this user had a
lot of single threaded jobs that could run on the gfx10 nodes. To run on these
nodes the user needs to change the jobs to add the feature=gbe option
(Gigabyte either-net). First I tried the following command:

    
    
    qalter -l feature=gbe $PBS_JOBID 

Unfortunately,the qalter command modifies jobs in the resource manager but the
job is waiting on the scheduler. I had hoped that the scheduler would talk to
the resouce manager and update the properties but this did not happen. After
talking with others in the office we found the command to alter jobs in the
scheduler:

    
    
     mjobctl -m feature=gbe $PBS_JOBID 

This worked great and propagated all changes to the resource manager. I wrote
a quick script to change all nodes currently pending in the queue to accept
add this change:

    
    
    #!/bin/bash -l
    for job in `qselect -s Q -u $USER`;
    do
         echo mjobctl -m feature=gbe $job
         mjobctl -m feature=gbe $job
    done
    
    

I added a qalter_all_gbe command to powertools to help users do the same thing
on the hpcc.

  * Dirk

[View
Online](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2012/08/15/Altering+jobs+that+are+in+the+queue)

Blogpost migrated from [ICER Wiki](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2012/08/15/Altering+jobs+that+are+in+the+queue) using custom python script. Comment on errors below.
