Title: Choosing more than one architecture type
Date: 2012-08-28
Tags: HPC, example, Migration

Blog post **edited** by Anonymous \- "Migration of unmigrated content due to
installation of a new plugin"

Although all of our nodes are binary compatible, the HPCC is a heterogeneous
cluster based built from many different types of nodes. The node types are
based on the type of architecture that the node is built on and the year the
nodes where purchased. Here is a current list:

Cluster name

|

Development node

|

Chip Manufacturer

|

Year Purchased

|

Node Prefix  
  
---|---|---|---|---  
  
amd05

|

dev-amd05

|

AMD

|

2005

|

amd  
  
intel07

|

dev-intel07

|

Intel

|

2007

|

scw  
  
amd09

|

dev-amd09

|

AMD

|

2009

|

afn  
  
gfx10

|

dev-gfx10

|

Intel with nVidia Graphics Card

|

2010

|

nvx  
  
intel10

|

dev-intel10

|

Intel

|

2010

|

icx  
  
intel11

|

n/a

|

intel

|

2011

|

ifi  
  
You can specify a specific architechture in your submission script using
feature= command. For example the following will only run on the intel10 node:

    
    
    #!/bin/bash --login
    #PBS -l nodes=1:ppn=1,mem=1gb,feature=intel10,walltime=03:59:00
    #PBS -j oe
    
    cd ${PBS_O_WORKDIR}
    
    #Your stuff here...
    
    

You can also specifiy multipule architechtures using the PIPE (OR) charicture.
For example the following will run on the intel07 or the intel10 nodes:

    
    
    #!/bin/bash --login
    #PBS -l nodes=1:ppn=1,mem=500mb,feature=intel07|intel10,walltime=00:05:00
    #PBS -j oe
    
    cd ${PBS_O_WORKDIR}
    
    #Your stuff here...
    

Unfortunately, as far as I can tell, the gfx10 nodes will not work using the
OR syntax. This is probably because the gfx10 nodes also use a different
network fabric (gbe) and I have not figured out the way use more complex logic
with the feature= resource.

[View
Online](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2012/08/28/Choosing+more+than+one+architecture+type)

Blogpost migrated from [ICER Wiki](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2012/08/28/Choosing+more+than+one+architecture+type) using custom python script. Comment on errors below.
