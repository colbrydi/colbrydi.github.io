Title: Automatically log into a dev-node from gateway
Date: 2012-03-27

Tags: HPC, example, Migration

Blog post **edited** by Anonymous \- "Migration of unmigrated content due to
installation of a new plugin"

You are not allowed to do any computation on the gateway nodes. Mostly they
are there as a firewall and a place to check and submit jobs. Many users find
it annoying to log into gateway and then have to immediately log into one of
the dev nodes. Although I have not tested it thoughouly, you can add the
following script to the beginning of your .bash_profile file and it will
automaticlly log you into a random dev node. Give it a try:



    if [ "$HOSTNAME" == "gateway-01" ]; then
            /opt/software/powertools/bin/dev
    fi


  * Dirk

[View
Online](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2012/03/27/Automatically+log+into+a+dev-
node+from+gateway)

Blogpost migrated from [ICER Wiki](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2012/03/27/Automatically+log+into+a+dev-node+from+gateway) using custom python script. Comment on errors below.
