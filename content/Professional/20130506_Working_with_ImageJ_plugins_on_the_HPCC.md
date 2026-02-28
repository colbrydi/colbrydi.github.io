Title: Working with ImageJ plugins on the HPCC
Date: 2013-05-06
Tags: HPC, example, Migration

Blog post **edited** by Anonymous \- "Migration of unmigrated content due to
installation of a new plugin"

Post written by Dan Perez (iCER Intern)

### Errors

One of the iCER users has had problems getting ImageJ - ImageViewer scripts
and plugins working on the HPCC. The ImageViewer classes, plugins, and scripts
are in a directory called MyMacro. When I execute RunJavaOnly.sh I get:

    
    
    cd MyMacro
    module load Java
    ./RunJavaOnly.sh
    
    File > Open > 30_1_DE2_C2crop/temp/mask0001.tif (this is an 8-bit image)
    
    Plugins > Analyze > Particle Analyser
    
    Error:
    Plugin org.double.bonej.ParticleCounter did not find required class: javax/media/j3d/Shape3D
    

And when I execute ./runmacro.sh I get:

    
    
    ./runmacro.sh
    
    Error:
    Unrecognized command: 3D Fast Filters
    

### Fixes

##### RunJavaOnly.sh

I've had some success getting this to work by installing the latest version of
ImageJ (v1.46r) and adding class paths and a shared object path:

1\. Download the latest version of ImageJ. This will create a directory called
ImageJ in you home directory.

    
    
    cd ~
    wget http://rsb.info.nih.gov/ij/download/linux/ij146-linux64.tar.gz
    tar -zxf ij146-linux64.tar.gz
    

2\. Delete the old version of ImageJ and copy the new version to your MyMacro
directory. Assuming that MyMacro is also in your home directory:

    
    
    rm MyMacro/ij-1.45q.jar
    cp ImageJ/ij.jar MyMacro/ij.jar
    

3\. Edit the RunJavaOnly.sh script. Java needs to know where to find the
libj3dcore-ogl.so shared object file (it's in the
/opt/software/Java3D/lib/amd64 directory). You'll also need to update the
script to use the new version of ImageJ you just installed. The script should
look like:

Post created by Daniel Perez (ICER Student Intern):

    
    
    #!/bin/bash
    java -Xmx8000m -Dplugins.dir=./plugins/ -Djava.library.path=/opt/software/Java3D/lib/amd64 -jar ./ij.jar &
    

4\. Edit the MyMacro/ij.jar/META-INF/MANIFEST.MF file. Java needs to know
where to find Java3D classes. Add the following line to the end of the file:

    
    
    Class-Path: /opt/software/Java3D/lib/ext/j3dcore.jar /opt/software/Java3D/lib/ext/j3dutils.jar
    

If this continues to create problems, you can also try adding
/opt/software/Java3D/lib/ext/vecmath.jar to the Class-Path. At this point I
think RunJavaOnly.sh works. However, I don't know what this program is
supposed to do, so Dirk should test this.

##### runmacro.sh

Works better using the plugins directory (instead of plugins2):

    
    
    #!/bin/bash -login
    java -Xmx8000m -Dplugins.dir=./plugins/ -jar ./ij.jar -macro ./SplitLargePiece.txt
    

Runs for awhile. Don't get the 3D Fast Filters error. Get the following errors
instead:

    
    
    No window with the title "particleID_parts" found.
    This command requires a stack.
    

[View
Online](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2013/05/06/Working+with+ImageJ+plugins+on+the+HPCC)

Blogpost migrated from [ICER Wiki](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2013/05/06/Working+with+ImageJ+plugins+on+the+HPCC) using custom python script. Comment on errors below.
