Title: Makefile Mystery
Date: 2012-03-05
Tags: HPC, example, Migration

Blog post **edited** by Anonymous \- "Migration of unmigrated content due to
installation of a new plugin"

I was working with a makfile the other day and I came across a "feature" that
I was not aware of. When running my makefile I saw the following lines appear:

    cat build.sh >build
    chmod a+x build


I could not find any part of the makefile that used either the cat or the
chmod command yet it seemed to work. Upon further testing I discovered that
Make will automatically convert a shell script to an executable. For example,
consider the following makefile

**"Makefile"**



    all:	demo

    demo:	test
    	./test

    clean:
    	rm test


This code seems streatforward but there is no rule to build test and my clean
removes test. However, the script works fine if I include the following in the
same directory:

**"test.sh"**



    #!/bin/bash
    #
    echo "This is a test!!!!, Hello world"


Now when I run make, I get the following output:



    >make
    cat test.sh >test
    chmod a+x test
    ./test
    This is a test!!!!, Hello world


This is a really neat feature but it threw me for a loop.

[View
Online](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2012/03/05/Makefile+Mystery)

Blogpost migrated from [ICER Wiki](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2012/03/05/Makefile+Mystery) using custom python script. Comment on errors below.
