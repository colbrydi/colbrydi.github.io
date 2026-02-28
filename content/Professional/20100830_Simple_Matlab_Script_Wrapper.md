Title: Simple Matlab Script Wrapper
Date: 2010-08-30
Tags: HPC, example, Migration

Blog post **edited** by Anonymous \- "Migration of unmigrated content due to
installation of a new plugin"

Sometimes you have four or five variations on the same MATLAB script. You
could write a different submissions script for each variation, or you can
constantly edit the submission script every time you need to change to a
different variation. However, I find that this can be confusing so I made the
following script to make my life easier:

**runMatlab.qsub**



    #!/bin/bash -login
    #PBS -l walltime=01:00:00,nodes=1:ppn=1
    #PBS -l software=MATLAB
    cd ${PBS_O_WORKDIR}
    module load matlab
    matlab -nodisplay -r "${PBS_JOBNAME}"


This is a qsub wrapper script that allows you to specify the name of the
MATLAB script as the name of the job. To run the script just type:



    qsub -N myScriptName runMatlab.qsub


Then when you want to run a different script you can type:



    qsub -N myDifferentScript runMatlab.qsub


Make sure you do not include the ".m" in the script name. Since command line
resource request override requests in the script, it is possible to also
change the resources from the command line. For example, if you have a really
short test you need to run you can do the following:



    qsub -N myquicktest -l walltime=00:05:00 runMatlab.qsub


**NOTE:** This above only works for MATLAB scripts (i.e. no input arguments)
and not functions.

[View
Online](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2010/08/30/Simple+Matlab+Script+Wrapper)

Blogpost migrated from [ICER Wiki](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2010/08/30/Simple+Matlab+Script+Wrapper) using custom python script. Comment on errors below.
