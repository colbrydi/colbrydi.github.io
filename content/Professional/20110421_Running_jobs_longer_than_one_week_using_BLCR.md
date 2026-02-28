Title: Running jobs longer than one week using BLCR
Date: 2011-04-21
Tags: HPC, example, Migration

Blog post **edited** by Anonymous \- "Migration of unmigrated content due to
installation of a new plugin"

Our submission system is set up with a maximum walltime of one week. This
works fine for most users but sometimes it is nice to be able to run a job
even longer. The following script uses [Berkley Lab Checkpoint Restart
(BLCR)](https://ftg.lbl.gov/CheckpointRestart/CheckpointRestart.shtml) to
automatically save the current state of a job and submit it back to the
scheduler.

**long_job.qsub**



    #!/bin/sh -login
    #PBS -j oe
    #PBS -l nodes=1:ppn=1,walltime=24:10:00,mem=2gb
    #PBS -m a

    cd ${PBS_O_WORKDIR}

    #Berkly Lab Checkpoint Restart script to run a job continuously
    #Written by Dirk Colbry

    #Job restarts itself every 24 hours or 86400 seconds
    export walltime="86400"

    export output="output.txt"

    # Name if main checkpoint file
    export checkpoint="checkfile.blcr"

    if [ "${PBS_ARRAYID}" = "" ]
    then
    	echo "Running for the first time"
    	#### SET UP JOB,
            #Runs once.  Include any job setup commands inside this if block before the cr_run command.

            #Replace the program "supernova 1000" with your program and input arguments
    	cr_run ./supernova 100 1> ${output} 2>&1 &
    	export PID=$!
    	export next=1
    else
    	echo "Restarting ${PBS_ARRAYID}"
            #Job running as a restart job
    	cr_restart --no-restore-pid ${checkpoint} >> ${output} 2>&1 &
    	export PID=$!
    	export next=$(($PBS_ARRAYID+1))
    fi

    #function to run if the program times out
    checkpoint_timeout() {
      echo "Timeout. Checkpointing Job"

      time cr_checkpoint --term ${PID}
      echo "**********"
      tail ${output}
      echo ""
      echo "**********"

      if [ ! "$?" == "0" ]
      then
            echo "Failed to checkpoint"
            exit 2
      fi

      echo "Queueing Next Job"
      chmod 644 context.${PID}
      mv context.${PID} ${checkpoint}
      qsub -t ${next} long_job.qsub

      exit 0
    }

    #set checkpoint timeout
    (sleep ${walltime}; echo 'Timer Done'; checkpoint_timeout;) &
    timeout=$!
    echo "starting timer (${timeout}) for ${walltime} seconds"

    echo "Waiting on $PID"
    wait ${PID}
    RET=$?

    #Check to see if job checkpointed
    if [ "${RET}" = "143" ] #Job terminated due to cr_checkpoint
    then
    	echo "Job seems to have been checkpointed, waiting for checkpoint to complete."
    	wait ${timeout}
    	qstat -f ${PBS_JOBID}
    	exit 0
    fi

    ## JOB completed

    #Kill timeout timer
    kill ${timeout}

    #Output the job statistics
    qstat -f ${PBS_JOBID}

    #Email the user that the job has completed
    qstat -f ${PBS_JOBID} | mail -s "JOB COMPLETE" $USER@msu.edu
    echo "Job completed with exit status ${RET}"
    exit 254


The job will keep submitting itself until the code exits successfully.

Some limitations of this script include:

  * This one uses Job array as an iteration flag so the script will not work in a job array
  * Currently only been tested on single thread jobs.

A simple modification to this script could be made such that each job runs
less than 4 hours. This would allow them to run on the buy-in nodes.

Hope you find this useful,

  * Dirk

[View
Online](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2011/04/21/Running+jobs+longer+than+one+week+using+BLCR)

Blogpost migrated from [ICER Wiki](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2011/04/21/Running+jobs+longer+than+one+week+using+BLCR) using custom python script. Comment on errors below.
