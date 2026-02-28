Title: Solution to BLCR Segmentation Bug
Date: 2012-05-15
Tags: HPC, Migration

Blog post **edited** by Anonymous \- "Migrated to Confluence 4.0"

After a few months since our install of RHEL6 and my original post reporting
the problem with BLCR:

  * <https://wiki.hpcc.msu.edu/x/c6LT>

We have found and tested a solution that works on our system. Here is a link
to a detailed description of the Prelink problem/BLCR and how to fix it:

  * <http://en.wikipedia.org/wiki/Prelink>
  * <https://upc-bugs.lbl.gov/blcr/doc/html/FAQ.html#prelink>

Note, for a while I was not convinced that Prelinking was a problem or the
only problem because my BLCR script used the --save-all option. Using this
option seems to have also messed up our system. Removing the --save-all option
is not a problem on our system since all of our compute nodes have same image
and directory structure.

This has already made a lot of users on our HPC system happy because it allows
them to get around our walltime limits and makes their jobs more robust to
node failure.

  * Dirk

[View
Online](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2012/05/15/Solution+to+BLCR+Segmentation+Bug)

Blogpost migrated from [ICER Wiki](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2012/05/15/Solution+to+BLCR+Segmentation+Bug) using custom python script. Comment on errors below.
