Title: Debugging BLCR problem
Date: 2012-04-10
Tags: HPC, Migration

Blog post **edited** by Anonymous \- "Migration of unmigrated content due to
installation of a new plugin"

We have isolated the problem. Details of the solution can be found at the
following blog post: <https://wiki.hpcc.msu.edu/x/qKXT>

We had BLCR working great on our SLES10 HPC system about four months ago (I am
not sure what version of BLCR we where running). We have upgraded our system
to RHEL6.0 and unfortunately BLCR (0.8.3) no longer works. Well, it works
about 80-90% of the time and segfaults another 10-20% when doing the
cr_restart command. I have been trying to come up with a reliable test case to
submit as a bug but the intermediate nature of the problem is making it really
hard to isolate.

I asked the BLCR mailing list and Paul H. Hargrove was quick to reply with
some debug suggestions. One possible problem that was suggested is that having
different /usr/lib/locale/locale-archive files on different nodes could cause
a problem. I did a check using md5sum and we had two different versions of the
file installed on the system. I wrote the following submission script designed
to force a job to only start on a node with the same file. If the md5sum is
different the job just resubmitts itself:



    #!/bin/bash -login
    #PBS -l nodes=1:ppn=1:intel10,walltime=00:10:00,mem=2gb,feature=gbe
    #PBS -j oe
    #PBS -N short_test
    #PBS -t 1

    cd ${PBS_O_WORKDIR}
    module load powertools
    shopt -s expand_aliases

    echo "### ${PBS_ARRAYID} running on $HOSTNAME with ${PBS_JOBID}"

    # 4 hours * 60 minutes * 6 seconds - 60 seconds * 5 minutes
    #export BLCR_WAIT_SEC=$(( 4 * 60 * 60 - 60 * 5))
    export PBS_JOBNAME="short_test"
    export BLCR_WAIT_SEC=30
    export PBS_JOBSCRIPT="$0"
    export BLCR_EMAIL="FALSE"
    echo "Waiting ${BLCR_WAIT_SEC} seconds to run ${PBS_JOBSCRIPT}"

    md5sum /usr/lib/locale/locale-archive > $PBS_ARRAYID.md5sum
    cat $PBS_ARRAYID.md5sum
    if [ -f ${PBS_ARRAYID}.orig ]
    then
            diff $PBS_ARRAYID.md5sum ${PBS_ARRAYID}.orig
            if [ "$?" != 0 ]
            then
                    echo "Not the same nd3sum restarting"
                    qsub -t ${PBS_ARRAYID} -N ${PBS_JOBNAME} ${PBS_JOBSCRIPT}
                    sleep 120
                    exit
            fi
    else
            echo "Running for the first time"
            cp $PBS_ARRAYID.md5sum $PBS_ARRAYID.orig
    fi

    longjob ./NKprob.sh ${PBS_ARRAYID}


Unfortunately, all this test showed me was that the difference in the
/usr/lib/locale/locale-archive files was not the problem I am debugging
(although it could be another problem).

[View
Online](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2012/04/10/Debugging+BLCR+problem)

Blogpost migrated from [ICER Wiki](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2012/04/10/Debugging+BLCR+problem) using custom python script. Comment on errors below.
