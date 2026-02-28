Title: Using X11 Virtual Frame Buffer (Xvfb) in a submission script
Date: 2013-10-08
Tags: HPC, example, Migration

Blog post **edited** by [Nicholas Anthony Rahme](https://wiki.hpcc.msu.edu/display/~rahmenic@msu.edu)

Some programs require access to a display in order to run properly. For
example, MATLAB will provide an error if you try to create an AVI file from a
image frame in -nodisplay mode. This can be an annoying problem on the HPCC
because all of our batch compute nodes do not have displays attached.
Fortunately, the X virtual Frame Buffer (Xvfb) is a program that simulates an
attached display and can allow programs that require Graphical User Interfaces
(X11) displays to run.

The following is a typical submission script for running a MATLAB program :

 **makeAVI.qsub**



    #!/bin/bash
    #PBS -l nodes=1:ppn=1,mem=2gb,feature=gbe
    #PBS -l walltime=01:00:00
    #PBS -j oe
    #PBS -W x=gres:MATLAB

    #Change directory to the qsub submission directory
    cd ${PBS_O_WORKDIR}

    #Run matlab script (replace this with your X11 code)
    matlab -nodisplay -r "makeAVI"

    #Print out job usage
    qstat -f ${PBS_JOBID}


Running this script will give me an error that says "Display not found." The
following script is modified to start Xvfb at the beginning, run the same
basic command and then terminate Xvfb at the end:

 **makeAVI.qsub**



    #!/bin/bash
    #PBS -l nodes=1:ppn=1,mem=2gb,feature=gbe
    #PBS -l walltime=01:00:00
    #PBS -j oe
    #PBS -W x=gres:MATLAB

    #Change directory to the qsub submission directory
    cd ${PBS_O_WORKDIR}

    ##### Specify the display, start the Xvfb server, and save the process ID.
    export DISPLAY=":1"
    rm -f /tmp/.X11-unix
    rm -f /tmp/.X11-lock
    Xvfb $DISPLAY -auth /dev/null/ &
    XVFB_PID=$!

    #Give system time to spin up X11 display (Probably not needed)
    sleep 5
    ####

    #Run matlab script
    matlab -r "makeAVI"

    ##### Stop the Xvfb server and remove the files it created.
    kill -9 $XVFB_PID
    rm -rf /tmp/.X11-unix
    rm -f  /tmp/.X11-lock
    ####

    #Print out job usage
    qstat -f ${PBS_JOBID}


Please note that the -nodisplay option was removed from the MATLAB command
line in the second script

An working example of this script can be downloaded on the HPCC using the
getexample command. Type the following on any development node to run the
example:



    module load powertools
    getexample
    getexample MATLAB_movie
    cd MATLAB_movie
    qsub makeAVI.qsub


  * Dirk

[View
Online](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2013/10/08/Using+X11+Virtual+Frame+Buffer+%28Xvfb%29+in+a+submission+script)

Blogpost migrated from [ICER Wiki](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2013/10/08/Using+X11+Virtual+Frame+Buffer+%28Xvfb%29+in+a+submission+script) using custom python script. Comment on errors below.
