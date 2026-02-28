Title: Tensorflow and Keras/PyTorch on the HPCC
Date: 2020-02-27
Tags: HPCC, Teaching

![The Tensorflow Logo](//avatars0.githubusercontent.com/u/15658638?s=200&v=4)

Every few semesters I have a Tensorflow example I want to try on the HPCC.  I'm not an expert on the software and between the HPCC, CUDA, Tensorflow, Keras, Python, Anaconda, etc. there are a lot of continuously changing and moving parts. Seems like when I figure out how to get it working something changes.  This time around wasn't too bad so I thought I would share my latest install instructions.

### Step 1: Install Anaconda Python
Here is a video I made a while ago about how to download and install Anaconda on the HPC.

<iframe width="560" height="315" src="https://www.youtube.com/embed/g0rGb6QqBPo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Step 2: Make a Tensor Conda Environment
On one of the development nodes create a Conda environment using the following commands:

```bash
conda create --prefix ./tensorflow-env tensorflow-gpu keras pytorch
conda init bash
exit
```

### Step 3: Test Conda 
Now we need to test keras and tensorflow.  I found an example on the internet and had to fix a few bugs. I am not sure how good an example is but it is good enough to run as a benchmark test. You can download the example file ([convolutional.py](//colbrydi.github.io/images/convolutional.py), or just use the following commands on a dev-node on the HPC:

```bash
wget https://colbrydi.github.io/images/convolutional.py
conda activate ./tensorflow-env
time python convolution.py
```
Running the above took me about 8 minutes on dev-intel18 about 1.3 minutes on dev-intel16-k80 and about 2 minutes on dev-intel14-k20.  I also ran on the special Volta node (nvl-001) which is only available to buy-in users. That thing only to about 30 seconds. Here are the commands I used (Requires buy-in access):

```bash
salloc --gres=gpu:1 --nodelist=nvl-001 --time=00:10:00 --account=cmse
conda activate ./tensorflow-env
time srun python convolutional.py
```

### Step 4: SLURM Script
To run this in a SLURM script you need to request GPUs and use the srun command. Here is an example:

```bash
#!/bin/bash --login
#SBATCH --time=01:00:00
#SBATCH -c 1
#SBATCH -n 1
#SBATCH --gres=gpu:1
#SBATCH --mem=4gb

module load powertools

conda activate ../tensorflow-env

time srun python convolutional.py

#Prints out job statistics
js ${SLURM_JOB_ID}
```

This installation is probably not optimal but seems to work consistently.  

