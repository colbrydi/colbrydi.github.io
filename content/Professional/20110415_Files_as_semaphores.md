Title: Files as semaphores
Date: 2012-04-15
Tags: HPC, example, Migration

Blog post **edited** by Anonymous \- "Migration of unmigrated content due to
installation of a new plugin"

The following is a script that is designed to make it really easy to run a
large number of embarrassingly parallel jobs on our scheduling system. The
trick to getting this to work is to use files as [semaphores
](http://en.wikipedia.org/wiki/Semaphore_\(programming\)). The program
compares a directory of input files with a directory of flag files. If a file
is found in the input directory and not in the flag directory, then this is a
job that still needs to run and the program will create a file in the flag
directory and do the computation. The flag files are used to keep track of
what is running and what is complete.

Strictly speaking, many file systems are not guaranteed to be atomic so this
method is risky but in my experience it works quite well especially if you do
not care if two processes run the same job.

**"FilesAsSemaphores.qsub"**



    #!/bin/sh -login
    #PBS -l nodes=1:ppn=1,walltime=00:30:00,feature=gbe,mem=1gb
    #PBS -j oe
    #PBS -m a

    #Files as semifors  
    # Script written by Dirk Colbry  

    #CHANGE the following to filter files that need to be processed
    filefilter="*.do"

    #Create a flags directory if one is not already created
    cd ${PBS_O_WORKDIR}
    mkdir -p flags

    #Check to see if job being run from an array. Space jobs so they do not run on
    #top of each other. This is probably unessary
    if [ ! "${PBS_ARRAYID}" = "" ]
    then
    	sleep ${PBS_ARRAYID}
    fi

    # Find the most recent file not in the flags directory
    # This indicates that the file has not been proceesed
    for file in `echo $filefilter`  
    do
    	if [ ! -f ./flags/${file}.flag ]
    	then
    		#Create the file so other jobs will not run the same program
    		touch ./flags/${file}.flag
    		dofile=$file
    		break
    	fi
    done

    #Check to see if dofile is empty
    #This indicates all files have been processed
    if [ "$dofile" == "" ]
    then
    	echo "All jobs completed!"
    	exit 0
    fi		

    #CHANGE the following to run the program of interest using the dofile as an input
    module load stata
    stata-se -b ${dofile}  

    #Save the return value of the last command
    RET=$?

    #Put the job statistics on the flag file as a record and to indicate
    # the program execited successfully.
    if [ "$RET" = "0" ]
    then
    	qstat -f ${PBS_JOBID} > ./flags/${dofile}.flag
    else
    	qstat -f ${PBS_JOBID}
    	echo "job with dofile=${dofile} completed with error ${RET}"
    	exit $RET
    fi

    #Check to see if anything is left that needs to be done
    for file in `echo $filefilter`  
    do
    	if [ ! -f ./flags/${file}.flag ]
    	then
    		#flag missing...start another job
    		qsub mainrun.qsub
    		exit $RET  
    	fi
    done

    #Nothing is left to be done... Exit
    #Note, return value (RET) should be zero
    echo "ALL JOBS COMPLETED!"
    exit $RET  


Obviously a user needs to modify the script to fit their need (this one was
designed to work with stata). To start the script you can just issue the
following command:



    qsub -t 1-149 FilesAsSemaphores.qsub


This will start 149 jobs working. When each job is done it will start another
job until all of the input files have been processed. This script could easily
be modified to work with a list of jobs in a text file or some other method
for listing what needs to be done. One nice feature of this program is that
you can look at the size of the flag files to determine if a job has completed
successfully. If you want, you can delete all of the jobs in your queue and
then delete all files of size zero and restart the entire process.

I do not recommend walltimes of less than 5 minutes as this will unnecessarily
flood the scheduler, please use this script at your own risk.

  * Dirk

[View
Online](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2011/04/15/Files+as+semaphores)

Blogpost migrated from [ICER Wiki](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2011/04/15/Files+as+semaphores) using custom python script. Comment on errors below.
