Title: keepalive script - solution to work around automounter problems
Date: 2012-05-23
Tags: HPC, example, Migration

Blog post **edited** by Anonymous \- "Migration of unmigrated content due to
installation of a new plugin"

Sometimes the automounter does not properly mount the home directories on our
hpcc system. This is not a problem when the job first starts because there is
a epilogue script that runs before each job that verifies the home directory
is mounted before the job starts.

The problem comes when a job is running for a long time with no activity in
the home directory. This may cause the automounter to automatically unmount
the drive unintentionally. Then when the drive is used again sometimes the
mount fails and then the job fails. I wrote the following script that keeps
the directory alive thought the computation and it seems to work.

This script is a part of our Powertools distribution

  * Dirk

    
    
    #!/bin/bash
    #DESCRIPTION Script to keep alive directory mounts
    #LABEL PowerJobs
    #Script to keep alive directory mounts
    # Written by Dirk Colbry
    #
    # USAGE:
    #   source keepalive PATH
    #   ... Do Something ...
    #   kill -9 ${KEEPALIVE}
    #
    # USAGE 2:
    #   alias keepalive="source keepalive"
    #   keepalive PATH
    #   ... Do Something ...
    #   kill -9 ${KEEPALIVE}
    #
    # USAGE 1 ON THE MSU HPCC:
    #   module load powertools
    #   source /opt/software/powertools/doc/keepalive
    #   ... Do Something ...
    #   kill -9 ${KEEPALIVE}
    #
    # USAGE 2 ON THE MSU HPCC:
    #   shopt -s expand_aliases
    #   module load powertools
    #   keepalive PATH
    #   ... Do Something ...
    #   kill -9 ${KEEPALIVE}
    # 
    # NOTE: Users are Responsible for Killing the KEEPALIVE Process when their script finishes.
    #
    
    #Set default PATH to current PATH
    dir=$1
    if [ "${dir}" == "" ]
    then
         dir="."
    fi
    
    # This is a two step program. The first step checks to make sure the directory can be 
    # mounted for each node. If the directory can not be mounted then the command returns with
    # an error.
    pbsdsh -u ${PTOOLS_ROOT}/share/KeepAlive/waitformount $dir
    ret=$?
    echo "pbsdsh exited with ${ret}"
    if [ "${ret}" -ne "0" ]
    then
         echo "ERROR- Unable to mount Directory"
         exit 1
    fi
    
    # The second step puts a process on each node that cds to the directory and goes to sleep.
    # This extra process is designed to ensure that the node stays mounted.
    pbsdsh -u ${PTOOLS_ROOT}/KeepAlive/dirsleep $dir &
    KEEPALIVE="${KEEPALIVE} $!" 
    
    

[View
Online](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2012/05/23/keepalive+script+-+solution+to+work+around+automounter+problems)

Blogpost migrated from [ICER Wiki](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2012/05/23/keepalive+script+-+solution+to+work+around+automounter+problems) using custom python script. Comment on errors below.
