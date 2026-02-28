Title: Using an X11 Virtual Frame Buffer to run GUI jobs in batch mode on the HPC.
Date: 2018-12-20
Tags: HPC

![X11 Logo](//upload.wikimedia.org/wikipedia/commons/a/ab/X11.png){ width=20%, align=right, hspace=10}

I have an example program that came with [BCCD](http://bccd.net/) called Pandemic which I wanted to run on our local HPCC. Unfortunately Pandemic requires X11 to run and I would get a segmentation fault every time I ran it in the batch system.

This blog post shows how I used the X11 Virtual Frame Buffer (Xvfb) to enable X11 in batch mode.  This example uses SLURM running in CentOS7.  This trick can come in really handing when you are using MATLAB to because last I checked it needed X11 to run in order to generate and save figures. This will let you do that even in batch mode.

First, here is the batch script for the OpenMP version (Should work for serial jobs as well).

```bash
#!/bin/bash
#SBATCH --time=00:10:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=10G
#SBATCH --job-name Pandemic-OpenMP

cd ${SLURM_SUBMIT_DIR}

# Have X11 find an open display number and communicate the number
# though a temporary file to set the environment variable.
display_file=.tmp_display.txt
Xvfb -displayfd 1 -auth /dev/null  1>$display_file 2> /dev/null &
sleep 5
export DISPLAY=:`cat $display_file`
echo "DISPLAY set to $DISPLAY"
rm $display_file

# Benchmark program with different numbers of processes
export OMP_NUM_THREADS=16
time ./Pandemic.c-openmp
export OMP_NUM_THREADS=8
time ./Pandemic.c-openmp
export OMP_NUM_THREADS=4
time ./Pandemic.c-openmp
export OMP_NUM_THREADS=2
time ./Pandemic.c-openmp
export OMP_NUM_THREADS=1
time ./Pandemic.c-openmp
echo done

# Report job statistics
scontrol show job $SLURM_JOB_ID

```  
And here is the job I got working with MPI. Notice it is basically the same but I need to pass the DISPLAY variable though MPI for it to work.  
```bash
#!/bin/bash
#SBATCH --time=00:10:00
#SBATCH --ntasks=16
#SBATCH --cpus-per-task=1
#SBATCH --mem=10G
#SBATCH --job-name Pandemic-MPI

cd ${SLURM_SUBMIT_DIR}
module swap GNU Intel
module load OpenMPI

# Have X11 find an open display number and communicate the number
# though a temporary file to set the environment variable.
display_file=.tmp_display.txt
Xvfb -displayfd 1 -auth /dev/null  1>$display_file 2> /dev/null &
sleep 5
export DISPLAY=:`cat $display_file`
echo "DISPLAY set to $DISPLAY"
rm $display_file

# Benchmark program with different numbers of processes
time mpirun -n 16 -x DISPLAY=$HOSTNAME:$DISPLAY ./Pandemic.c-mpi
time mpirun -n 8 -x DISPLAY=$HOSTNAME$DISPLAY ./Pandemic.c-mpi
time mpirun -n 4 -x DISPLAY=$HOSTNAME$DISPLAY ./Pandemic.c-mpi
time mpirun -n 2 -x DISPLAY=$HOSTNAME$DISPLAY ./Pandemic.c-mpi
time mpirun -n 1 -x DISPLAY=$HOSTNAME$DISPLAY ./Pandemic.c-mpi

# Report job statistics
scontrol show job $SLURM_JOB_ID

```

Hope you find this useful.
