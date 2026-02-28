Title: zsh job number autocomplete
Date: 2014-11-16
Tags: HPC, example, Migration

Blog post **edited** by Anonymous \- "Migration of unmigrated content due to
installation of a new plugin"

We do not directly support zsh users on our system. However, many of our more
advanced users enjoy some of the modern and advanced features provided by zsh.
One of these users shared a code snippet that he uses in his ~/.zshrc file to
autocomplete job id numbers. He is letting us share the code for use to our
users who prefer zsh over bash.

 **.zshrc**



    _jobs_list() {
    qstat | grep $USER | cut -d' ' -f1 | cut -d'.' -f1
    }

    _jshow_complete() {
    if (( CURRENT ==2)); then
    jjobs=( $(_jobs_list))
    _multi_parts / jjobs
    else
    _files
    fi
    }
    
    compdef _jshow_complete showstart jdel checkjob qstat

This code should work on any system that used PBS Torque.

I hope you find it useful,

  * Dirk

[View
Online](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2014/11/16/zsh+job+number+autocomplete)

Blogpost migrated from [ICER Wiki](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2014/11/16/zsh+job+number+autocomplete) using custom python script. Comment on errors below.
