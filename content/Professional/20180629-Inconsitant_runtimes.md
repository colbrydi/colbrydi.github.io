Title: Managing Inconsistent Runtimes on the HPCC
Date: 2018-06-29
Tags: HPC

One of our postdocs stopped by my office today to talk about a problem with inconsistant runtimes on our [HPCC](//icer.msu.edu).  This user is running a lot of jobs with 512 cores (current cpu limit is 520).  The problem is that it is really difficult for the user to estimate the walltimes. There is a 2x difference in walltimes on the HPCC.  The code has been tested on other large scale systems with much less variation. The user would prefer more consistent runtimes and did not mind waiting in the queue (although less queue time is better).  

The problem is that there are many things that can impact the runtime of a job. The HPCC runs at over 95% utilization most of the time so many of the resources are in contention.  Without additional information, my best guess is that the bottleneck is MPI communication over the high speed network. If this is the case, I hypothesize that moving more processes to the same nodes (instead of spread across the cluster) will help reduce network competition with other users and result in more consistent walltimes. Here are some things I suggested the user try:

- Open a ticket with iCER and see if you can set up a consulting appointment. They may be able to get much better idea about what resources are in contention and causing the bottleneck: [https://contact.icer.msu.edu/contact](https://contact.icer.msu.edu/contact)
- Add “qstat -f ${PBS_JOBID}” to the end of the jobscript.  This will provide some stats that may help us understand differences between jobs that run fast and slow.   
- Try different core and node ratios (ex. nodes=128:ppn=4, nodes=64:ppn=8, nodes=32:ppn=8 etc.). Although increasing the ppn will likely make queue times longer, i believe the overall runtime will be more consistent.
- Start the process to get DOE and XSEDE allocations.  Create XSEDE Portal account here: [https://portal.xsede.org/](https://portal.xsede.org/) and send me your login name when you get it so we can add you to the MSU campus champion account.

Anyone else have a similar problem?  Other suggestions that I may have missed?

** Dirk **
