Title: Custom Build Systems
Date: 2012-05-15
Tags: HPC, Migration

Blog post **edited** by Anonymous \- "Migrated to Confluence 4.0"

I really get frustrated with Custom Build System (CBS), especially with
software for scientific research. I define a CBS as a set of scripts/makefiles
that are written by the software developers to install their software. In my
experience, writing your own build system is never a good idea. It may work
for you and your closest friends, but chances are the build will break when
you move to a larger system or when someone wants to do something that you did
not expect (which is always the case). There's a reason they call these
"custom" systems: even if your build works great, it is customized to your
systems (hardware, software, file structure, naming conventions, libraries,
etc.). Rarely do CBS include sufficient documentation and in order to get it
to work, an experienced system administrator has to learn your "custom" way of
doing things.

For example, I am currently trying to install some software written for
Physicists. When I first looked at the project webpage, I noticed that the
build system was nonstandard and required its own specialized instructions for
installation. This always makes me cringe, and when the opportunity arose I
asked one of the developers why didn't they use a standard build system? The
response was that the group had an outstanding, experienced programmer who
made a custom build system, complete with a secondary installer to make
installing the support libraries even easier. The developer assured me that
"it just works."

This all sounded good, so I gave it a try. The first problem I encountered is
that the installer focused on single user installs (Unbuntu), and I was asked
to install the software on the HPC in a nonstandard directory. There is no
list of required libraries; instead, they want me to use the support library
installer. The problem here is that our system probably already has many of
the support components installed and it required sudo (super user) access to
the system - which I do not, and should not, use for user-level software
installs.

Despite my reservations, I decided to try just downloading it and following
the directions:

./clean ; ./install

This command results in a bunch of errors, ending with a big FAILED
notification. However, there is no indication from the CBS about how to fix
the problem. So, I now need to read though the CVS scripts and see if I can
figure out what is wrong. If the developers had used a standard build system,
such as autoconfig or cmake, I could have used standard debugging techniques
to try to determine the cause of the errors.

Fixing the larger problem, of CBS that are not robust, requires re-thinking
how we train both computer programmers and research scientists. Basic
[software carpentry](http://software-carpentry.org/) techniques are an
essential skill for modern researchers, and professional programmers need to
be taught WHY following standards and developing robust installation packages
is important. In many cases, the software is the science - and good sciences
is all about reproducibility.

My advice: stick with standard build systems, such as autoconfig or
[cmake](http://www.cmake.org/). Follow standard build and install practices
whenever possible. In the long run, it will mean less work for you and a more
robust and powerful build system than anything custom solution.

  * Dirk

[View
Online](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2012/05/15/Custom+Build+Systems)

Blogpost migrated from [ICER Wiki](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2012/05/15/Custom+Build+Systems) using custom python script. Comment on errors below.
