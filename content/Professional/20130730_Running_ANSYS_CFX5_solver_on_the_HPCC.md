Title: Running ANSYS CFX5 solver on the HPCC
Date: 2013-07-30
Tags: HPC, example, Migration

Blog post **edited** by Anonymous \- "Migration of unmigrated content due to
installation of a new plugin"

The following job submission script should get a parallel MPI solve of the
cfx5solver working. In order for this to work on our system I needed to change
the ANSYS module file to include setting CFX5RSH to /usr/bin/ssh



    #!/bin/bash -login
    #PBS -j oe
    #PBS -l walltime=00:10:00,nodes=8:ppn=1,mem=4gb

    cd ${PBS_O_WORKDIR}

    module load ANSYS

    #Hack to create comma seperated list of hosts for this job
    echo `cat $PBS_NODEFILE` | sed "s/ /,/g" > Hosts.file
    read HOSTS < Hosts.file

    cfx5solve -def mymodel.def -start-method 'Platform MPI Distributed Parallel' -par-dist $HOSTS

    qstat -f $PBS_JOBID


Users should consider changing the **walltime** , **nodes** and **def file**
to get this to work for their program.

[View
Online](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2013/07/30/Running+ANSYS+CFX5+solver+on+the+HPCC)

Blogpost migrated from [ICER Wiki](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2013/07/30/Running+ANSYS+CFX5+solver+on+the+HPCC) using custom python script. Comment on errors below.
