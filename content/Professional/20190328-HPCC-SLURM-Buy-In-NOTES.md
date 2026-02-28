Title: HPCC SLURM Buy-in Notes
Date: 2019-03-28
Tags: HPC

[![SLURM Logo](//upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Slurm_logo.svg/2000px-Slurm_logo.svg.png){ width=200, align=right, hspace=10}](https://slurm.schedmd.com/)

This year, the HPCC moved over to SLURM.  Overall, I think the new scheduler is nice but it required me to relearn a bunch of things I have gotten to know by reflex.

One nice new feature is that I can manage our own Buy-in account.  The CMSE department has multiple buy-in nodes. For example, the command to **show** everyone on the CMSE account is:

```
sacctmgr show association account=cmse
```

If I want to **add** someone to the CMSE buy-in account I just do the following:


```
sacctmgr add user account=cmse name=colbrydi
```

Then if I want to **delete** someone from he CMSE buy-in account is just as easy:

```
sacctmgr delete user account=cmse name=colbrydi
```

The HPCC staff also provides the following useful powertools that users can access by running ```module load powertools```:

**priority_status** or **buyin_status** - equivalent commands that shows all of your buy-in nodes and who is currently running on them.

To use the buy-in account you need to specifically use the account option in the job script (I think).  For example, the following SBATCH commands should request one of the Volta GPU cards on the cmse account:

```
#SBATCH --gres=gpu:1  
#SBATCH --nodelist=nvl-001
#SBATCH --time=08:00:00
#SBATCH --account=cmse
```

Many of our people want to use the Volta over Jupyterhub run though the [webrdp](https://webrdp.hpcc.msu.edu) website.  To do this, you would log into [webrdp](https://webrdp.hpcc.msu.edu), open a terminal on the [webrdp](https://webrdp.hpcc.msu.edu) desktop, ssh to one of the dev nodes and then issue the following command:

```
salloc --gres=gpu:1  --x11 --nodelist=nvl-001 --time=08:00:00 --mail-type=BEGIN --account=cmse
```

Once the job starts, you would just type ```jupyter notebook``` assuming you have it installed.


Hope you find these notes useful.

- Dirk
