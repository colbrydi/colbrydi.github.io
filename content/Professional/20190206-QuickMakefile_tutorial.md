Title: Quick Makefile Overview
Date: 2019-02-06

![Makefile as a Directed Acyclic Graph](//colbrydi.github.io/images/make.png){ width=320, align=right, hspace=10}

[Example Makefile](//colbrydi.github.io/images//Makefile)

A former student recently emailed me asking for a good reference about makefiles.  To be honest, I teach a lot about makefiles but I am not sure I have a go-to source.  I could have googled something but instead I just tapped out this quick description. I thought it makes for a fairly quick introduction to Makefiles.  Feel free to leave your favorite resource in the comments.

Makefiles are fairly simple in concept but are an entire programming language so can get very advanced. Basically a makefile consists of rules in the following format:
```
target : prerequisite_file1 prerequisite_file2 prequiste_file3 ...
  Recipe step 1
  Recipe step 2
  ...
```

When you type “make Target” on the command line you active the rule.  Then the Make program recursively activates rules to make each of the prerequisites.  If there is no rule to make a prerequisite it looks to see if the prerequisite file exists. If there is no rule and there is no file you will get an error.  However, assuming you have all the prerequisite files you need  for a rule, the Make program then runs the Recipe commands (things like gcc or whatever you want).  It is assumed that the commands will take the prerequisites as inputs and generate the target file (this is not always the case).
That is basically it.  Some more things to note:
*   If you just type “make” (with no target) the Make command assumes you are trying to make the first rule in the file.
*   Often the first rule target is called “all” with a bunch of prerequisites and no recipe steps.  This is just a high level rule that tells make to build all of your main target files. There is nothing special about the keyword “all” it is just used as a convention.
*   Often there is a rule at the end of a makefile called “clean” with no prerequisites.   You typically have to explicitly activate  this target by writing “make clean” (i.e. you normally do not make “clean” a prerequisite to a rule).  Typically the Recipe steps are remove (rm) commands that delete all intermediate files you may have generated (ex exe and \*.o files). Basically giving you a clean slate.
*   Makefiles can have variables and wildcards. In these cases they can get fairly advanced.
*   Make is fairly smart,  it will rebuild a target if the targets modification date is older than the modification date of it’s prerequisites.  This means that if you repeat the make command it will not automatically regenerate a file it thinks will not change.

That was fun for me.  I hope you find this description a useful first step.  

Above is a toy example of a makefile and a visual representation.

- Dirk
