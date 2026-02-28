Title: New Powertool to help checkpoint jobs
Date: 2011-10-06
Tags: HPC, example, Migration

Blog post **edited** by [Xiaoge Wang](https://wiki.hpcc.msu.edu/display/~wangx147@msu.edu)

In a previous blog post I posted my script for automatically checkpointing
jobs using BLCR which enables us to run jobs longer than a week:

<http://wiki.hpcc.msu.edu/x/eIHT>

I didn't like the complexity of the script so I created a new Powertool to do
the same thing. I call this tool "longjob" which requires a few modifications
to your submission script. In addition to running jobs longer than a week,
using longjob with a four hour walltime has the following advantages:

  1. Run jobs with unknown walltimes
  2. Run jobs on the buy-in nodes (which requires 4 hours or less walltime)
  3. Enables robustness of long jobs due to hardware failure
  4. Run jobs up to a maintenance window without having to wait for that window to complete

The following are instructions for trying out longjob on our system. First,
you start with a a basic submission script. For example, consider the
following simple submission script:



    #!/bin/bash -login
    #PBS -l nodes=1:ppn=1,walltime=200:00:00,mem=2gb,feature=gbe
    #PBS -j oe
    #PBS -m ae

    cd $PBS_O_WORKDIR

    srcdir=${PBS_O_WORKDIR}/bin/
    WORK=/mnt/scratch/${USER}/KineticSN/${PBS_JOBID}
    mkdir -p ${WORK}

    # Copy files to work directory
    cp -r $srcdir/* $WORK/

    #Move to the working directory
    cd $WORK

    #Run my program
    ./SimulationTest -scattering_flag 0 -weak_reaction_flag 0 -outputVisData 100
    ret=$?

    qstat -f ${PBS_JOBID}

    exit $ret



To get longjob to work, the following modificaitons need to be made:

  1. Adjust the walltime to be shorter (I suggest 4 hours or less).
  2. Wrap all setup-code that only needs to be run once in an if statement that checks for the checkpoint file (checkfile.blcr). This will ensure that the setup-code only runs the first time the script is run because the first time the script is run there should not be a checkpoint file.
  3. add the "longjob" command before the command in the submission script that you want to checkpoint.
  4. load the powertools module and turn on aliases. i.e. add the following lines of code to the script:
    * shopt -s expand_aliases
    * module load powertools
  5. Set the following enviornment variables as appropriate for your job:
    *  **BLCR_WAIT_SEC** number of seconds the job should wait before checkpointing and restarting. (should be less than your walltime, default is 3 hours and 55 minutes).
    *  **PBS_JOBSCRIPT (required)** the path and name of the jobscript to use in the restart. Typically this is the same as your main jobscript and by default you can always add the following line:
      * export PBS_JOBSCRIPT="$0"
    *  **BLCR_OUTPUT** name of the main standardout/standarderr file (Default is output.txt)
    *  **BLCR_CHECKFILE** name of the checkpoint file (Default is checkfile.blcr)

The following is a modified example script with the changes:



    #!/bin/bash -login
    #PBS -l nodes=1:ppn=1,walltime=04:00:00,mem=2gb,feature=gbe
    #PBS -j oe
    #PBS -m ae

    shopt -s expand_aliases
    cd $PBS_O_WORKDIR
    module load powertools

    # 4 hours * 60 minutes * 6 seconds - 60 seconds * 5 minutes
    export BLCR_WAIT_SEC=$(( 4 * 60 * 60 - 60 * 5))
    export PBS_JOBSCRIPT="$0"
    echo "Waiting ${BLCR_WAIT_SEC} seconds to run ${PBS_JOBSCRIPT}"

    if [ ! -f checkfile.blcr ]
    then
    	srcdir=${PBS_O_WORKDIR}/bin/
    	WORK=/mnt/scratch/${USER}/KineticSN/${PBS_JOBID}
    	mkdir -p ${WORK}

    	# Copy files to work directory
    	cp -r $srcdir/* $WORK/

    	#Run main simulation program
    	cd $WORK

    fi
    longjob ./SimulationTest -scattering_flag 0 -weak_reaction_flag 0 -outputVisData 100
    ret=$?

    qstat -f ${PBS_JOBID}

    exit $ret



If everything works as expected, you should be able to qsub the above file and
it will resubmit itself every four hours until the job completes. Note, this
is a work in progress and I have not tested all cases. For example, one case
that could propose a problem is if the main program gets caught in a loop and
never exits, in this case the code will keep submitting itself indefinitely.

Please email me (colbrydi@msu.edu) if you end up using this code or if you
would like to learn more how longjob is implemented.

  * Dirk

[View
Online](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2011/10/06/New+Powertool+to+help+checkpoint+jobs)

Blogpost migrated from [ICER Wiki](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2011/10/06/New+Powertool+to+help+checkpoint+jobs) using custom python script. Comment on errors below.
