Title: Investigation of the process of converting a C++ code into an implementable FPGA file
Date: 2019-07-24
Tags: Presentations


![Picture of Ana in front of her poster](//colbrydi.github.io/images/2019_ENSURE_Ana.jpg)

Summer 2019 [ENSURE Student](https://www.egr.msu.edu/graduate/ensure) Poster presentation at MidSure by Ana Flavia Borges de Almeida Barreto

A Field Programmable Gate Arrays (FPGAs) is an integrated circuit that can be “rewired” to become other circuits.  This ability makes FPGAs highly configurable and can significantly help speed up large scale computation used in scientific research.  While useful, FPGAs are often underutilized because of the complexity of developing circuits using Hardware Descriptive Languages (HDLs).  Software compilers exist (ex. OpenCL and Merlin) to make circuit design easier but these compilers require many hours to translate C++ into a variable circuit implementable file and can fail to even find a solution. Compiling a C++ code into an implementable file has three main steps. First, converting the C++ code into an HDL code, running the implementation of that code, and finally mapping the implementation for the specific FPGA. The first two steps are relatively quick to complete. However, the mapping part is what makes the whole process slow. It is difficult for the computer to take an arbitrary HDL circuit diagram and map it to the FPGA framework.  The calculations is an optimization problem that requires searching though many different circuit pathways to find one that will work.  The premise of this project is to explore methods to more efficiently converting C++ into FPGA applicable file. As this is a big problem to tackle, the first objective is to understand how the mapping is currently done (using Intel FPGA SDK), make a practical guide of installing and using the open source compiler and explore alternatives to the existing FPGA programming workflows.  
