Title: Building a VM suitable for distribution to a class on a USB drive
Date: 2012-11-15
Tags: HPC, example, Migration

Blog post **edited** by Anonymous \- "Migration of unmigrated content due to
installation of a new plugin"

I am teaching a class to first and second year undergrads. Since we will be
using many different types of software I was discouraged by the idea of
installing all of the software they would need on all of their computers.
Although installing software is a very useful exercise, the many different
platforms and laptops make this task prohibitively hard to manage.

In the past I have used "[Portable Apps](http://portableapps.com/)" to deliver
software to windows users. This works great and eliminates the need to install
a lot of software. However, typical portable apps do not work on macs and more
than half of my class use macs.

So, my next thought was to use a lightweight Virtual Machine (VM). I had some
supply funds for the students so I bought them all 16GB USB drives and my plan
is to install the VM on the drives and use the drives to also pass around the
data files the students need for their projects. I would just put all the data
files on the VM but each student needs a different set of files and they would
make the VM much bigger than the 16GB that I had available.

My plan is to create a USB drive with a standard Virtual Machine Image and
then Individual project data for each student. Here is the process I went
though to make these drives:

### Choosing a VM platform and building the machine:

I created a [Lubuntu](http://lubuntu.net/) VM using
[VMWare](http://www.vmware.com/) and installed all of the software I wanted
the students to have. This included; Python (with a lot of packages), ImageJ,
FFmpeg and others. Then I found out that VMWare Player doesn’t run on a mac so
I had to switch to [VirtualBox](https://www.virtualbox.org/). I used the
following instructions to convert the VM:

<http://www.ubuntugeek.com/howto-convert-vmware-image-to-virtualbox-image.html>

**Take away** : Use VirtualBox, it works the best cross platform and is
available for free

### Copy the VM to the USB drive (first attempt):

Once I had a working VM I copied over the file to the USB drive and tried to
run it. Unfortunately, trying to boot the VM gave me all types of errors and I
ended up realizing that the USB drives are formatted using FAT32 and can not
contain files larger than 2gb
![\(sad\)](https://wiki.hpcc.msu.edu/s/en_US/8100/4410012ac87e845516b70bc69b6f7a893eabaa5a/_/images/icons/emoticons/sad.svg)

**Take away** : Can't use FAT32 to save large VM drive files

### Reformat and copy the VM to the USB drive (second attempt):

So, I did some research and both mac and windows support exFAT a new files
system from Microsoft specifically designed for larger files on USB drives.
Great! I formatted the USB drive to use exFAT, copied over the VM and then
individually copied the data files each student needed onto their USB drive.

Problem 1: exFAT drive formatted on a MAC

When I passed the drives out in class today they would not be recognized by
the windows machine. It seems that exFAT only works in one direction. When I
format the drive on my MAC and try to read it on windows it doesn’t work.
However, if I format exFAT on windows my MAC can read it fine.

Problem 2: Missing Linux USB Drivers

Another problem I did not consider is that the exFAT drive can not be
recognized in the Lubuntu VM. So, although the VM worked fine on the MACs, the
students could not read their data.

### Fix limitations of exFAT (third attempt):

We did some brainstorming and came up with the following possible solutions
that cover both problems:

**Option 1**. Format exFAT on windows machines (so they will work on both MAC
and windows). Figure out how to install exFAT drivers in Lubuntu.

This option ended up not being too difficult. I used the following commands to
install exFAT on the Lubuntu machine:

    
    
    sudo apt-add-repository ppa:relan/exFAT
    sudo apt-get update
    sudo apt-get install fuse-exFAT exFAT-utils
    

**Option 2**. Duel partition the USB drive with one exFAT drive (Formatted on
windows) and one FAT32 drive for the data.

Seems like a lot of work and I would need to switch to the disk duplicate tool
(dd) to make the copies.

**Option 3**. Format the entire drive back to FAT32 and break the VM down into
smaller files.

I can't find a way to break the large files apart in Virtual box. I could do
it with some third party splitting software but then I would need to figure
out how to merge the files on each individual computer. Not really a step I
prefer to take.

The VMDK files in VMWear are already broken up into 2gb or less files. I may
be able to convert back to the VMDK files and load the VM in Virtual box
directly.

**Option 4**. Try a different large-scale file system such as NTSF and get
that to work on all of the platforms.

I was told that this could be tricky especially if the students to not
properly eject their USB drives. So far I have avoided this option.

**Final Take Aways** : Option 1 worked for me. Use VirtualBox and an exFAT
formatted USB drive. Make sure the exFAT drive is formatted in Windows and
install exFAT drivers on your Linux VM before distribution.  

\- Dirk

[View
Online](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2012/11/15/Building+a+VM+suitable+for+distribution+to+a+class+on+a+USB+drive)

Blogpost migrated from [ICER Wiki](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2012/11/15/Building+a+VM+suitable+for+distribution+to+a+class+on+a+USB+drive) using custom python script. Comment on errors below.
