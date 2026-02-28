Title: PBS quick submission script
Date: 2012-03-19
Tags: HPC, example, Migration

Blog post **edited** by Anonymous \- "Migration of unmigrated content due to
installation of a new plugin"

I write a lot of submissions scripts for a lot of users on the HPCC. I find
myself using the same tricks over and over again. Recently I came up with the
following script as a quick way to cover most of my job submission needs.

What is nice for me is I don't have to rewrite the script for every job. All
of the job options can be overwritten on the command line and the script uses
the PBS_JOBNAME to determine an executable to run in the current directory. It
also replaces any dashes in the name with spaces as a crude method to include
input arguments. Since PBS_ARRAYID is automatically appended to the end of the
PBS_JOBNAME this also allows job arrays to be used as an input variable.

I hope you find this useful,

  * Dirk



    #!/bin/bash
    #PBS -l nodes=1:ppn=1,walltime=08:00:00,mem=2gb,feature=gbe
    #PBS -j oe
    #PBS -m ae
    #PBS -N a.out

    # I personally use openmpi as my default mpi library and not mvapich
    module unload mvapich
    module load openmpi

    # Change to the original working directory where the qsub command is executed
    cd ${PBS_O_WORKDIR}

    #set OMP thread is appropriate for MPI jobs
    export OMP_NUM_THREADS=`cat ${PBS_NODEFILE} | wc -l`

    # Run the jobname as a command in the local directory and
    # use the ARRAYID as the first input variable if avaliable
    # Uses '-' in the jobname to designate spaces
    #
    # Example:
    #
    #  Run a simple single thread program
    #    qsub -N myprogram quick.qsub
    #
    #  Run a simple program with three different input numbers
    #    qsub -N myprogram -t 100,200,300 quick.qsub
    #
    #  Run a basic openmp program
    #    qsub -N myprogram -l nodes=1:ppn=8 quick.qsub
    #
    #  Run a basic openmpi program
    #    qsub -N mpirun-myprogram -l nodes=64:ppn=1,feature=ib quick.qsub

    #Display the execution command for debugging
    echo ./${PBS_JOBNAME} | sed "s/-/ /g"

    #Run the command using the PBS_JOBNAME to determine the executable name and input variables
    `echo ./${PBS_JOBNAME} | sed "s/-/ /g"`

    #Display the runtime and resources used for the job
    qstat -f ${PBS_JOBID}



[View
Online](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2011/03/19/PBS+quick+submission+script)

Blogpost migrated from [ICER Wiki](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2011/03/19/PBS+quick+submission+script) using custom python script. Comment on errors below.
