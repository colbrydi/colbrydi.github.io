Title: On Demand MakeFlow PBS script
Date: 2011-11-11
Tags: HPC, example, Migration

Blog post **edited** by Anonymous \- "Migration of unmigrated content due to
installation of a new plugin"

We just installed [MakeFlow](http://nd.edu/~ccl/software/makeflow/) on our
system as an easy to use workflow manager that uses the familiar "makefile"
syntax. MakeFlow uses a master node and schedules all of the work off to
worker nodes. To get this working on our system I wanted to have an easy way
for the master node to communicate it's location and port to the worker nodes.
With the help of one of our students we came up with three basic ways for this
to work:

  * Option 1: Schedule a master job and have it schedule worker jobs.
  * Option 2: Schedule a large job and use pbsdsh to call the worker nodes.
  * Option 3: Combine Options 1 & 2

Which option you use depends a lot on how PBS is set up on your system and
there are different pros and cons to each setup. The following is a
description of how I set it up on our HPCC:

# Option 1: Schedule a master job and have it schedule worker jobs.

In this option, the system needs to be able to schedule jobs from all of the
compute nodes. If this is the case, then it is easy to pass the host
information to the worker nodes though a system variable. The job array can
have as many single node jobs as it needs and the jobs will get scheduled as
resources become available. The downside to this approach is that the job has
to wait for the workers to be scheduled before any work can get done. Here is
an example script:



    #!/bin/sh -login
    #PBS -l nodes=1:ppn=1,walltime=04:00:00
    #PBS -j oe

    #Set up running environment for all workers
    module load ImageMagick
    module load cctools

    cd $PBS_O_WORKDIR
    export PORT=9123

    # Check to see if MAINHOST is set
    if [ "${MAINHOST}" == "" ]
    then
           #Run Main process
           export MAINHOST=$HOST
           jobid=`qsub -t 1-10 -v MAINHOST -N ${PBS_JOBNAME} $0`
           makeflow -T wq example.makeflow

           #clean up spawned jobs
           qdel $jobid
    else
           #Run Worker process
           work_queue_worker $MAINHOST $PORT
    fi


# Option 2: Schedule a large job and use pbsdsh to call the worker nodes.

This option can be used if the system is not set up to schedule jobs from the
compute nodes. It has the added benefit of starting immediately. However, the
downside to this approach is that the scheduler needs to be able to schedule a
large block of nodes together which may cause longer queue times. Here is the
example script:



    #!/bin/bash -login
    #PBS -l nodes=4:ppn=1,walltime=04:00:00
    #PBS -j oe

    # Set up running environment for all workers
    module load ImageMagick
    module load cctools

    # If no input argument is given then script is running from qsub
    if [ "$1" == "" ]
    then
            #Script called from qsub
            cd $PBS_O_WORKDIR
            export PORT=9123
    else
            #Script called manually from pbsdsh
            export MAINHOST="$1"
            export PORT="$2"
    fi

    # Check to see if MAINHOST is set
    if [ "${MAINHOST}" == "" ]
    then
            export MAINHOST=$HOST

            #Run Main process
            makeflow -T wq example.makeflow &
            PID=$!

            tempfile=${PBS_O_WORKDIR}/${PBS_JOBID}.sh
            cp $0 $tempfile
            chmod 755 $tempfile
            pbsdsh $tempfile $MAINHOST $PORT &

            #Wait for main makeflow process to finish       
            wait $PID

            #Clean up jobs  
            rm $tempfile
    else
            #Run Worker process
            work_queue_worker $MAINHOST $PORT
    fi


# Option 3: Combine Options 1 & 2

The third option is to combine Options 1 & 2 together. This way the job can
get started right away and grow as additional workers get added to the queue.



    #!/bin/bash -login
    #PBS -l nodes=4:ppn=1,walltime=04:00:00
    #PBS -j oe

    # Set up running environment for all workers
    module load ImageMagick
    module load cctools

    # If no input argument is given then script is running from qsub
    # Note: The else statement is only needed for Option 2
    if [ "$1" == "" ]
    then
            #Script called from qsub
            cd $PBS_O_WORKDIR
            export PORT=9123
    else
            #Script called manually from pbsdsh
            export MAINHOST="$1"
            export PORT="$2"
            echo "MAINHOST=${MAINHOST} PORT=${PORT}"
    fi

    # Check to see if MAINHOST is set
    if [ "${MAINHOST}" == "" ]
    then
            export MAINHOST=$HOST

            #Run Main process
            makeflow -T wq example.makeflow &
            PID=$!

            #Option 1: Spawn workers as independent PBS jobs
            jobid=`qsub -l nodes=1:ppn=1 -t 1-10 -v MAINHOST -N ${PBS_JOBNAME} $0`
            echo $jobid

            #Option 2: run workers inside current job
            tempfile=${PBS_O_WORKDIR}/${PBS_JOBID}.sh
            cp $0 $tempfile
            chmod 755 $tempfile
            pbsdsh $tempfile $MAINHOST $PORT &

            #Wait for main makeflow process to finish       
            wait $PID

            #Clean up jobs  
            echo "Cleaning up $jobid and $tempfile"
            qdel $jobid
            rm $tempfile
    else
            #Run Worker process
            echo "RUNNING WORKER PROCESS"
            work_queue_worker $MAINHOST $PORT
    fi


Future Work

I need to be careful with this script because I have not tested the behavior
when two master jobs end up getting scheduled on the same node and use the
same port. I will need to put in a test to make sure this doesn't happen. I
also am planning on wrapping everything into a simple command that will hide
all of the details from the user.

[View
Online](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2011/11/11/On+Demand+MakeFlow+PBS+script)

Blogpost migrated from [ICER Wiki](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2011/11/11/On+Demand+MakeFlow+PBS+script) using custom python script. Comment on errors below.
