Title: Reordering the Eligible Jobs in Your Queue
Date: 2010-08-17
Tags: HPC, example, Migration

Blog post **edited** by [Chun-Min Chang](https://wiki.hpcc.msu.edu/display/~changc81@msu.edu) \- "Migration of unmigrated content due to installation of a new plugin"

I run a lot of different types of jobs with many different resource
requirements. Back when we could have up to 144 eligible jobs in the queue
this was not a problem. However, now to make the queuing system more fair,
users can only have 15 eligible jobs in the queue (at any one time) and the
rest of the jobs are set as idle. If all of your jobs require the same types
of resources, this is not really a problem.

However, sometimes I get five jobs in the queue that are waiting on resources
and I want to run a different type of simpler job that should be able to run
immediately but can't because it is in the idle queue instead of the eligible
queue. The problem is that the five, complex resource, jobs that are already
in the eligble queue end up blocking the simpler job that could run.

For example, lets say I have five jobs that need nodes=1:ppn=8 and I want to
add a job that only requires nodes=1:ppn=1 (no memory or significant
walltimes). If there are no 8-core nodes available then the five 8-core jobs
end up blocking my single core job which will not be eligible to run unless
one of the 8-core jobs gets out of the way. To fix this problem I reorder my
queue by putting a temporary hold on the more complex jobs using the "qhold"
command:



    qhold JOBID#


Suspending the complex jobs allows my single core job to move to the eligible
queue and be able to run. I can then immediately run the queue resume command
(qrls) and the complex jobs move back into the queue, behind the single core
job. To resume a suspended job in the queue:



    qrls JOBID#


Just for fun, I quickly came up with the following scripts that can help move
a job to either the top or the bottom of a users eligible queue:

 **move2top**



    #/bin/bash --login
    #DESCRIPTION Move a job to the top of your eligble queue
    # This script suspends all of your jobs and then resumes only
    # the specified job so it moves to the top of the eligible queue
    # The remaining jobs are then resumed (after a wait period).
    #
    # This script allows users to move a job up if they are being
    # blocked by other jobs.
    #
    # Written by Dirk Colbry August 17, 2010
    # © 2010 Michigan State University Board of Trustees.

    jobid=$1
    if [ "$1" == "" ]
    then
            echo "job id required"
            exit 1
    fi
    qhold `qselect -s Q -u ${USER}`
    qrls $1
    echo "Waiting 30 seconds for queue to settle..."
    sleep 30
    qrls `qselect -s H -u ${USER}`
    showjobs


**move2bot**



    #/bin/bash --login
    #DESCRIPTION Move a job to the bottom of your eligble queue
    # This script teporarily suspends a jobs to allow other jobs to
    # move up in the eligible queue.  The job is then resumed (after
    # 30 second wait period.
    #
    # Written by Dirk Colbry August 17, 2010
    # © 2010 Michigan State University Board of Trustees.

    jobid=$1
    if [ "$1" == "" ]
    then
    	echo "job id required"
    	exit 1
    fi

    qhold $1
    echo "Waiting 30 seconds for queue to settle..."
    sleep 30
    qrls $1
    showjobs


I put copies of these scripts in the powertools module. To use them just type
the following in one of the developer nodes:



    module load powertools
    move2top JOBID
    move2bot JOBID


Hope you find this useful,

  * Dirk

* * *

Dr. Dirk Joel Luchini Colbry  
Research Specialist  
Institute for Cyber-Enabled Research (iCER)  
Michigan State University  
1445 Biomedical and Physical Sciences Building (BPS),  
East Lansing, MI 48824-1226  
email: dirk (at) colbry.com  
web: <http://www.dirk.colbry.com>  
phone: (517) 355-0730

To ask an HPC or iCER related technical question or to schedule a consulting
appointment, please visit: <http://hpcc.msu.edu/contact>

[View
Online](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2010/08/17/Reordering+the+Eligible+Jobs+in+Your+Queue)

Blogpost migrated from [ICER Wiki](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2010/08/17/Reordering+the+Eligible+Jobs+in+Your+Queue) using custom python script. Comment on errors below.
