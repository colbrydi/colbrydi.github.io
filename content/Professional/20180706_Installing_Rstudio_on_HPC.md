Title: Installing RStudio on the MSU HPCC
Date: 2018-07-06
Tags: HPC

![Rstudio](//www.rstudio.com/wp-content/uploads/2016/09/RStudio-Logo-Blue-Gray-250.png)

These instructions are for installing RStudio on the HPCC. RStudio provides a variety of installers on their website [https://www.rstudio.com/products/rstudio/download2/](https://www.rstudio.com/products/rstudio/download2/). However, the HPCC uses an older version of Linux and the precompiled binaries are not compatible.  Trying to install RStudio from the source code is an option but is also difficult due to the large numbers of libraries and compile dependancies.  I basically gave up trying to install RStudio on until I realized that a version is included as an option in Anaconda.  The following instructions show how to install RStudio using Anaconda.

## **Step 0:** Connect to the HPC.
Use ssh to connect to the HPCC and make sure you have a working X11 server (ex. MobaXterm on windows or XQuarts on Mac).  More information about X11 can be found here:

 - [Old HPCC Windows instructions](//wiki.hpcc.msu.edu/display/hpccdocs/Installing+an+X-server+on+Windows)
 - [Old HPCC Mac Instructions](https://wiki.hpcc.msu.edu/display/hpccdocs/Installing+an+X-server++for+Macs)

## **Step 1:** Download the Linux Anaconda installers

Find the latest Linux installer on the [Anaconda website](//www.anaconda.com/download/#linux). Right click on the download button for version 3.x and select "Copy Link". Use the ```wget``` command on the hpcc to download the script file by typing wget and then pasting the url. For Example:

```
wget https://repo.anaconda.com/archive/Anaconda3-5.2.0-Linux-x86_64.sh
```

## **Step 2:** Install anaconda using the defaults
Run the downloaded script in bash using the following command:

```
bash ./Anaconda3-5.2.0-Linux-x86_64.sh
```

The last question will ask you to add the anaconda folder to your bashrc file. Say yes...

## **Step 3:** Install RStudio

Use the conda install command to install RStudio.  Note you may need to run ```source ~/.bashrc``` first to update your path:

```
conda install rstudio
```

That should be it, RStudio is now installed in your home directory on the HPCC.  The only other thing you will need is a X11 server.  Assuming you have connected to the hpcc with an X11 connection you can run rstudio from the command line by typing:

```
rstudio
```
