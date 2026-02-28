Title: Playing around with git
Date: 2012-01-26
Tags: HPC, Migration

Blog post **edited** by Anonymous \- "Migration of unmigrated content due to
installation of a new plugin"

# Looking at an older version

Use "git checkout HASH" where HASH is that long number in the "git log" file.
You can use the command to temporarily revert to an old version in git. To
come back to the master version and discard any temporary changes just run the
"git checkout master" command.

# pulling in changes made by a collaborator.

To pull in changes made by another user in a different directory (For example
from a tar.gz file). Use the following command:

    
    
    git pull /mnt/home/colbrydi/UserCode/greerjos/powertools master
    

Check the changes and then upload them to the external repository:

    
    
    git log
    git push
    

[View
Online](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2012/01/26/Playing+around+with+git)

Blogpost migrated from [ICER Wiki](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2012/01/26/Playing+around+with+git) using custom python script. Comment on errors below.
