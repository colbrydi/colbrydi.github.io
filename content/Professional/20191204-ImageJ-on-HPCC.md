Title: Running ImageJ on the HPCC
Date: 2019-12-04
Tags: HPC

![Fiji logo](//imagej.net/_images/a/ae/Fiji-icon.png){ width=200, align=right, hspace=10}

A group working over in Plant and Soil Sciences are experts on ImageJ but are relatively new to the HPCC.  Together we put together a workflow for getting ImageJ up and running on the HPCC.

### Step 1: Log onto the HPCC with an X11 connection

Log onto the HPC using an X11 connection.  You need x11 in order to test the install using the Graphical User Interface (GUI).  If you are on windows, I recommend [MobaXTerm](//mobaxterm.mobatek.net/) as an easy way to get started, if you are on Mac you may need to install [XQuarts](https://www.xquartz.org/).

If you don't have X11 working you can try logging in using the HPCC remote server and a "full linux desktop" by going to the following website:

https://webrdp.hpcc.msu.edu

You can test if graphics are working by typing the following on the command line:

```bash
xeyes
```

### Step 2: Install ImageJ

For this step I recommend installing [Fiji](https://fiji.sc/) (Fiji is just ImageJ) which a little easier to use than ImageJ proper.  For one thing it makes installing a few plug-ins much easier.

Download the 64-bit installer into your home directory on the HPCC.  Go to the [Fiji](//imagej.net/Fiji/Downloads) website to get a URL link to the latest version.  Once you have the URL you can run the following command on an HPC Development node:

```bash
wget https://downloads.imagej.net/fiji/latest/fiji-linux64.zip
```

After the file has downloaded you just need to unzip the file using the following command:

```bash
unzip fiji-linux64.zip
```

Test ImageJ using the following command:

```bash
~/Fiji.app/ImageJ-linux64
```

The first time running it will ask if you want to run the "updater." I would recommend doing this.

### Step 3: Install needed plugins

Once you have Fiji running you shold be able to install most plugins from the user interface.  You can also copy plugin jar files to the plugins folder inside the Fiji.app folder.

### Step 4: Write a Macro

You can run for about 2 hours on any of the HPCC development nodes, however, to really take advantage of the HPCC you want to run in batch mode.  Batch mode does not let you use the mouse and click on the graphics which means you need to create an ImageJ macro that runs from start to end without any user input.  For now I will assume that you know how to make a macro, if not, you may have to look for some sort of online tutorial or read the [manual](https://imagej.nih.gov/ij/docs/guide/146-14.html),

If you want to just do a quick test I recmmend making a macro with just a "hello world" print command as follows:

```
print(hello world);
```

Save the file as ```myMacro.ijm```

### Step 5: Submit the macro to the scheduler

Let us assume that your macro name is ```myMacro.ijm``` then the following submission script should work to get your macro running in SLURM:

```bash
#!/bin/bash
#SBATCH --mem=4gb
#SBATCH --time=04:00:00
#SBATCH -n 1
#SBATCH -c 1

module load java
module load powertools

srun ~/Fiji.app/ImageJ-linux64 --headless --memory=4000M -macro myMacro.ijm

js $SLURM_JOB_ID
```

If we call the above script ```runFiji.sb``` then you can submit the job to the SLURM scheduler using the following command:

```bash
sbatch runFiji.sb
```

That should be it. You can change the required memory or the amount of time it takes to run.  
