Title: Using mpi pernode option
Date: 2010-08-25
Tags: HPC, example, Migration

Blog post **edited** by Anonymous \- "Migration of unmigrated content due to
installation of a new plugin"

The mpiexec (mvapich) pernode option will run a single process for on every
machine with the same host name. For example, if you run a job with
nodes=16:ppn=2, the job's PBS_NODEFILE could look like the following:



    afn-000
    afn-000
    afn-000
    afn-000
    afn-002
    afn-002
    afn-002
    afn-002
    afn-002
    afn-002
    afn-002
    afn-002
    afn-001
    afn-001
    afn-001
    afn-001
    afn-001
    afn-001
    afn-001
    afn-001
    afn-001
    afn-001
    afn-001
    afn-001
    scw-049
    scw-049
    scw-118
    scw-118
    scw-094
    scw-094
    scw-006
    scw-006


If you run using the -pernode option, the job will run on the following nodes:



    afn-000
    afn-002
    afn-001
    scw-049
    scw-118
    scw-094
    scw-006


However, this may be a problem depending on the type of job you are running.
The pernode option may not run the number of nodes asked for by the job script
(in the above example I asked for 16 nodes, however, since some of these 16
are the same node, the pernode option only runs on 7 nodes). Sometimes it is
more desirable to have the mpi job run on the same number of nodes as was
originally requested in the submission script. To do this, I have made the
following script which will generate a config file that can be used to run the
job:

**pernodecofig**



    #!/usr/bin/perl
    # Written by Dirk Colbry - iCERi - August 26, 2009
    # (c) 2010 Michigan State University Board of Trustees.
    #
    # Program to generate a mpiexec config file to run an mpi job with one job per node.
    # This fixes the problem with the -pernode mpiexec option which does not work when
    # two of the nodes are allocated on the same machine.  
    #
    # This function will run the same number of processes as allocated in the nodes= section of
    # the PBS resource request.
    #
    # pernodeconfig ppn nodefile executable arguments
    #   ppn - process per node for the current submission script.
    #   nodefile - nodefile for the current submission script (typically PBS_NODEFILE).
    #   exectuable - name of the executable to be run on each node.
    #   arguments - arguments used for the executable.

    $ppn=$ARGV[0];
    $nodefile=$ARGV[1];

    #Parse the nodefile to find the names of each of the allocated nodes.
    if(-T $nodefile) {
    	open (FILE, "$nodefile") || print "Can't open '$nodefile': $! \n\n";
            @testfile = <FILE>;
    	close(FILE);
    	$count=0;
    	foreach (@testfile) {
    		chomp;
    		$count=$count+1;
    		if($count == $ppn) {
    			$count=0;
    			print "$_\t";
    		}
    	}
    } else {
    	print STDERR "INPUT NOT A TEXT FILE\n";
    	die;
    }

    # Add the executable to the config file
    $numArgs = $#ARGV + 1;
    print " \: ";

    foreach $argnum (2 .. $#ARGV) {
    	print "$ARGV[$argnum] ";
    }
    print "\n"


To use this command you can add the following to your submission script:

**pernodetest.qsub**



    #!/bin/sh
    #PBS -l nodes=16:ppn=2,walltime=00:01:00
    cd ${PBS_O_WORKDIR}

    ./pernodeconfig 2 ${PBS_NODEFILE} hostname > $PBS_JOBID.cfg
    mpiexec -comm none -conf $PBS_JOBID.cfg


This script will output the following nodes which is may be more correct
depending on your job:



    afn-000
    afn-000
    afn-002
    afn-002
    afn-002
    afn-002
    afn-001
    afn-001
    afn-001
    afn-001
    afn-001
    afn-001
    scw-049
    scw-118
    scw-094
    scw-006


Email me if you find this helpful,

  * Dirk

\-----------------------------------------------  
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
Online](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2010/08/25/Using+mpi+pernode+option)

Blogpost migrated from [ICER Wiki](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2010/08/25/Using+mpi+pernode+option) using custom python script. Comment on errors below.
