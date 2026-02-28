Title: HFSS script
Date: 2011-06-08
Tags: HPC, example, Migration

Blog post **edited** by [Pat Bills](
https://wiki.hpcc.msu.edu/display/~billspat@msu.edu

) \- "Migration of unmigrated content due to installation of a new plugin"

HFSS is available on the MSU HPCC. You can run interactively or in batch mode.

You may run the GUI interactive using the iCER Remote Desktop Gateway. See
[Copy of Connecting with a Remote Desktop
Client](https://wiki.hpcc.msu.edu/pages/[viewpage.action](./images/viewpage.action)?pageId=1343579)

you must run HFSS from a development node via a terminal

Connect to the iCER Remote Desktop Gateway

Start a Terminal by clicking The Applications Menu and selecting "Terminal
Emulator"

Once in the terminal, connect to a Development Node, Load the module for HFSS,
and start hfss. When you run for the firs time, it will create a configuration
setup for you. This may take a bit, and appear to be stalled, but please be
patient if the system is busy.

**Start HFSS in the Terminal**



    [billspat@rdpgw-00 ~]$ ssh dev-intel14
    [billspat@dev-intel14 ~]$ module load hfss
    Lmod Warning: hfss not found, loading: HFSS/15.0

    [billspat@eval-k40 ~]$ hfss
    ANSYS Electromagnetics 15.0 Configuration
    =========================================
    Hostname: eval-k40
    User:     billspat
    > Running first-time configuration...
      - *** Skipping dependency verification test ***
      - Retrieving user settings... Done
      - Applying user settings... Done
      - Configuring OCX files... Done
      - Retrieving machine settings... Done
      - Applying machine settings... Done
      - Configuring binaries... Done
    First-time configuration completed successfully.

At which point the GUI/ Window will start. It will ask you a question about
which directories you'd like to use. Please change the scratch folder:

![](https://wiki.hpcc.msu.edu/download/attachments/5411556/[hfss-folderchoice.png](./images/hfss-folderchoice.png)?version=1&modificationDate=1441138478000&api=v2)The default scratch directory is simply /mnt/scratch. We suggest you createyour own folder on scratch, and enter that folder here. You have to firstcheck the "override" box and then type in your scratch folder.You may also use Batch mode to run HFSS jobs on the cluster. Here is anexample HFSS 15.0 submission script written by Andrew Temme that sets up theHFSS job options. For more detail see his excellent [Python Notebook onHFSS](http://nbviewer.ipython.org/urls/bitbucket.org/temmeand/example-ipython-notebooks/raw/master/MSU-supercomputer-HFSS-and-IPython.ipynb)

**hfssrun.qsub**



    #!/bin/bash -login
    #PBS -l walltime=03:59:00,mem=50gb,nodes=19:ppn=1
    #PBS -j oe
    #PBS -m abe
    #PBS -W x=gres:hfss_solve

    module load HFSS/15.0
    export OptFile=${PBS_O_WORKDIR}/Options.txt
    export ANSYSEM_JOB_ID=${PBS_JOBID}
    export ANSYSEM_HOST_FILE=$PBS_NODEFILE
    export LINUX_SSH_BINARY_PATH=/usr/bin
    export ANSYSEM_LINUX_HPC_UTILS=/opt/software/AnsysEM/15.0/AnsysEM15.0/Linux64/schedulers/utils

    cd ${PBS_O_WORKDIR}
    # mkdir -p ${PBS_O_WORKDIR}/scratch

    echo creating batch options list
    echo \$begin \'Config\' > ${OptFile}
    echo \'HFSS/NumCoresPerDistributedTask\'=${PBS_NUM_PPN} >> ${OptFile}
    echo \'HFSS/HPCLicenseType\'=\'Pool\' >> ${OptFile}
    echo \'HFSS/SolveAdaptiveOnly\'=0 >> ${OptFile}
    echo \'HFSS/MPIVendor\'= \'Intel\' >> ${OptFile}
    echo \'HFSS-IE/NumCoresPerDistributedTask\'=${PBS_NUM_PPN}  >> ${OptFile}
    echo \'HFSS-IE/HPCLicenseType\'=\'Pool\' >> ${OptFile}
    echo \'HFSS-IE/SolveAdaptiveOnly\'=0 >> ${OptFile}
    echo \'HFSS-IE/MPIVendor\'=\'Intel\' >> ${OptFile}
    # echo \'tempdirectory\'=\'${PBS_O_WORKDIR}/scratch\' >> ${OptFile}
    echo \$end \'Config\' >> ${OptFile}
    chmod 777 ${OptFile}

    hfss -ng -monitor -distributed -machinelist num=${PBS_NUM_NODES} -batchoptions ${OptFile} -BatchSolve ${PBS_JOBNAME}.hfss

[View
Online](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2011/06/08/HFSS+script)

Blogpost migrated from [ICER Wiki](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2011/06/08/HFSS+script) using custom python script. Comment on errors below.
