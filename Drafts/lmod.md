Hey Conner,

Making modules isn’t too hard. They are a little cryptic and would need to review the process to give you a complete answer.  However, I should be able to get you started with the following info:

There are different module implementations. The HPCC uses Lua Modules which is called lmod and written in the Lua programming language:

https://www.tacc.utexas.edu/research-development/tacc-projects/lmod

http://lmod.readthedocs.io/en/latest/

Lua is not too hard to pick up but I never remember the syntax. The easy thing to do is just copy an existing module and use it as a template.  All of the hpc modules are stored in the following folder:

/opt/software/modulefiles

Modules are organized by file structure with individual files for different versions.  Once you have a module written (just copy one to start), make your own modulefiles folder in your home directory.  Then you can add your modulefiles folder to your module path and you are good to go. I forget the command but a quick “module help” lead me to this:

module use path

So, I think a quick test to get up and running may be:

cd ~
mkdir -p modulefiles/TEST
cd modulefiles
cp /opt/software/modulefiles/MODULE-TEMPLATE.lua ./modulefiles/TEST/1.2.3.lua

module use ~/modulefiles/

module load TEST

A quick check of the above gave me an error in my 1.2.3.lua file but it basically worked.  Please let me know if that helps.

Also note, the HPCC staff makes their lua modules really difficult with lots of support functions and error testing.  Your’s can be very simple with just dependancies and changing environment variables.

- Dirk



On Jul 13, 2017, at 11:19 AM, Connor Glosser <connor.glosser@gmail.com> wrote:

Hey Dirk -

Do you have any resources on how to write a module profile? I remember you mentioned it once when I had to manually pull in a bunch of specific versions and I can't seem to find anything on the wiki.

Thanks!
~Con
