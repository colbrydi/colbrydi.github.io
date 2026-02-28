Title: Running the XSEDE MPI workshop examples on the HPCC
Date: 2013-06-18
Tags: HPC, example, Migration

Blog post **edited** by Anonymous \- "Migration of unmigrated content due to
installation of a new plugin"

Differences in examples to get them to run on the HPCC.

Step 1:  
Download these examples buy loading the power tools module and using the get
example command:

    
    
    module load powertools
    getexample
    getexample XSEDE_MPI_WORKSHOP
    

Step 2:  
Compile the code using "mpicc" or "mpif90":

    
    
    mpicc ex1.c
    mpif90 ex1.f
    

Step 3:  
Run the code in the command line using same command:

    
    
    mpirun -np 4 ./a.out
    

Step 4:  
Write a submission script and run the job on the cluster:

    
    
    #!/bin/bash
    #PBS -j oe
    #PBS -l walltime=05:00,nodes=8:ppn=1
    
    cd ${PBS_O_WORKDIR}
    
    mpirun ./a.out
    
    qstat -f ${PBS_JOBID}
    
    

Step 5:  
Submit the job using the following command:

    
    
    qsub myjob.qsub
    

[View
Online](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2013/06/17/Running+the+XSEDE+MPI+workshop+examples+on+the+HPCC)

Blogpost migrated from [ICER Wiki](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2013/06/17/Running+the+XSEDE+MPI+workshop+examples+on+the+HPCC) using custom python script. Comment on errors below.
