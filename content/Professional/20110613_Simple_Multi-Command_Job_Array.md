Title: Simple Multi-Command Job Array
Date: 2011-06-13

Tags: HPC, example, Migration

Blog post **edited** by [Pat Bills](https://wiki.hpcc.msu.edu/display/~billspat@msu.edu) \- "type"

It is fairly easy to map a single variable to a job array. However it gets
tricky when you have more than one variables because it is not strait forward
to expand the 1D job array. In the past, I have managed to make a script to
run over all possible combinations of two variables by flattening a 2D array
into a 1D array (see [Massively Nested
Loops](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2011/05/19/Massively+Nested+Loops)
for an example) using syntax such as the following:



    v1=`echo "${PBS_ARRAYID} % ${cols}" | bc`
    v2=`echo "${PBS_ARRAYID} / ${cols}" | bc`


However, this code can quickly get out of hand as you get bigger sets. One
simple alternative is to just make a file that contains a list of all of the
variations that you want to run of your command. For example, say you need to
run the following programs with various different inputs:

 **commands.txt**



    ./myprogram -a 100 -z 3023
    ./myprogram dosomething different
    ./myprogram
    ./myprogram -s 100 -d 1
    ./myprogram -s 100 -d 2
    ./myprogram -s 100 -d 3
    ./myprogram -s 200
    ./myprogram -s 300
    ./myprogram -w 400
    ./myotherporgram
    ./mythirdprogram


It is fairly easy to make a program to generate your command list or even use
something like excell to generate different input parameters. Then, assuming
all of these commands take the same number of resources, you can use the
folloing following job submission script to run them all in the same job
array:

 **jobarray.qsub**



    #!/bin/bash -login
    #PBS -l walltime=00:05:00
    #PBS -l nodes=1:ppn=1,feature=gbe
    #PBS -j oe
    #PBS -t 1-100

    cd ${PBS_O_WORKDIR}

    cmd=`tail -n ${PBS_ARRAYID} commands.txt | head -n 1`
    echo ${cmd}
    ${cmd}

    qstat -f ${PBS_JOBID}


You should make sure that the array length is the same size as the number of
lines in your commands.txt file. One way to do this is to submit the job as
follows:



    qsub -t 1-`cat commands.txt | wc -l` jobarray.qsub


Hope you find this useful,

  * Dirk

[View
Online](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2011/06/30/Simple+Multi-
Command+Job+Array)

Blogpost migrated from [ICER Wiki](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2011/06/30/Simple+Multi-Command+Job+Array) using custom python script. Comment on errors below.
