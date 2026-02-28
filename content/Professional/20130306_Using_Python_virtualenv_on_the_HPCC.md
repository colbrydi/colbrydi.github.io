Title: Using Python virtualenv on the HPCC
Date: 2013-03-06
Tags: HPC, example, Migration

Blog post **edited** by Anonymous \- "Migration of unmigrated content due to
installation of a new plugin"

Python has a lot of packages, modules and libraries that researchers may want
to use. However, it is difficult for iCER and the HPCC to keep up with and
install all of the different libraries, versions, and conflicts between them.
Users who need Python software packages installed on the HPCC have the
following choices:

  * Try to install their own copy of Python and the modules in their home directories. (gives researchers full control but can be difficult and time consuming).
  * Ask HPCC staff to install the software in the base Python installation (This option could easily be rejected due to software conflicts)
  * Ask HPCC staff to install the software in a separate system module (This option is more forgiving of different versions but still requires the user to wait on HPCC staff to complete and test the install)
  * Use virtualenv (this works best if the software uses easy_install or pip and has the advantage of putting control in the hands of the researcher, This option also give the researcher the ability to explore which is integral to the research process)

The remainder of this post will explain how to use virtualenv on the HPCC.
Documentation for virtualenv can be found at the following website:

<http://pypi.python.org/pypi/virtualenv>

**Step 1:** make sure you are on a developer node and use system modules to
load the Python version you want to use. You can see the default version of
Python by typing the following:

    
    
    module list
    

As of writing this post, my default was set to Python/2.7.2. If you need
another vision you can see what is available by typing the following:

    
    
    module spider Python
    

To load a different version of python use the "module unload" and "module
load" commands. For example the following will switch from the default version
of Python to 2.6.7:

    
    
    module unload Python
    module load Python/2.6.7
    

**Step 2:** use system modules to load existing Python related software. Many
Python packages are already installed and can be loaded using the module
system. Use the following command to list all available modules:

    
    
    module avail
    

Since most of the Python modules have the word "py" in them so you can use the
spider command to see what is installed:

    
    
    module spider py
    

Once you know what is available, you can load the modules using "module load"
command. For example:

    
    
    module load NumPy
    module load SciPy
    module load PIL
    module load matplotlib
    

**Step 3:** at this point you can make your own virtual Python environment.
This environment lets you install packages using easy_install and pip in your
how directory. You can also have multiple different virtual Python
environments, each one with a different name. For this example, I am going to
call my virtual Python environment "myPy". Use the following commands to
create and activate a virtual environment:

    
    
      
    virtualenv myPy
    source myPy/bin/activate
    

After running the source command, you should see your normal command prompt
with a (myPy) in front of it. This tells you, that you are running in the myPy
virtual environment.

**Step 4:** Now that you are running in your virtual environment you can run
easy_install or pip commands to install almost all Python modules. For
example, the following command installed a redditanalysis package:

    
    
    easy_install redditanalysis
    

**Step 5:** Once you have everything installed test out your program. If you
need to leave the Python virtual environment just type the following command:

    
    
    deactivate
    

If you log out of the system and log back in, you can reactivate the virtual
environment as before. Just make sure you load the modules you need:

    
    
    module load NumPy
    module load SciPy
    module load PIL
    module load matplotlib
    source myPy/bin/activate
    

**Submission Scripts**  
Now that you have your own version of Python running, you will want to use it
in your submission scripts. The following job submission script can be used as
a template for running virtualenv Python jobs (note this job assumes that your
myPy folder is in your home directory):

    
    
    #!/bin/bash --login
    #PBS -j oe
    #PBS -l walltime=03:00:00,mem=2gb,nodes=1:ppn=1
    
    cd ${PBS_O_WORKDIR}
    
    module load NumPy
    module load SciPy
    module load PIL
    module load matplotlib
    source ~/myPy/bin/activate
    
    python mypythonscript.py
    
    qstat -f ${PBS_JOBID}
    

[View
Online](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2013/03/06/Using+Python+virtualenv+on+the+HPCC)

Blogpost migrated from [ICER Wiki](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2013/03/06/Using+Python+virtualenv+on+the+HPCC) using custom python script. Comment on errors below.
