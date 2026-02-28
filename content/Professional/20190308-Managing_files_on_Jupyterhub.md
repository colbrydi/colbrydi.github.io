Title: Managing Files on the MSU Engineering Jupyterhub server
Date: 2019-03-08
Tags: Jupyter

![Disk Icon](//colbrydi.github.io/images/Floppy_Disk.png){ width=200, align=right, hspace=10}

The MSU Engineering Jupyterhub server provides 2GB of disk storage space for each student.  It can be helpful to learn some disk management so you can use this space effectively.

For example, pip install uses a temporary folder when downloading packages.  Periodically, deleting this folder can significantly free up space.  

```rm -rf ~/.cache```

Also, some functions in the scikit learn and seaboarn libraries download their own data folders. You may also want to have them delete those once they are no longer using those packages.

```
rm -rf  ~/scikit_learn_data
rm -rf ~/seaborn-data
```

Another good command to learn is the “dh” command.  I like to run the following in my home directory to see which of my folders are taking up the most space:

```du -sh ~/*```

To include hidden folders use:

```du -sch .[!.]* *```

To also sort the results (may take a while):

```du -sch .[!.]* * | sort -h```

- Dirk
