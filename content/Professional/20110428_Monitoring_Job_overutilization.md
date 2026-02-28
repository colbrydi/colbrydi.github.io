Title: Monitoring Job overutilization
Date: 2011-04-28
Tags: HPC, example, Migration

Blog post **edited** by Anonymous \- "Migration of unmigrated content due to
installation of a new plugin"

This week I was debugging some user code that was over-utilizing a compute
node. The job was intended to use only 1 cpu but one of the job's libraries
ended up using all the cpus on the node. I needing to run a lot of tests to
see what exactly was causing the problem. Since I didn't want my tests to
over-utilize the nodes (too much), I wrote the following job script that will
run a monitor and kill the job if it goes to high over the cpu utilization:

**overutilize.qsub**



    #!/bin/bash
    #PBS -l nodes=1:ppn=1,walltime=168:00:00,mem=2gb,feature=gbe
    #PBS -j oe

    #Change to current working directory
    cd ${PBS_O_WORKDIR}

    #Copy the entire testing directory into its own folder
    mkdir -p ${PBS_JOBID}
    cp -r ./testdir/* ./${PBS_JOBID}
    cd ${PBS_JOBID}

    #Make the name of the executable unique so that more than one test can run on the same node
    export name=`echo "ex+${PBS_JOBID}" | cut -d "." -f 1`
    ln -s testprogram ${name}

    #run the testprogram using the new name (including input arguments)
    ./${name} 2.5 -15 -7.5 &
    export PID=$!

    #Wait for job to get going
    sleep 60

    # Start job monitor
    export per="0"
    (
         #Ensure job does not go over the 120% limit
         while [ "$per" -lt "120" ]
         do
            #pause between checking
    	sleep 22
            #Run top in batch mode but with only one iteration
            # Pick out job with the unique executable name and grab the CPU utilization (9th item)
    	export per=`top -b -n 1 -u ${USER} | grep ${name} | awk {'print $9'}`
    	echo "per=$per"
         done
         kill $PID
         echo "Killed $PID"
   ) &
    wpid=$!

    #Wait for job to complete
    wait $PID

    #Kill off wait command if it is still running
    kill $wpid

    #Display all the stats for the job
    qstat -f ${PBS_JOBID}



[View
Online](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2011/04/28/Monitoring+Job+overutilization)

Blogpost migrated from [ICER Wiki](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2011/04/28/Monitoring+Job+overutilization) using custom python script. Comment on errors below.
