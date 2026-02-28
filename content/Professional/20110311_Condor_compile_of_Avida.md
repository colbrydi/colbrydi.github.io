Title: Condor compile of Avida
Date: 2011-03-11
Tags: HPC, example, Migration

Blog post **edited** by Anonymous \- "Migration of unmigrated content due to
installation of a new plugin"

Today I figured got a condor_compile version of
[Avida](http://avida.devosoft.org/) working on
[TeraGrid](http://www.teragrid.org/). First, I downloaded Avida to my Teragrid
account:



    > svn checkout https://avida.devosoft.org/svn/stable


Then I modified the build_avida script as follows:

**build_avida**



    #!/bin/sh
    export CC="condor_compile gcc"
    mkdir -p cbuild
    cd cbuild
    cmake "$@" ../
    make -j 10
    make install


Then I run the build script using the following commands:



    > module load cmake
    > ./build_avida
    > ./run_tests


Once Avida builds and tests successfully I write a condor script

**avida.condor**



    #
    # avida.condor
    # Example avida condor submission script
    #

    # Specify your TeraGrid allocation project here.
    +TGProject = "YOUR PROJECT NUMBER HERE"

    universe = vanilla

    #PATH TO CONDOR_COMPILE BUILD OF AVIDA
    # The executable to run. Need the full path. ~/ does not work.
    executable = /home/ba01/u124/dcolbry/avida_condor/work/avida

    #Sets the process id to the avida seed
    arguments = -s $(Process)

    # false: The executable is already on remote machine.
    # true: Copy the executable from the local machine to the remote.
    transfer_executable = false

    # Filenames for standard output, standard error, and Condor log.
    output = output/out.$(Process)
    error = output/err.$(Process)
    log = output/condor.log

    # PATH TO WORK DIRECTORY
    initialdir = /home/ba01/u124/dcolbry/avida_condor/work/

    # The following line is always required. It is the command to submit the above.
    # The number is the number of jobs that you want to run
    queue 5



Make an output directory and submit the job to the condor scheduler using the
following commands:



    > mkdir /home/ba01/u124/dcolbry/avida_condor/work/output
    > condor_submit avida.condor


That did it for me.

  * Dirk

[View
Online](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2011/03/11/Condor+compile+of+Avida)

Blogpost migrated from [ICER Wiki](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2011/03/11/Condor+compile+of+Avida) using custom python script. Comment on errors below.
